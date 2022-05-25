import sys
from lexer import tokenize 
from os.path import exists
import os 


def validateArgs():

    if len(sys.argv) == 1:
        raise Exception("Mamba filepath not provided")

    if len(sys.argv) > 2:
        raise Exception("Too many arguments")

    filepath = os.getcwd() + "/" + sys.argv[1]
    
    if not exists(filepath):
        raise Exception("Invalid file path")

def get_iterator(source):
    while True:
        ch = source.read(1)
        if ch != "":
            yield ch 
        else:
            break

def main():
    validateArgs()   
    filepath = sys.argv[1]
    
    source_file = open(filepath)
    iterator = get_iterator(source_file)

    tokens = tokenize(iterator)
    print(tokens)

if __name__ == '__main__':
    main()
