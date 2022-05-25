
import re

def read_string(delim, stream):
    token = ""
    stream.move_next()

    while True:
        ch = stream.peek()
        if ch is not None:
            if ch == delim:
                stream.move_next()
                break 
            else:
                token += ch
                stream.move_next()

    return token 

def read(first_char, stream, allowed_chars):
    token = first_char
    stream.move_next()

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
        print("Tokens: ", tokens)
        try:
            ch = stream.peek() 

            if ch == None:
                break

            print("top level: ", ch)
            if ch in " \n\t~": # ignore white spaces and comments 
                stream.move_next()
                continue

            elif ch in "{}();=<>":
                tokens.append((ch, ""))
                stream.move_next()
            elif ch in "+-/*":
                tokens.append(("operator", ch))
                stream.move_next()

            elif ch in ('"', "'"):
                tokens.append(("string", read_string(ch, stream)))

            elif re.match("[.0-9]", ch):
                tokens.append(("number", read(ch, stream, "[.0-9]")))

            elif re.match("[_a-zA-Z]", ch):  
                tokens.append(("symbol", read(ch, stream, "[_a-zA-Z]")))

            else:
                print("Exception for: ", ch)
                raise Exception("Invalid character in program: " + ch)   
        except StopIteration:
                break

    return tokens

        

             
