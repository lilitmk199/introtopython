mport argparse


parser = argparse.ArgumentParser()

parser.add_argument("value",type=int)

args = parser.parse_args()

set3={4,7, 9, 10, 11, 23, 54, 32, 1, 6, 7}

print(set3)

argparse in [min(set3):max(set3)]