import argparse

parser = argparse.ArgumentParser()




parser.add_argument("text", type=str)
args = parser.parse_args()

start=int((len(args.text)-3)/2)
end=int((len(args.text)+3)/2)

print(start)
print(end)
print(args.text[start:end])

print(args.text[:start] + args.text[start:end].upper()+args.text[end:]) 