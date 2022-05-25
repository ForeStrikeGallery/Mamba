import sys
from lexer import Lexer
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

def main():
    validateArgs()   
    filepath = sys.argv[1]
    
    source = open(filepath).read()
    print(source) 
    
    lexer = Lexer()
    tokens = lexer.tokenize()

if __name__ == '__main__':
    main()
