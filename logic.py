# Logical connectives

def logical_not(a):
    """Return the truth value of ¬a."""
    return not a

def logical_and(a, b):
    """Return the truth value of a ∧ b."""
    return a and b

def logical_or(a, b):
    """Return the truth value of a ∨ b."""
    return a or b

def implies(a, b):
    """Return the truth value of a → b."""
    return (not a) or b

def iff(a, b):
    """Return the truth value of a ↔ b."""
    return a == b
