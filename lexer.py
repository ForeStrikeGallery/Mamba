
import re

debug = True  

def log_debug(string):
    if debug:
        print(string)


def read_string(delim, stream):
    token = ""

    while True:
        ch = stream.peek_and_move()
        if ch is not None:
            if ch == delim:
                break 
            else:
                token += ch

    return token 

def read(first_char, stream, allowed_chars):
    token = first_char

    while True:
        ch = stream.peek()
        if ch is not None:
            if re.match(allowed_chars, ch):
                token += ch 
                stream.move_next()
            else:
                break 
        else:
            break
    return token

def skip_line(stream):
    while stream.peek() is not "\n" and stream.peek() is not None:
        stream.move_next()
        

def tokenize(stream):
    tokens = list()

    ch = " " 

    while ch is not None:
        if ch in " \n\t": # ignore white spaces 
            pass 
        elif ch in "~":
            skip_line(stream)
        elif ch in "{}();=<>":
            tokens.append((ch, ""))
        elif ch in "+-/*":
            tokens.append(("operator", ch))
        elif ch in ('"', "'"):
            tokens.append(("string", read_string(ch, stream)))
        elif re.match("[.0-9]", ch):
            tokens.append(("number", read(ch, stream, "[.0-9]")))
        elif re.match("[_a-zA-Z]", ch):  
            tokens.append(("symbol", read(ch, stream, "[_a-zA-Z]")))
        else:
            raise Exception("Invalid character in program: " + ch)   

        ch = stream.peek_and_move()

    return tokens

             
