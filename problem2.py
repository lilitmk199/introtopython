import argparse

parser = argparse.ArgumentParser()


parser.add_argument("text")


args = parser.parse_args()
parser.add_argument("text")



print(args.text[5:-3])
