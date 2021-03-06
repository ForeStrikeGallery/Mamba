
key_words = ["num", "string"]


def is_identifier(index, tokens):
   # print(index, tokens)
    return index < len(tokens) and tokens[index][0] == "symbol" and tokens[index][1] not in key_words

def create_declaration(index, tokens, data_type):

    syntax_tree = dict()
    index += 1

    if not is_identifier(index, tokens):
        raise Exception("Expected identifier after declaration: " + data_type)

    identifier = tokens[index][1]
    syntax_tree["data_type"] = data_type
    syntax_tree["identifier"] = identifier


    if not index + 1 < len(tokens) or not tokens[index + 1][0] == ";":
        print(tokens, index, syntax_tree)
        raise Exception("Expected ; after declaration")

    index += 2

    return (index, syntax_tree)


def create_tree(index, tokens):

    syntax_tree = dict()

    if tokens[index][0] == "symbol":
        if tokens[index][1] == "num":
            index, syntax_tree["declaration"] = create_declaration(index, tokens, "num")
        elif tokens[index][1] == "string":
            index, syntax_tree["declaration"] = create_declaration(index, tokens, "string")

    return (index, syntax_tree)


def parse(index, tokens):

    executables = list()

    while index < len(tokens):
        index, syntax_tree = create_tree(index, tokens)
        executables.append(syntax_tree)

    return executables
