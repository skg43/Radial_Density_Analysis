from ReadInput   import *
from Globals     import *
from ParseFrames import *
from Reports   import *

def DP():
   prm = ReadInput()
   print("Input read!!!")
   gl_def(prm)
   frames, total_frames, atoms_per_frame = Load_all_Frames()
   print("...")
   print("Writing output...")
   print("...")
   Report(frames, total_frames, atoms_per_frame)
   print("Output Written!!")

@timer
def main():
	DP()

if __name__ == '__main__':
	main() # Entry point for running the Radial Density analysis
