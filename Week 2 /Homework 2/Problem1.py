import argparse

parser=argparse.ArgumentParser()

parser.add_argument("--num_y",type=int)
parser.add_argument("--num_d",type=int)

args = parser.parse_args()

import datetime

current_date= datetime.datetime(2019,11,1,12,15)

print("current date:", current_date)

print("final date:", current_date+datetime.timedelta(days=args.num_d))


