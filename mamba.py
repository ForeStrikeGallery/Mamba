import sys
from lexer import tokenize 
from peekable_stream import PeekableStream
from parser import parse
from os.path import exists
from executor import execute
import os 
import logging 

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")

def validateArgs():

    if len(sys.argv) == 1:
        raise Exception("Mamba filepath not provided")

    if len(sys.argv) > 2:
        raise Exception("Too many arguments")

    filepath = os.getcwd() + "/" + sys.argv[1]
    
    if not exists(filepath):
        raise Exception("Invalid file path")

    file_extension = filepath.split("/")[-1].split(".")[-1]

    logging.debug(file_extension)
    if file_extension != "mamba":
        raise Exception("Invalid file type. Mamba only interprets .mamba files")

def get_iterator(source_file):
    while True:
        ch = source_file.read(1)
        if ch != "":
            yield ch 
        else:
            break

def create_stream_from(filepath):
    source_file = open(filepath)
    iterator = get_iterator(source_file)
    return PeekableStream(iterator)

def main():
    validateArgs()   
    filepath = sys.argv[1]
   
    peekable_stream = create_stream_from(filepath)
    tokens = tokenize(peekable_stream)

    try:
        executables = parse(0, tokens)
        execute(executables)
    except Exception as e:
        print("Mamba compilation error: ", e)

if __name__ == '__main__':
    main()
