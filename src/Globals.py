
"""
NTF2 Flux Analysis through NPC model
All rights reserved.

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    Defines global variables and constants used throughout the flux analysis project.
"""

import 	sys
from 	math import *
import itertools as it
import concurrent.futures as cf
import os
import time
from functools import wraps


class gl:

	"""
	Defines data structures and methods for tracking molecule positions and flux events.
	"""

	ENTRY_z= None
	EXIT_z= None
	N_nup= None
	N_wall= None
	N_Kap= None
	N_NTF2= None
	AA_Kap= None
	AA_NTF2= None
	NO_FRAMES= None
	version= None



def gl_def(prm):

#***************************************************
#
#				Simulation parameters
#
#***************************************************
	gl.Entry_z = prm[0]
	gl.Exit_z = prm[1]
	gl.max_dist = prm[2]
	gl.n_bins = prm[3]
	gl.N_Residue = prm[4]
	gl.ATOM_COUNT = prm[5]
	gl.START_INDEX = prm[6]
	gl.NO_FRAMES = prm[7:]

#***************************************************
#
#				global settings
#
#***************************************************


	gl.H_lines = 9 # number of lines of the header section
	gl.Length = abs(gl.Exit_z - gl.Entry_z)
	gl.pi = pi
	gl.factor = fabs(gl.n_bins / gl.max_dist)
	
	gl.cnt = 0
	gl.dp_sum = gl.norm = gl.dp_rr_sum = 0.0
	gl.file_index=0




def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)   # Call the function
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' finished in {elapsed_time:.2f} seconds")
        return value
    return wrapper_timer
	

