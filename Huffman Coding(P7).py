"""
Problem 7: Huffman Coding and File Compression Simulation
"""
import heapq
from collections import Counter


# Binary Tree Node 
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char      # Character (None for internal nodes)
        self.freq = freq      # Frequency
        self.left = None
        self.right = None
        self.code = ""        # Huffman code (filled after generation)

    # For min-heap ordering by frequency, then by char for stability
    def __lt__(self, other):
        if self.freq == other.freq:
            # Smaller char (or None last) goes left
            if self.char is None and other.char is None:
                return False
            if self.char is None:
                return False
            if other.char is None:
                return True
            return self.char < other.char
        return self.freq < other.freq

# (1) Count Frequencies 
def count_freq(text):
    return dict(Counter(text))

# (2) Build Huffman Tree 
def build_huffman_tree(freq_map):
    heap = []
    for char, freq in freq_map.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    if len(heap) == 1:
        # Edge case: only one distinct character
        node = heapq.heappop(heap)
        root = HuffmanNode(None, node.freq)
        root.left = node
        return root

    while len(heap) > 1:
        # Extract two trees with smallest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Create new internal node
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman tree

# (3) Generate Codes 
def generate_codes(root):
    codes = {}

    def _traverse(node, current_code):
        if node is None:
            return
        if node.char is not None:
            # Leaf node
            codes[node.char] = current_code if current_code else "0"
            return
        _traverse(node.left, current_code + "0")
        _traverse(node.right, current_code + "1")

    _traverse(root, "")
    return codes

# (4) Encode 
def encode(text, codes):
    return "".join(codes[ch] for ch in text)

# (5) Decode 
def decode(binary_str, root):
    result = []
    node = root
    for bit in binary_str:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            result.append(node.char)
            node = root  # Return to root
    return "".join(result)

# Main 
def huffman_compress(text):
    print(f"Original text: '{text}'")
    print(f"Text length:   {len(text)} characters\n")

    # 1. Count frequencies
    freq_map = count_freq(text)
    print("Character frequencies:")
    for ch in sorted(freq_map.keys()):
        display = repr(ch) if ch == ' ' else ch
        print(f"  '{display}': {freq_map[ch]}")

    # 2. Build Huffman tree
    root = build_huffman_tree(freq_map)

    # 3. Generate codes
    codes = generate_codes(root)
    print("\nHuffman codes (sorted by character):")
    for ch in sorted(codes.keys()):
        display = ' ' if ch == ' ' else ch
        print(f"  {display}:{codes[ch]}")

    # 4. Encode
    binary_str = encode(text, codes)
    print(f"\nEncoded binary string: {binary_str}")
    print(f"Encoded length: {len(binary_str)} bits")
    print(f"Original size:  {len(text) * 8} bits (ASCII)")
    ratio = len(binary_str) / (len(text) * 8) * 100
    print(f"Compression ratio: {ratio:.1f}%")

    # 5. Decode
    decoded = decode(binary_str, root)
    print(f"\nDecoded text: '{decoded}'")
    print(f"Lossless: {decoded == text}")

    return codes, binary_str, decoded

def main():
    print("=== Huffman Coding and File Compression Simulation ===\n")

    # Sample from the problem statement
    print("─" * 55)
    print("Test 1: Sample Input from Problem Statement")
    print("─" * 55)
    n = 7
    text1 = "abc abc"
    print(f"n = {n}")
    huffman_compress(text1)

    # Second test
    print("\n" + "─" * 55)
    print("Test 2: Longer Text")
    print("─" * 55)
    text2 = "hello huffman coding"
    huffman_compress(text2)

    # Third test
    print("\n" + "─" * 55)
    print("Test 3: Repetitive Text")
    print("─" * 55)
    text3 = "aaaaabbbccddddde"
    huffman_compress(text3)

    # Interactive
    print("\n" + "─" * 55)
    print("Interactive Mode")
    print("─" * 55)
    try:
        n = int(input("Enter n (number of characters): "))
        text = input("Enter text: ")
        if len(text) != n:
            print(f"Warning: entered text length {len(text)} != {n}. Using actual text.")
        huffman_compress(text)
    except (ValueError, EOFError):
        print("Skipping interactive mode.")

if __name__ == "__main__":
    main()
