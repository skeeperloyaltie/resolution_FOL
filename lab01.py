import sys
import copy
import re


def read_cnf_file(file_path):
    """Reads the CNF file and returns a list of clauses."""
    with open(file_path, "r") as f:
        lines = f.readlines()
    clauses = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        literals = re.split("\s+", line)
        clauses.append(literals)
    return clauses


def resolve(clause1, clause2):
    new_clause = []
    for literal1 in clause1:
        for literal2 in clause2:
            if literal1 == literal2 or literal1 == f"!{literal2}" or f"!{literal1}" == literal2:
                new_clause.extend(
                    [literal for literal in clause1 + clause2 if literal != literal1 and literal != literal2])
                new_clause = list(set(new_clause))
                if not new_clause:
                    new_clause.append('')  # placeholder for an empty clause
                return new_clause
    return None


def resolve_all(clauses_):
    new_clauses = copy.deepcopy(clauses_)
    while True:
        n = len(new_clauses)
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        new_clauses = [clause for clause in new_clauses if clause]  # remove any empty clauses
        for i, j in pairs:
            resolvers = resolve(new_clauses[i], new_clauses[j])
            if resolvers is not None:
                if "" in resolvers:  # contradiction found
                    return "no"
                new_clauses.append(resolvers)
        if new_clauses == clauses_:
            return "yes"
        clauses_ = copy.deepcopy(new_clauses)

        clauses_ = new_clauses


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python resolution.py <cnf_file>")
        sys.exit(1)
    cnf_file = sys.argv[1]
    clauses = read_cnf_file(cnf_file)
    result = resolve_all(clauses)
    print(result)
