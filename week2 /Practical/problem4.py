import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age")

args = parser.parse_args()

if args.age:
  print ("Happy birthday, you are already", args.age, "years old!")
 
 