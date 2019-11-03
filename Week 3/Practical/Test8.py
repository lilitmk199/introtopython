import argparse


parser = argparse.ArgumentParser()

parser.add_argument("value",type=int)

args = parser.parse_args()

set1={4,7, 9, 10, 11, 23, 54, 32, 1, 6, 7}

print(set1)

set1.add(args.value)

print(set1)