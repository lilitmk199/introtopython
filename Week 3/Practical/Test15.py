import argparse


parser = argparse.ArgumentParser()

parser.add_argument("key",type=str)

parser.add_argument("value",type=str)


args = parser.parse_args()

my_dict= {"name1":"Lilit", "name2":"Ani", "name3":"Ashot"}

print(my_dict)

my_dict[args.key]=args.value

print(my_dict)