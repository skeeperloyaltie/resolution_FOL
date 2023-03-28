import sys

def parse_cnf(cnf_file):
    with open(cnf_file) as f:
        lines = f.readlines()

    predicates = set()
    variables = set()
    constants = set()
    functions = set()
    clauses = []

    for line in lines:
        if line.startswith('c') or line.startswith('p'):
            continue
        clause = []
        terms = line.strip().split(' ')
        for term in terms:
            if term == '0':
                break
            if term.startswith('-'):
                clause.append((False, parse_term(term[1:], predicates, variables, constants, functions)))
            else:
                clause.append((True, parse_term(term, predicates, variables, constants, functions)))
        clauses.append(clause)

    return predicates, variables, constants, functions, clauses

def parse_term(term, predicates, variables, constants, functions):
    if term.islower():
        variables.add(term)
        return term
    elif term[0].isupper():
        constants.add(term)
        return term
    elif '(' in term:
        function, variables_str = term.split('(')
        variables_str = variables_str[:-1]
        variables_list = variables_str.split(',')
        variables.update(variables_list)
        functions.add(function)
        return (function, variables_list)
    else:
        raise ValueError('Invalid term: {}'.format(term))

def is_satisfiable(predicates, variables, constants, functions, clauses):
    for variable_assignment in _generate_variable_assignments(variables, constants):
        if all(_eval_clause(clause, variable_assignment) for clause in clauses):
            return True
    return False

def _generate_variable_assignments(variables, constants):
    num_vars = len(variables)
    for i in range(2 ** num_vars):
        binary_str = bin(i)[2:].rjust(num_vars, '0')
        var_assignments = dict(zip(variables, binary_str))
        var_assignments.update({constant: '1' for constant in constants})
        yield var_assignments

def _eval_clause(clause, variable_assignment):
    for term in clause:
        term_value = term[0]
        if term[0] in variable_assignment:
            term_value = variable_assignment[term[0]]
        elif term[0] in variable_assignment.values():
            term_value = list(variable_assignment.keys())[list(variable_assignment.values()).index(term[0])]
        else:
            term_value = term[0]
        if not term[2] and term_value == '1':
            return True
        elif term[2] and term_value == '0':
            return True
    return False

if __name__ == '__main__':
    cnf_file = sys.argv[1]
    predicates, variables, constants, functions, clauses = parse_cnf(cnf_file)
    if is_satisfiable(predicates, variables, constants, functions, clauses):
        print("The CNF is satisfiable.")
    else:
        print("The CNF is unsatisfiable.")
