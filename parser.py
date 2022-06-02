import logging 


key_words = ["num", "string", "loop", "if", "else"]
data_types = ["num", "string"]

def is_identifier(tokens, index):
    return index < len(tokens) and tokens[index][0] == "symbol" and tokens[index][1] not in key_words

def construct_assignment(tokens, index):
    validate_assigment(tokens, index)
    
    syntax_tree = dict()
    
    syntax_tree["assignment"] = dict()
    
    syntax_tree["assignment"]["assignee"] = tokens[index][1]
    syntax_tree["assignment"]["value"] = eval_expression(tokens, index+2) 

    return (index + 4, syntax_tree)

def eval_expression(tokens, index):

    tree = dict()   
        
    val1 = tokens[index]
    val2 = tokens[index+1]

    if val1[0] == "number" and val2[0] == ";":
        return int(val1[1])
    elif val2[0] in operators:
        tree["operation"] = dict()
        tree["operation"]["operand1"] = val1[1]
        tree["operation"]["type"] = val2[0]
        tree["operation"]["operand2"] = eval_expression(tokens, index + 2) 
    elif val2[0] == "(":
        tree["call"] = dict()
        tree["call"]["name"] = val1[1]
        tree["call"]["params"] = get_param_list(tokens, index + 2)

    return tree

def get_param_list(tokens, index):
    return list()
 
def validate_assigment(tokens, index):
    if tokens[index+1][0] != "=":
        raise ValueError("Expected '=' after identifier")

def construct_declaration(tokens, index):
    syntax_tree = dict()
    data_type = tokens[index]
    index += 1

    if not is_identifier(index, tokens):
        raise Exception("Expected identifier after declaration: " + data_type)

    identifier = tokens[index][1]
    syntax_tree["data_type"] = data_type
    syntax_tree["identifier"] = identifier


    if not index + 1 < len(tokens) or not tokens[index + 1][0] == ";":
        raise Exception("Expected ; after declaration")

    index += 2

    return (index, syntax_tree)

def construct_function(tokens, index):
    return dict()


def construct_loop(tokens, index):
    return dict()


def construct_tree(index, tokens):

    curr = tokens[index][0]

    if is_identifier(tokens, index):
        return construct_assignment(tokens, index)
    elif curr == "fun":
        return construct_function(tokens, index)
    elif curr == "loop":
        return construct_loop(tokens, index)
    elif curr in data_types:
        return construct_declaration(tokens, index) 

def parse(index, tokens):

    executables = list()

    while index < len(tokens):
        index, syntax_tree = construct_tree(index, tokens)
        executables.append(syntax_tree)

    return executables
