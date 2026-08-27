"""
Problem 4: Basic Operations of Linked Stack
Decimal to r-base number conversion using a Linked Stack
"""


class Node:
    """Node of the linked stack."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """Linked stack implementation."""
    def __init__(self):
        self.top = None  # top pointer (None = empty stack)
        self._size = 0

    def init_stack(self):
        """Initialize an empty linked stack."""
        self.top = None
        self._size = 0

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def push(self, data):
        """Push an element onto the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Pop an element from the stack. Returns the data."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data


# Digit characters for bases up to 36
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert(num, r):
    """
    Convert integer num (decimal) to base-r number string.
    Uses the division-remainder method with a linked stack.
    Handles positive, negative, and zero.
    """
    stack = LinkedStack()
    stack.init_stack()

    if num == 0:
        return "0"

    # Determine sign
    negative = num < 0
    num = abs(num)

    # Division-remainder method: push remainders onto the stack
    while num > 0:
        remainder = num % r
        stack.push(DIGITS[remainder])
        num //= r

    # Pop from stack to get the converted number (most significant digit first)
    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    if negative:
        result.insert(0, '-')

    return "".join(result)


def convert_rational(num, r, precision=10):
    """
    Convert a decimal rational number to base-r.
    Integer part uses division-remainder; fractional part uses multiplication-integer method.
    """
    if num < 0:
        return "-" + convert_rational(-num, r, precision)

    int_part = int(num)
    frac_part = num - int_part

    int_str = convert(int_part, r)

    if frac_part == 0:
        return int_str

    frac_str = []
    count = 0
    while frac_part > 0 and count < precision:
        frac_part *= r
        digit = int(frac_part)
        frac_str.append(DIGITS[digit])
        frac_part -= digit
        count += 1

    return int_str + "." + "".join(frac_str)


def main():
    print("=== Linked Stack: Number Base Conversion ===\n")

    test_cases = [
        (0, 2), (13, 2), (335, 16), (150, 8),
        (-10, 2), (3000, 3), (510, 2), (4324, 16),
    ]

    print(f"{'Decimal':>10} | {'Base':>5} | {'Result':>20}")
    print("-" * 42)
    for num, r in test_cases:
        result = convert(num, r)
        print(f"{num:>10} | {r:>5} | {result:>20}")

    print("\n--- Rational Number Conversion ---")
    rational_cases = [(3.14159, 2), (0.625, 2), (10.5, 8), (255.75, 16)]
    print(f"{'Decimal':>12} | {'Base':>5} | {'Result':>30}")
    print("-" * 54)
    for num, r in rational_cases:
        result = convert_rational(num, r)
        print(f"{num:>12} | {r:>5} | {result:>30}")

    print("\n--- Interactive Mode ---")
    try:
        num = float(input("Enter a decimal number: "))
        r = int(input("Enter target base (2-36): "))
        if r < 2 or r > 36:
            print("Base must be between 2 and 36.")
        elif num == int(num):
            print(f"Result: {convert(int(num), r)}")
        else:
            print(f"Result: {convert_rational(num, r)}")
    except (ValueError, EOFError):
        print("Skipping interactive mode.")


if __name__ == "__main__":
    main()
