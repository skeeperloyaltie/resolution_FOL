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


def resolve(c1, c2):
    """Performs the resolution operation on two clauses."""
    resolvents = []
    for literal1 in c1:
        for literal2 in c2:
            if literal1 == "!" + literal2 or literal2 == "!" + literal1:
                # Found complementary literals, so perform the resolution operation
                resolvent = list(set(c1) | set(c2))  # Union of the two clauses
                if literal1 in resolvent:
                    resolvent.remove(literal1)
                if literal2.replace("!", "") in resolvent:
                    resolvent.remove(literal2.replace("!", ""))
                resolvents.append(resolvent)
    return resolvents



def resolve_all(clauses):
    """Applies the resolution rule to all possible pairs of clauses."""
    new_clauses = copy.deepcopy(clauses)
    while True:
        prev_clauses = copy.deepcopy(new_clauses)
        for i in range(len(prev_clauses)):
            for j in range(i+1, len(prev_clauses)):
                resolvents = resolve(prev_clauses[i], prev_clauses[j])
                for resolvent in resolvents:
                    if resolvent not in new_clauses and resolvent not in prev_clauses:
                        new_clauses.append(resolvent)
        if new_clauses == prev_clauses:
            break
    if [] in new_clauses:
        return "no"
    else:
        return "yes"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python resolution.py <cnf_file>")
        sys.exit(1)
    cnf_file = sys.argv[1]
    clauses = read_cnf_file(cnf_file)
    result = resolve_all(clauses)
    print(result)
