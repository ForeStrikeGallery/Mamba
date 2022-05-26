from lexer import log_debug 

global_variables = dict()

def execute(executables):

	for executable in executables:
		if len(executable.keys()) > 1:
			raise Exception("More than one task in executable")

		if list(executable.keys())[0] == "declaration":
			execute_declaration(executable["declaration"])


def execute_declaration(syntax_tree):

	mamba_vname = syntax_tree["data_type"] + "_" + syntax_tree["identifier"]

	if mamba_vname in global_variables:
		raise Exception(syntax_tree["identifier"] + " already declared")

	if syntax_tree["data_type"] == "num":
		create_num_variable(mamba_vname)


def create_num_variable(mamba_vname):

	val = 0
	global_variables[mamba_vname] = val 
	log_debug("variable of type num declared")
	log_debug(global_variables)




