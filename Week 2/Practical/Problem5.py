import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text")

args = parser.parse_args()

print (args.text)
print (args.text.upper())
print (args.text.lower())
print(args.text[:6] + args.text[6:].upper())