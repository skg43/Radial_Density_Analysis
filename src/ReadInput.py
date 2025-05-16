
"""
NTF2 Flux Analysis through NPC model
All rights reserved.

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    Reads the user-provided input.inp file and parses simulation parameters for analysis.
"""

import sys

def ReadInput():

	"""
	Parses the input.inp file to extract simulation parameters.

	Returns:
		  dict: Dictionary containing parsed parameters.
	"""
	try:
		f_read1 = open('../input.inp', 'r')

		(xx, NO_FRAMES, ii) = ([], [], 0)

		for line in f_read1:
			ii += 1
			if ii == 12:
				yy = float(line)
				xx.append(yy)

			if ii == 14:
				yy = float(line)
				xx.append(yy)

			if ii == 16:
				yy = float(line)
				xx.append(yy)

			if ii == 18:
				yy = int(line)
				xx.append(yy)

			if ii == 20:
				yy = int(line)
				xx.append(yy)

			if ii == 22:
				yy = int(line)
				xx.append(yy)

			if ii == 24:
				yy = int(line)
				xx.append(yy)

			if ii == 26:				
				yy = line.split()
				[xx.append(int(yy[i])) for i in range(len(yy))]

	
	except IOError:
		print("***")
		print("*** error: can't find input file!")
		print("***")
		sys.exit()

	return xx
