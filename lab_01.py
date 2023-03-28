import sys

def is_clause_satisfied(clause, model):
    for literal in clause:
        if literal[0] == '!':
            if literal[1:] in model:
                return True
        else:
            if '!' + literal in model:
                return True
    return False

def is_satisfiable(kb):
    model = {}

    while True:
        is_kb_satisfied = True

        for clause in kb:
            if not is_clause_satisfied(clause, model):
                is_kb_satisfied = False
                for literal in clause:
                    if literal not in model and '!' + literal not in model:
                        model[literal] = True
                        break

        if is_kb_satisfied:
            return "Yes"

        for literal in model:
            if literal[0] == '!':
                if literal[1:] in model:
                    return "No"
            else:
                if '!' + literal in model:
                    return "No"

def main():
    if len(sys.argv) < 2:
        print("Usage: python fol_resolution.py <cnf_file>")
        return

    filename = sys.argv[1]
    with open(filename) as f:
        # Parse the predicates, variables, constants, and functions used in the knowledge base
        # (Not implemented in this example)

        # Parse the clauses in the knowledge base
        kb = []
        for line in f:
            if not line.startswith("Predicates:") and not line.startswith("Variables:") and not line.startswith("Constants:") and not line.startswith("Functions:"):
                literals = line.strip().split()
                kb.append(literals)

    result = is_satisfiable(kb)
    print(result)

if __name__ == "__main__":
    main()
