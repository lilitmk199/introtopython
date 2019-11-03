import argparse


parser = argparse.ArgumentParser()

parser.add_argument("value",type=int)

args = parser.parse_args()

set3={4,7, 9, 10, 11, 23, 54, 32, 1, 6, 7}



print(set3)

print(min(set3))
print(max(set3))


if min(set3)<args.value<max(set3):
 print("True")
else:
 print("false")