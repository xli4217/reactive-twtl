'''
.. module:: postprocessing.py
   :synopsis: Post-processing module of logged data.

.. moduleauthor:: Cristian Ioan Vasile <cvasile@bu.edu>
'''

license_text='''
    Post-processing module of logged data.
    Copyright (C) 2018  Cristian Ioan Vasile <cvasile@bu.edu>
    Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Laboratory,
    Boston University

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import itertools as it

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from lomap import Ts

from spaces.base import Workspace, Point
from spaces.maps2d import BallRegion2D, BoxRegion2D, PolygonRegion2D, \
                          expandRegion, BoxBoundary2D, BallBoundary2D, \
                          PolygonBoundary2D, Point2D
from spaces.maps_nd import BallRegion, BoxRegion, BoxBoundary, BallBoundary
from robots import *
from planning import RRGPlanner, Request, LocalPlanner
from graphics.planar import addStyle, Simulate2D, drawBallRegion2D, to_rgba


def process_rrg_trial(logfile):
    '''Processes one global planner execution.'''
    # first process general data
    data = dict()
    line = ''
    line_data = 'dict()'
    for line in logfile:
        prefix, line_data = line.split('--')
        if prefix.lower().rfind('info') >= 0:
            data.update(eval(line_data))
            if line_data.lower().find('start global planning') >= 0:
                break
    print 'general data:', len(data)

    # second process data on global planner
    rrg_data = []
    iteration_data = None
    for line in logfile:
        prefix, line_data = line.split('--')
        if prefix.lower().rfind('info') >= 0:
            if line_data.lower().rfind('found solution') >=0:
                rrg_data.append(iteration_data)
                break
            if line_data.lower().find('iteration') >= 0:
                if iteration_data is not None:
                    rrg_data.append(iteration_data)
                iteration_data = dict()
            iteration_data.update(eval(line_data))
    print 'rrg data:', len(rrg_data)

    rrg_stat_data = eval(line_data)
    for line in logfile:
        prefix, line_data = line.split('--')
        if prefix.lower().rfind('info') >= 0:
            if line_data.lower().find('end global planning') >= 0:
                break
            rrg_stat_data.update(eval(line_data))
    print 'rrg_stat_data', len(rrg_stat_data)

    if rrg_stat_data:
        assert rrg_stat_data['Iterations'] == len(rrg_data), \
               str((rrg_stat_data['Iterations'], len(rrg_data)))
    return data, rrg_data, rrg_stat_data

def postprocessing_global_performance(logfilename, outdir,
                                      outfile='global_performance_stats.txt'):
    '''Parses log file and generates statistics on global TS planning.'''

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    with open(logfilename, 'r') as logfile:
        trials = []
        while True:
            _, rrg_data, rrg_stat_data = process_rrg_trial(logfile)
            if not (rrg_data and rrg_stat_data):
                break

            pa_runtime = 0
            for iteration_data in rrg_data:
                pa_runtime += (iteration_data.get('PA check forward runtime', 0)
                       + iteration_data.get('PA update forward runtime', 0)
                       + iteration_data.get('PA check backward runtime', 0)
                       + iteration_data.get('PA update backward runtime', 0))

            rrg_stat_data['TS nodes'], rrg_stat_data['TS edges'] = \
                                                    rrg_stat_data['Size of TS']
            rrg_stat_data['PA nodes'], rrg_stat_data['PA edges'] = \
                                                    rrg_stat_data['Size of PA']
            rrg_stat_data['PA update runtime'] = pa_runtime
            del rrg_stat_data['global policy']
            trials.append(rrg_stat_data)

    with open(os.path.join(outdir, outfile), 'w') as f:
        print>>f, '{'
        print>>f, '"no trials" :', len(trials), ','
        ops = [np.mean, np.min, np.max, np.std]
        for key in trials[0].keys():
            print>>f, '"{}"'.format(key), ':',
            print>>f, [op([trial[key] for trial in trials]) for op in ops], ','
        print>>f, '}'

    return trials

def postprocessing_local_performace(logfilename, outdir,
                                    outfile='local_performance_stats.txt'):
    '''Parses log file and generates statistics on local planning.'''

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    with open(logfilename, 'r') as logfile:
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                if line_data.lower().find('end global planning') >= 0:
                    break

        # third process data on local planner
        rrt_stat_data = dict()
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                if line_data.lower().find('initialize local planner') >= 0:
                    break
                rrt_stat_data.update(eval(line_data))
        print 'rrt_stat_data:', len(rrt_stat_data)

        rrt_data = []
        execution_data = dict()
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                if line_data.lower().find('local online planning finished') >=0:
                    rrt_data.append(execution_data)
                    break
                # NOTE: second condition is for compatibility with Cozmo logs
                if (line_data.lower().find('start local planning step') >= 0
                    or line_data.lower().find('plan start time') >= 0):
                    rrt_data.append(execution_data)
                    execution_data = dict()
                execution_data.update(eval(line_data))
        print 'rrt data:', len(rrt_data)

    metrics = [('tree size', True), ('local planning runtime', False),
               ('local planning execution', False)]
    rrt_data = rrt_data[1:]
    # NOTE: This is for compatibility with the Cozmo logs
    if 'local planning execution' not in rrt_data[0]:
        for d in rrt_data:
            duration = (d['plan stop time'] - d['plan start time'])*1000
            d['local planning execution'] = duration

    data = [len(d['requests']) for d in rrt_data]
    serviced = sum(n1 - n2 for n1, n2 in it.izip(data, data[1:]) if n1 > n2)

#     with open(os.path.join(outdir, outfile), 'w') as f:
#         print>>f, 'no trials:', len(rrt_data)
#         print>>f, 'no requests serviced', serviced
#         ops = [np.mean, np.min, np.max, np.std]
#         for key, positive in metrics:
#             if positive:
#                 print>>f, key, [op([trial[key] for trial in rrt_data
#                                           if trial[key] > 0]) for op in ops]
#             else:
#                 print>>f, key, [op([trial[key] for trial in rrt_data])
#                                                               for op in ops]

    ret = {'No trials': len(rrt_data), 'No requests serviced': serviced}
    for key, positive in metrics:
        if positive:
            ret[key] = [trial[key] for trial in rrt_data if trial[key] > 0]
        else:
            ret[key] = [trial[key] for trial in rrt_data]
    return ret

def postprocessing(logfilename, ts_filename, outdir, lts_index,
                   rrg_iterations, lts_iterations,
                   local_traj_iterations, generate=()):
    '''Parses log file and generate statistics and figures.'''

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    with open(logfilename, 'r') as logfile:
        # first process general data
        data = dict()
        line = ''
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                data.update(eval(line_data))
                if line_data.lower().find('start global planning') >= 0:
                    break
        print 'general data:', len(data)

        # second process data on global planner
        rrg_data = []
        iteration_data = None
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                if line_data.lower().rfind('found solution') >=0:
                    rrg_data.append(iteration_data)
                    break
                if line_data.lower().find('iteration') >= 0:
                    if iteration_data is not None:
                        rrg_data.append(iteration_data)
                    iteration_data = dict()
                iteration_data.update(eval(line_data))
        print 'rrg data:', len(rrg_data)

        rrg_stat_data = eval(line_data)
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                if line_data.lower().find('end global planning') >= 0:
                    break
                rrg_stat_data.update(eval(line_data))
        print 'rrg_stat_data', len(rrg_stat_data)

        assert rrg_stat_data['Iterations'] == len(rrg_data)

        # third process data on local planner
        rrt_stat_data = dict()
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                if line_data.lower().find('initialize local planner') >= 0:
                    break
                rrt_stat_data.update(eval(line_data))
        print 'rrt_stat_data:', len(rrt_stat_data)

        rrt_data = []
        execution_data = dict()
        for line in logfile:
            prefix, line_data = line.split('--')
            if prefix.lower().rfind('info') >= 0:
                if line_data.lower().find('local online planning finished') >=0:
                    rrt_data.append(execution_data)
                    break
                # NOTE: second condition is for compatibility with Cozmo logs
                if (line_data.lower().find('start local planning step') >= 0
                    or line_data.lower().find('plan start time') >= 0):
                    rrt_data.append(execution_data)
                    execution_data = dict()
                execution_data.update(eval(line_data))
        print 'rrt data:', len(rrt_data)

    # save useful information
    with open(os.path.join(outdir, 'general_data.txt'), 'w') as f:
        for key in ['Robot initial configuration', 'Robot step size',
                    'Global specification', 'Buchi size',
                    'Local specification']:
            print>>f, key, ':', data[key]

        for key in ['Iterations', 'global planning runtime', 'Size of TS',
                    'Size of PA']:
            print>>f, key, ':', rrg_stat_data[key]
        pre, suff = rrg_stat_data['global policy']
        print>>f, 'Global policy size :', (len(pre), len(suff))

        # key = 'Computing potential function runtime'
        # print>>f, key, ':', rrt_stat_data[key]

    # get workspace
    wspace, style = data['Workspace']
    wspace.boundary.style = style
    ewspace, style = data['Expanded workspace']
    ewspace.boundary.style = style

    # get robot
    robot_name = data['Robot name']
    initConf = data['Robot initial configuration']
    stepsize = data['Robot step size']
    robot = eval(data['Robot constructor'])
    robot.diameter = data['Robot diameter']
    robot.localObst = data['Local obstacle label']

    # create simulation object
    sim = Simulate2D(wspace, robot, ewspace)
    sim.config['output-dir'] = outdir

    # add regions to workspace
    for key, value in data.iteritems():
        if isinstance(key, tuple) and key[0] == "Global region":
            r, style = value
            # add styles to region
            addStyle(r, style=style)
            # add region to workspace
            sim.workspace.addRegion(r)
            # create expanded region
            er = expandRegion(r, robot.diameter/2)
            # add style to the expanded region
            addStyle(er, style=style)
            # add expanded region to the expanded workspace
            sim.expandedWorkspace.addRegion(er)

    # get local requests and obstacles
    localSpec = data['Local specification']
    requests = []
    obstacles = []
    for key, value in data.iteritems():
        if isinstance(key, tuple) and key[0] == "Local region":
            r, style, path, is_request = value
            # add styles to region
            addStyle(r, style=style)
            # add path
            if path:
                r.path = it.cycle(path)
                r.original_path = path[:]
            # add to requests or obstacles lists
            if is_request:
                name = next(iter(r.symbols))
                requests.append(Request(r, name, localSpec[name]))
            else:
                obstacles.append(r)

    # get robot sensor
    robot.sensor = eval(data['Robot sensor constructor'])

    # create RRG planner and load transition system, and global policy
    sim.offline = RRGPlanner(robot, None, 1)
    prefix, suffix = rrg_stat_data['global policy']
    sim.solution = (prefix, suffix[1:])
    print 'Global policy size:', len(prefix), len(suffix)

    if any(option in generate for option in
                ('workspace', 'expanded workspace', 'global solution')):
        # set larger font for saving figures
        for r in sim.workspace.regions | sim.expandedWorkspace.regions:
            r.fontsize_orig = r.textStyle.get('fontsize', 12)
            r.textStyle['fontsize'] = 24

        # display workspace
        if 'workspace' in generate:
            sim.display(save='workspace.png')
        # display expanded workspace
        if 'expanded workspace' in generate:
            sim.display(expanded=True, save='eworkspace.png')
        # display solution for off-line problem
        if 'global solution' in generate:
            ts = sim.offline.ts
            sim.offline.ts = Ts.load(ts_filename)
            sim.display(expanded=True, solution=prefix+suffix[1:],
                        save='global_solution.png')
            sim.offline.ts = ts

        # restore original fontsize
        for r in sim.workspace.regions:
            r.textStyle['fontsize'] = r.fontsize_orig
            del r.fontsize_orig

    # display both workspaces
    if 'both workspaces' in generate:
        sim.display(expanded='both')

    # show construction of rrg
    sim.offline.ts.init[initConf] = 1
    if 'RRG construction' in generate:
        sim.config['global-ts-color'] = {'node_color': 'blue',
                                         'edge_color': 'black'}
        sim.config['video-interval'] = 500
        sim.config['video-file'] = 'rrg_construction.mp4'
        sim.save_rrg_process(rrg_data)
        # reset to default colors
        sim.defaultConfiguration(reset=['global-ts-color'])

    if 'RRG iterations' in generate:
        sim.config['global-ts-color'] = {'node_color': 'blue',
                                         'edge_color': 'black'}
        rrg_iterations = [i + (i==-1)*(len(rrg_data)+1) for i in rrg_iterations]
        sim.save_rrg_iterations(rrg_data, rrg_iterations)
        # reset to default colors
        sim.defaultConfiguration(reset=['global-ts-color'])

    # set to global and to save animation
    sim.offline.ts = Ts.load(ts_filename)
    print 'TS size', sim.offline.ts.size()
    if 'offline plan' in generate:
        sim.config['video-interval'] = 30
        sim.config['sim-step'] = 0.02
        sim.config['video-file'] = 'global_plan.mp4'
        sim.simulate(loops=1, offline=True)
        sim.play(output='video', show=False)
        sim.save()


    # get online trajectory
    sim.offline.ts = Ts.load(ts_filename)
    trajectory = [d['new configuration'] for d in rrt_data]
    local_plans = [d['local plan'] for d in rrt_data] + [[]]
    potential = [d['potential'] for d in rrt_data] + [0]
    requests = [d['requests'] for d in rrt_data] + [[]]
    print len(trajectory), len(local_plans)

    if 'trajectory' in generate:
        # set larger font for saving figures
        for r in sim.workspace.regions | sim.expandedWorkspace.regions:
            r.fontsize_orig = r.textStyle.get('fontsize', 12)
            r.textStyle['fontsize'] = 24

        sim.config['trajectory-min-transparency'] = 0.2 # fading
        sim.config['trajectory-history-length'] = len(trajectory) # full history
        sim.config['global-policy-color'] = 'orange'

        sim.online = LocalPlanner(None, sim.offline.ts, robot, localSpec)
        sim.online.trajectory = trajectory
        sim.online.robot.sensor.requests = []
        sim.display(expanded=True, solution=prefix+suffix[1:], show_robot=False,
                    localinfo=('trajectory',), save='trajectory.png')
        sim.defaultConfiguration(reset=['trajectory-min-transparency',
                            'trajectory-history-length', 'global-policy-color'])

        # restore original fontsize
        for r in sim.workspace.regions:
            r.textStyle['fontsize'] = r.fontsize_orig
            del r.fontsize_orig

    # local plan visualization
    sim.online = LocalPlanner(None, sim.offline.ts, robot, localSpec)
    sim.online.trajectory = trajectory
    if 'online plan' in generate:
        sim.config['video-interval'] = 30
        sim.config['sim-step'] = 0.01
        sim.config['video-file'] = 'local_plan.mp4'
        sim.simulate(offline=False)
        sim.play(output='video', show=False,
                 localinfo={'trajectory': trajectory, 'plans': local_plans,
                            'potential': potential, 'requests': requests})
        sim.save()

    if 'online trajectory iterations' in generate:
        sim.config['sim-step'] = 0.05
        sim.config['trajectory-min-transparency'] = 1.0 # no fading
        sim.config['trajectory-history-length'] = 100000 # entire history
        sim.config['image-file-template'] = 'local_trajectory_{frame:04d}.png'
        sim.config['global-policy-color'] = 'orange'
        # simulate and save
        sim.simulate(offline=False)
        sim.play(output='plots', show=False,
                 localinfo={'trajectory': trajectory, 'plans': local_plans,
                            'potential': potential, 'requests': requests})
        sim.save(output='plots', frames=local_traj_iterations)
        # set initial values
        sim.defaultConfiguration(reset=['trajectory-min-transparency',
                            'trajectory-history-length', 'image-file-template',
                            'global-policy-color'])

    msize = np.mean([d['tree size'] for d in rrt_data if d['tree size'] > 0])
    print 'Mean size:', msize
    for k, d in enumerate(rrt_data):
        if d['tree size'] > 0:
            print (k, d['tree size'])

    if any(option in generate for option in
                                        ('LTS iterations', 'LTS construction')):
        idx = lts_index
        print rrt_data[idx]['tree size']
        print 'current state:', rrt_data[idx-1]['new configuration']

        lts_data = sorted([v for k, v in rrt_data[idx].items()
                                if str(k).startswith('lts iteration')],
                          key=lambda x: x[0])
    #     print lts_data

        sim.online.lts = Ts(directed=True, multi=False)
        sim.online.lts.init[rrt_data[idx-1]['new configuration']] = 1
        # reset and fast-forward requests' locations
        for r in sim.robot.sensor.all_requests:
            aux = it.cycle(r.region.original_path)
            for _ in range(idx-1):
                r.region.translate(next(aux))
        sim.robot.sensor.requests = [r for r in sim.robot.sensor.all_requests
                                           if r in rrt_data[idx]['requests']]
        if 'LTS construction' in generate:
            sim.config['video-interval'] = 500
            sim.config['video-file'] = 'lts_construction.mp4'
            sim.save_lts_process(lts_data, endframe_hold=20)

        if 'LTS iterations' in generate:
            lts_iterations = [i + (i==-1)*len(lts_data) for i in lts_iterations]
            sim.save_lts_iterations(lts_data, lts_iterations)

    if 'LTS statistics' in generate:
        metrics = [('tree size', True), ('local planning runtime', False),
                   ('local planning execution', False)]
        rrt_data = rrt_data[1:]
        # NOTE: This is for compatibility with the Cozmo logs
        if 'local planning execution' not in rrt_data[0]:
            for d in rrt_data:
                duration = (d['plan stop time'] - d['plan start time'])*1000
                d['local planning execution'] = duration

        data = [len(d['requests']) for d in rrt_data]
        serviced = sum(n1 - n2 for n1, n2 in it.izip(data, data[1:]) if n1 > n2)

        with open(os.path.join(outdir, 'local_performance_stats.txt'), 'w') as f:
            print>>f, 'no trials:', len(rrt_data)
            print>>f, 'no requests serviced', serviced
            ops = [np.mean, np.min, np.max, np.std]
            for key, positive in metrics:
                if positive:
                    print>>f, key, [op([trial[key] for trial in rrt_data
                                              if trial[key] > 0]) for op in ops]
                else:
                    print>>f, key, [op([trial[key] for trial in rrt_data])
                                                                  for op in ops]

def box_plots(data, outfile='stat_{}.png'):
    '''Saves boxplot figures for various performance parameters.'''
    sns.set(style="whitegrid")
    dims = data.keys()
    xname = 'Dimension'
    ynames = {
        'Iterations' : 'Iterations',
        'PA update runtime' : 'Duration of PA update step [s]',
        'PA nodes' : 'Number of PA states',
        'PA edges' : 'Number of PA transitions',
        'global planning runtime' : 'Duration of global planning [s]',
        'TS nodes' : 'Number of TS states',
        'TS edges' : 'Number of TS edges'
    }
    for key in ynames:
        fig = plt.figure(key)
        yname = ynames[key]
        df = pd.concat([pd.DataFrame([(dim, v[key]) for v in data[dim]],
                                     columns=[xname, yname])
                        for dim in dims], ignore_index=True)
        if key in ('PA update runtime', 'global planning runtime'):
            df[yname] /= 1000
        bp = sns.boxplot(x=xname, y=yname, data=df, width=.5)
        if key in ('Iterations', 'global planning runtime'):
            bp.set_yscale('log')
        plt.savefig(outfile.format(key.replace(' ', '_')), dpi=fig.dpi)

def workspace_plot(outfile='highdim_workspace.png'):
    '''Plot planar workspace for the high-dimensional case study.'''
    # define boundary: unit hypercube
    boundary = BoxBoundary([[0, 1], [0, 1]])
    # define boundary style
    boundary.style = {'color' : 'black'}
    # create robot's workspace
    wspace = Workspace(boundary=boundary)

    # create robot object
    initConf = Point2D((0.1, 0.1)) # start close to the origin
    robot = FullyActuatedRobot('Robot-highdim', init=initConf, wspace=wspace)
    robot.diameter=0

    # create simulation object
    sim = Simulate2D(wspace, robot, None)

    # regions of interest
    R1 = (BoxRegion2D([[.00,  .20], [.00,  .20]], ['r1']), 'brown')
    R2 = (BoxRegion2D([[.25,  .40], [.40,  .55]], ['r2']), 'green')
    R3 = (BoxRegion2D([[.70, 1.00], [.40,  .60]], ['r3']), 'red')
    R4 = (BoxRegion2D([[.00,  .50], [.90, 1.00]], ['r4']), 'magenta')
    # global obstacles
    O1 = (BoxRegion2D([[.20,  .30], [.30,  .35]], ['o1']), 'gray')
    O2 = (BoxRegion2D([[.15,  .20], [.40,  .60]], ['o2']), 'gray')
    O3 = (BoxRegion2D([[.50,  .55], [.30,  .80]], ['o3']), 'gray')
    # local obstacles
    L1 = (BoxRegion2D([[.45,  .50], [.75,  .80]], ['LO']), to_rgba('gray', .6))
    L2 = (BoxRegion2D([[.90, 1.00], [.50,  .55]], ['LO']), to_rgba('gray', .6))
    L3 = (BoxRegion2D([[.75,  .80], [.20,  .25]], ['LO']), to_rgba('gray', .6))

    # add all regions
    regions = [R1, R2, R3, R4, O1, O2, O3, L1, L2, L3]

    # add regions to workspace
    for r, c in regions:
        # add styles to region
        addStyle(r, style={'facecolor': c})
        r.textStyle['fontsize'] = 24
        # add region to workspace
        sim.workspace.addRegion(r)

    # set the robot's sensor
    sensingShape = BallBoundary([0, 0], 0.001)
    robot.sensor = BoundingBoxSimulatedSensor(robot, sensingShape, [], [])

    # display workspace
    sim.display(save=outfile, figsize=(7, 7))

def plot_local_performance(data, outfile='local_stat_{}.png'):
    '''Generates and plots local performance graphs.'''

    sns.set(style="whitegrid")
    dims = data.keys()
    xname = 'Dimension'
    ynames = {
        'No trials' : 'No trials',
        'No requests serviced' : 'No requests serviced',
#         'tree size' : 'Tree size',
        'local planning runtime' : 'Duration of local planning [s]',
    }
    for key in ynames:
        fig = plt.figure(key)
        yname = ynames[key]
        if key in ('No trials', 'No requests serviced'):
            df = pd.DataFrame([(dim, data[dim][key]) for dim in dims],
                          columns=[xname, yname])
            plt.plot(df[xname], df[yname], 'o', color='black')
            plt.xlabel(xname)
            plt.ylabel(yname)
            plt.xticks(dims)
            plt.xlim(dims[0]-1, dims[-1]+1)
        else:
            df = pd.concat([pd.DataFrame([(dim, v) for v in data[dim][key]],
                                         columns=[xname, yname])
                            for dim in dims], ignore_index=True)
            if key in ('local planning runtime',):
                df[yname] = df[yname] / 1000.0
            bp = sns.boxplot(x=xname, y=yname, data=df, width=.5)
            if key in ('local planning runtime',):
                bp.set_yscale('log')
        plt.savefig(outfile.format(key.replace(' ', '_')), dpi=fig.dpi)
        plt.show()


if __name__ == '__main__':

    postprocessing(logfilename='../data_ijrr/schlumberger/ijrr_schlumberger.log',
                   ts_filename='../data_ijrr/schlumberger/ts.yaml',
                   outdir='../data_ijrr/schlumberger',
                   lts_index=48,
                   rrg_iterations=[30, 75, 150, -1],
                   lts_iterations=[15, 30, 45, -1],
                   local_traj_iterations=[155, 187, 273, 329, 749, 1191],
                   generate=[ # Defines what media to generate 
                         'workspace',
                         'expanded workspace',
                         'global solution',
#                         'both workspaces',
#                         'RRG construction',
#                         'RRG iterations',
                         'offline plan',
#                         'online plan',
#                         'online trajectory iterations',
#                         'LTS construction',
#                         'LTS iterations',
#                         'LTS statistics',
                        ])

