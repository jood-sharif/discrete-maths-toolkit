# Implication truth table
from logic import implies

def implication_truth_table():

    values = [True, False]

    print(f"{'A':<7}{'B':<7}{'A → B':<7}")

    for a in values:
        for b in values:
            print(f"{str(a):<7}{str(b):<7}{str(implies(a,b)):<7}")

implication_truth_table()

# Biconditional truth table
from logic import iff

def biconditional_truth_table():

    values = [True, False]

    print(f"{'A':<7}{'B':<7}{'A → B':<7}")
    
    for a in values:
        for b in values:
            print(f"{str(a):<7}{str(b):<7}{str(iff(a,b)):<7}")

biconditional_truth_table()
