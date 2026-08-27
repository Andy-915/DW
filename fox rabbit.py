"""
Problem 3: The Fox Catching Rabbit Problem
Sequential List Implementation
"""


class SeqList:
    """Sequential list (array-based) to represent the 10 holes."""
    def __init__(self, size):
        self.elem = [0] * size
        self.length = size

    def init_list(self):
        """Initialize all holes with flag = 1 (not yet checked)."""
        for i in range(self.length):
            self.elem[i] = 1


def rabbit(L):
    """
    Simulate the fox checking holes 1000 times.
    Holes are numbered 1..10, stored at indices 0..9.
    The fox checks hole 1 first (index 0), then skips 1, 2, 3, ... holes.
    """
    L.init_list()

    current = 0        # index of current hole (0-based), starts at hole 1
    total_checks = 1000

    for i in range(total_checks):
        L.elem[current] = 0          # Mark this hole as checked
        current = (current + i) % L.length  # Move to next hole

    # Output holes that were never checked
    safe_holes = []
    for i in range(L.length):
        if L.elem[i] == 1:
            safe_holes.append(i + 1)  # Convert to 1-based hole number

    return safe_holes


def main():
    print("=== Fox Catching Rabbit Problem ===\n")
    print("10 holes are arranged in a circle.")
    print("The fox checks 1000 times with increasing skip counts.")
    print("Holes not checked are safe for the rabbit.\n")

    L = SeqList(10)
    safe = rabbit(L)

    print("Flag status of each hole after 1000 checks:")
    print(f"{'Hole':>6} | {'Flag':>6}")
    print("-" * 16)
    for i in range(L.length):
        status = "Safe ✓" if L.elem[i] == 1 else "Checked"
        print(f"{i+1:>6} | {L.elem[i]:>6}  ({status})")

    if safe:
        print(f"\nThe rabbit can safely hide in hole(s): {safe}")
    else:
        print("\nAll holes were checked! The rabbit has no safe hole.")


if __name__ == "__main__":
    main()
