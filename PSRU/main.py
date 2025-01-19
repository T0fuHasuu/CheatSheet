from collections import defaultdict
import heapq
from PIL import Image

# Helper class to define nodes for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman Tree
def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman tree

# Generate Huffman codes from the tree
def generate_huffman_codes(node, prefix='', codes=None):
    if codes is None:
        codes = {}
    
    if node is not None:
        if node.char is not None:
            codes[node.char] = prefix
        generate_huffman_codes(node.left, prefix + '0', codes)
        generate_huffman_codes(node.right, prefix + '1', codes)
    
    return codes

# Process the image and get pixel frequencies
def get_image_frequencies(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    
    # Convert pixels to frequencies
    frequencies = defaultdict(int)
    for pixel in pixels:
        frequencies[pixel] += 1
    
    return frequencies, pixels

# Main function to generate the Huffman code bitstream
def main(image_path, output_file="output.txt"):
    # Step 1: Get frequencies from the image
    frequencies, pixels = get_image_frequencies(image_path)

    # Step 2: Build the Huffman tree based on pixel frequencies
    huffman_tree = build_huffman_tree(frequencies)

    # Step 3: Generate the Huffman codes
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Step 4: Generate the continuous bitstream by appending Huffman codes
    bitstream = ''.join([huffman_codes[pixel] for pixel in pixels])

    # Step 5: Save the bitstream to output.txt
    with open(output_file, "w") as f:
        f.write(bitstream)

    print(f"Bitstream saved to {output_file}")

if __name__ == '__main__':
    # Replace 'your_image.jpg' with the path to your image
    main("AnyPlace-01.jpg")
