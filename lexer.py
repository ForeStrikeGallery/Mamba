
import re


def read_string(delim, source_iter):
    token = ""

    while True:
        try:
            ch = next(source_iter)
            if ch == delim:
                break
            else:
                token += ch 
        except StopIteration:
            break

    return token

def read(first_char, source_iter, allowed_chars):
    token = first_char

    while True:
        try:
            ch = next(source_iter)
            if re.match(allowed_chars, ch):
                token += ch 
            else:
                break 
        except StopIteration:
            break

    return token


def tokenize(source_iter):
    tokens = list()
    # convert program into a list of tokens 
    while True:
        try:
            ch = next(source_iter)
           # print(ch)
            if ch in " \n\t~": # ignore white spaces and comments 
                continue

            elif ch in "{}();=<>":
                tokens.append((ch, ""))
            elif ch in "+-/*":
                tokens.append(("operator", ch))

            elif ch in ('"', "'"):
                tokens.append(("string", read_string(ch, source_iter)))

            elif re.match("[.0-9]", ch):
                tokens.append(("number", read(ch, source_iter, "[.0-9]")))

            elif re.match("[_a-zA-Z]", ch):  
                tokens.append(("symbol", read(ch, source_iter, "[_a-zA-Z]")))

            else:
                print("Exception for: ", ch)
                raise Exception("Invalid character in program: " + ch)   
        except StopIteration:
                break

    return tokens

        

             
