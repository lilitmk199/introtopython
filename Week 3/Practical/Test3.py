import argparse

parser = argparse.ArgumentParser()

parser.add_argument("value",type=int)

args = parser.parse_args()

list2=[4,7, 9, 10, 20, 30, 30, 30, 28, 1, 9, 30]

print(list2)

a=list2.count(args.value)

print(a)