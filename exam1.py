# from pathlib import *

# current_dir= Path.cwd()
# home_dir=Path.home()

from os import read


string = str(input())
input_filename=string



def count_lines(filename):
    with open(filename) as file:
            for int_readlines, str_readlines in enumerate(file):
                pass
    return int_readlines+1
                   
print(count_lines(input_filename))
 