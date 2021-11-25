import argparse

parser = argparse.ArgumentParser(description="Total number of path finding, input a positive integer")
parser.add_argument("-integer", default=2)
args = parser.parse_args()
total_movement = 2*int(args.integer)
num_variations = (total_movement-1)*2

print(num_variations)