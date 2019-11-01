import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text")
parser.add_argument("start_index", type=int)
parser.add_argument("end_index",type=int)



args = parser.parse_args()

print(args.text[args.start_index:args.end_index])


 