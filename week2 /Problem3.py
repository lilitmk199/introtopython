import argparse

parser = argparse.ArgumentParser()




parser.add_argument("text", type=str)
parser.add_argument("first_word", type=str)
parser.add_argument("second_word", type=str)

args = parser.parse_args()

print (args.text.replace(args.first_word, args.second_word))


