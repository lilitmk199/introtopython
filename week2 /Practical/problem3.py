import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()

if args.name:
    print( "Welcome", args.name)