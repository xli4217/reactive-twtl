# Copyright (C) 2015, Cristian-Ioan Vasile (cvasile@mit.edu)
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from classes import Buchi, Fsa, Rabin
import numpy as np

def test_buchi():
    # specs = ['F a && G ! b']
    specs = ['Fa && G(a -> XF(b || c)) && G!((a && b) || (a && c) || (c && b) || (a && b && c) ) ']
    for spec in specs:
        aut = Buchi()
        aut.from_formula(spec)
        aut.visualize(draw='pydot')
        print(aut)

def test_fsa():
    #specs = ['F a && F !b']
    #specs = ['F a && F b && F c && !a U b && !b U c']
    #specs = ['Fa && (Fa->XFb) && (Fb -> XFc) && (!b U a) && (!c U b)']
    specs = ['Fa && Fb', 'Fc']
    #specs = ['Fa && G(a -> XF(b || c)) && G!((a && b) || (a && c) || (c && b) || (a && b && c) ) ']
    #specs = ['Fa && G(a -> XF(b || c)) ']
    #specs = ['Fa && Fb && Fc','Fa', 'Fb', 'Fc']
    #specs = ['F(a && b) || F(c && d)']
    from matplotlib.pyplot import pause
    for spec in specs:
        aut = Fsa()
        aut.from_formula(spec)
        # aut.add_trap_state()
        #aut.visualize(draw='pydot')
        aut.visualize(draw='pydot')
        #print(aut)
        tmp = list(aut.init.keys())
        print(tmp)
        print(aut.g.node)
        pause(2)
        # print("-------")
        # print("{0:02b}".format(0))
        # print("{0:02b}".format(1))
        # print("{0:02b}".format(2))
        # print("{0:02b}".format(3))
        # print(aut.symbols_w_prop("a"))
        # print(aut.bitmap_of_props(["a"]))
        # print(aut.next_states_of_fsa("T0_init", ["a","b"]))
        
        
        
def test_rabin():
    specs = ['F a && G ! b']
    
    for spec in specs:
        aut = Rabin()
        aut.from_formula(spec)
        aut.visualize(draw='pydot')
       
        print(aut)

if __name__ == '__main__':
    #test_buchi()
    test_fsa()
    #test_rabin() # can't find ltl2dstar

