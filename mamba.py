import sys
from lexer import tokenize 
from peekable_stream import PeekableStream
from parser import parse
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

def get_iterator(source_file):
    while True:
        ch = source_file.read(1)
        if ch != "":
            yield ch 
        else:
            break

def main():
    validateArgs()   
    filepath = sys.argv[1]
    
    source_file = open(filepath)
    iterator = get_iterator(source_file)
    peekable_stream = PeekableStream(iterator)
    tokens = tokenize(peekable_stream)
    print("Tokens: ", tokens)
    print("Syntax tree: ", parse(tokens))

if __name__ == '__main__':
    main()
