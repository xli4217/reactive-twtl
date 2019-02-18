'''
.. module:: fullyActuatedRobot
   :synopsis: Module implements a fully actuated robot (an integrator).

.. moduleauthor:: Cristian Ioan Vasile <cvasile@bu.edu>
'''

'''
    Module implements a fully actuated robot (an integrator).
    Copyright (C) 2014-2016  Cristian Ioan Vasile <cvasile@bu.edu>
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

from robot import Robot


class FullyActuatedRobot(Robot):
    '''
    Class representing a fully actuated robot.
    '''
    def __init__(self, name, init=None, wspace=None, stepsize=0.1):
        Robot.__init__(self, name, initConf=init, cspace=wspace, wspace=wspace,
                       controlspace=stepsize)

    def getSymbols(self, position, local=False):
        '''Returns the symbols satisfied at the given position.
        If `local` is False global symbols are returned, otherwise local ones
        are computed.
        '''
        if local:
            return set([r.name for r in self.sensor.sensed_requests
                            if r.region.intersects(position)])
        return self.wspace.getSymbols(position)

    def steer(self, start, target, atol=0):
        '''Returns a position that the robot can move to from the start position
        such that it steers closer to the given target position using the
        robot's dynamics.

        Note: It simulates the movement.
        '''
        s = start.coords
        t = target.coords
        dist = self.cspace.metric(s, t)
        if dist <= self.controlspace + atol:
            return target
        return self.initConf.__class__(s + (t-s) * self.controlspace/dist)

    def isSimpleSegment(self, u, v):
        '''Returns True if the curve [x, y] = H([u, v]) in the workspace space
        does not intersect other regions than the ones x and y belong to.
        In the definition, H is a submersion mapping the line segment [u, v] in
        the configuration space to a curve [x, v] in the workspace, where the
        trajectory is annotated with the properties of the regions it
        intersects.
        Since the robot is a fully actuate points, the configuration space is
        the same as the workspace and the submersion is the identity map.

        Note: assumes non-overlapping regions.
        '''
        nrRegUV = len(self.cspace.intersectingRegions(u, v))
        regU = self.cspace.intersectingRegions(u)
        regV = self.cspace.intersectingRegions(v)

        # if both endpoints of the segment are in the free space
        if (not regU) and (not regV):
            return nrRegUV == 0
        # if one endpoint is in the free space
        if (not regU) or (not regV): # NOTE: assumes convex regions
            return nrRegUV == 1
        # if both endpoints are in the same region
        if regU[0] == regV[0]:
            # NOTE: experimental for non-convex regions
            # and regU.contains(u, v):
            return nrRegUV == 1
        # if the endpoints belong to two different regions
        return nrRegUV == 2

    def collision_free(self, plan, local_obstacles):
        '''Checks if the plan is obstacle free with respect to the locally
        detected ones.
        '''
        if local_obstacles:
            aux = [self.currentConf] + plan
            for start, stop in zip(aux[:-1], aux[1:]):
                if any([obs.intersects(start, stop)
                                         for obs in local_obstacles]):
                    return False
            return True
        return True

    def collision_free_segment(self, u, v, local_obstacles):
        '''Checks if a line segment is obstacle free.'''
        if local_obstacles:
            return not any([obs.intersects(u, v) for obs in local_obstacles])
        return True

    def __str__(self):
        return 'Fully actuated robot'
