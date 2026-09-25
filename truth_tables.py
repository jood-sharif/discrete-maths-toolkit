# Import logical operators
from logic import logical_not
from logic import logical_and
from logic import logical_or
from logic import implies
from logic import iff


def not_a_truth_table():
    # handles unary operation NOT
    
    values = [True, False]

    print(f"{'A':<7}{'not A':<7}")
    for a in values:
        print(f"{str(a):<7}{str(logical_not(a)):<7}")

    print()


def truth_table(operation, heading):
    # handles binary operations like AND, OR, →, ↔
    
    values = [True, False]

    print(f"{'A':<7}{'B':<7}{heading:<7}")

    for a in values:
        for b in values:
            print(f"{str(a):<7}{str(b):<7}{str(operation(a,b)):<7}")

    print()


#Print truth tables
not_a_truth_table()
truth_table(logical_and, "A ∧ B")
truth_table(logical_or, "A ∨ B")
truth_table(implies, "A → B")
truth_table(iff, "A ↔ B")
