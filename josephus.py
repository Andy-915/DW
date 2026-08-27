"""
Problem 2: Josephus Problem
Circular Singly Linked List (no header node)
"""


class Node:
    """Node in a circular singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


def create_clist(n):
    """
    Create a circular singly linked list without a header node.
    Returns the head pointer (clist) and global joseph pointer.
    """
    if n <= 0:
        return None, None
    head = Node(1)
    tail = head
    for i in range(2, n + 1):
        new_node = Node(i)
        tail.next = new_node
        tail = new_node
    tail.next = head  # Make it circular
    clist = head
    joseph = head
    return clist, joseph


def josephus(n, m, k):
    """
    Solve the Josephus problem.
    n: total number of people
    m: starting position (1-indexed)
    k: count-off number
    Returns the dequeue sequence.
    """
    clist, p = create_clist(n)
    if clist is None:
        return []

    # Advance to the m-th node (start counting from position m)
    for _ in range(m - 1):
        p = p.next

    dequeue_seq = []

    while p is not None:
        # Count k-1 steps forward (p will be at the (k-1)-th node)
        for _ in range(k - 1):
            p = p.next

        q = p.next  # q is the k-th node (person who steps out)
        dequeue_seq.append(q.data)

        if p.next == p:
            # Only one node left
            p = None  # Signal loop end
        else:
            # Remove q
            p.next = q.next
            p = p.next  # Move p forward for next round

    clist = None
    return dequeue_seq


def main():
    print("=== Josephus Problem ===\n")

    # Test 1: n=7, m=1, k=3
    n, m, k = 7, 1, 3
    result = josephus(n, m, k)
    print(f"n={n}, m={m}, k={k}")
    print(f"Dequeue sequence: {result}\n")

    # Test 2: n=5, m=1, k=2
    n, m, k = 5, 1, 2
    result = josephus(n, m, k)
    print(f"n={n}, m={m}, k={k}")
    print(f"Dequeue sequence: {result}\n")

    # Test 3: n=6, m=2, k=4
    n, m, k = 6, 2, 4
    result = josephus(n, m, k)
    print(f"n={n}, m={m}, k={k}")
    print(f"Dequeue sequence: {result}\n")

    # Interactive mode
    print("--- Interactive Mode ---")
    try:
        n = int(input("Enter number of people (n): "))
        m = int(input("Enter starting position (m): "))
        k = int(input("Enter count-off number (k): "))
        result = josephus(n, m, k)
        print(f"Dequeue sequence: {result}")
    except (ValueError, EOFError):
        print("Skipping interactive mode.")


if __name__ == "__main__":
    main()
