
import argparse
from argparse import Namespace

parser = argparse.ArgumentParser()

def argument_pa():
   parser.add_argument('--host', action='extend', nargs='+', type=str, help='iDRAC IP')
   parser.add_argument('-f', action='store', dest='CONFIG_FILE', type=str, help='iDRAC yaml configuration file')
   parser.add_argument('--user', action='store', dest='USER', type=str, help='iDRAC user name')
   return (parser.parse_args())



a = argument_pa().host
new_a = []
new_a = a[0].split(',')

for x in new_a:
  print(x)
