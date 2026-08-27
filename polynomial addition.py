"""
Problem 1: Application of Singly Linked List
Polynomial Addition using Singly Linked List
"""

class Node:
    """Node of the singly linked list for polynomial terms."""
    def __init__(self, coef=0, exp=0):
        self.coef = coef   # coefficient
        self.exp = exp     # exponent
        self.next = None


class LinkedList:
    """Singly linked list with a dummy head node."""
    def __init__(self):
        self.head = self._init()

    def _init(self):
        """Initialize an empty linked list with a dummy head node."""
        head = Node()
        head.next = None
        return head

    def create_from_tail(self, terms):
        """
        Create a linked list via tail insertion method.
        terms: list of (coef, exp) tuples, sorted by exponent ascending.
        """
        tail = self.head
        for coef, exp in terms:
            new_node = Node(coef, exp)
            tail.next = new_node
            tail = new_node

    def print_poly(self):
        """Print the polynomial in a readable format."""
        p = self.head.next
        if p is None:
            print("0")
            return
        terms = []
        while p:
            if p.coef != 0:
                if p.exp == 0:
                    terms.append(f"{p.coef}")
                elif p.exp == 1:
                    terms.append(f"{p.coef}x")
                else:
                    terms.append(f"{p.coef}x^{p.exp}")
            p = p.next
        if not terms:
            print("0")
        else:
            # Print from highest exponent to lowest
            print(" + ".join(reversed(terms)).replace("+ -", "- "))


def polyadd(LA, LB):
    """
    Add two polynomials stored in LA and LB.
    The result is stored in LA. No new memory is allocated.
    Returns LA (the result list).
    """
    # prev points to the node before LA1 in LA
    prev = LA.head
    LA1 = LA.head.next
    LB1 = LB.head.next

    while LA1 is not None and LB1 is not None:
        if LA1.exp < LB1.exp:
            # Keep LA1 node in result; advance LA1
            prev = LA1
            LA1 = LA1.next
        elif LA1.exp == LB1.exp:
            # Add coefficients
            s = LA1.coef + LB1.coef
            lb_next = LB1.next
            if s == 0:
                # Remove both nodes
                prev.next = LA1.next
                # Free LA1 (Python GC handles this)
                LA1 = prev.next
            else:
                # Update LA1 coefficient, free LB1
                LA1.coef = s
                prev = LA1
                LA1 = LA1.next
            LB1 = lb_next
        else:  # LA1.exp > LB1.exp
            # Insert LB1 node before LA1
            lb_next = LB1.next
            LB1.next = LA1
            prev.next = LB1
            prev = LB1
            LB1 = lb_next

    # Append remaining LB nodes
    if LB1 is not None:
        prev.next = LB1

    return LA


def main():
    # Example: P(x) = 5x^3 + 2x + 1  (stored as ascending exponent)
    LA = LinkedList()
    LA.create_from_tail([(1, 0), (2, 1), (5, 3)])  # 1 + 2x + 5x^3

    # Q(x) = 3x^3 + x^2 - 2x - 3
    LB = LinkedList()
    LB.create_from_tail([(-3, 0), (-2, 1), (1, 2), (3, 3)])

    print("P(x) = ", end="")
    LA.print_poly()
    print("Q(x) = ", end="")
    LB.print_poly()

    result = polyadd(LA, LB)
    print("P(x) + Q(x) = ", end="")
    result.print_poly()

    # Second test
    print("\n--- Additional Test ---")
    LA2 = LinkedList()
    LA2.create_from_tail([(3, 0), (0, 1), (2, 2)])  # 3 + 2x^2
    LB2 = LinkedList()
    LB2.create_from_tail([(-3, 0), (5, 1), (-2, 2), (4, 3)])  # -3 + 5x - 2x^2 + 4x^3
    print("P(x) = ", end="")
    LA2.print_poly()
    print("Q(x) = ", end="")
    LB2.print_poly()
    result2 = polyadd(LA2, LB2)
    print("P(x) + Q(x) = ", end="")
    result2.print_poly()


if __name__ == "__main__":
    main()
