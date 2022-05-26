
import re

debug = False

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

    return token


def tokenize(stream):
    tokens = list()
    # convert program into a list of tokens 
    while True:
        log_debug("Tokens: " + str(tokens))
        try:
            ch = stream.peek_and_move() 

            if ch == None:
                break

            log_debug("top level: " + ch)
            if ch in " \n\t": # ignore white spaces 
                continue

            if ch in "~":
                while stream.peek() is not "\n":
                    stream.move_next()

                continue  

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
        except StopIteration:
                break

    return tokens

        

             
