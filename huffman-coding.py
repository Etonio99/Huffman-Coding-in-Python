codes = {}

def start_huffman_coding():
    global codes
    codes = {}

    text = input("Enter text to apply Huffman Coding to: ")
    root_node = create_nodes(text)
    assign_character_codes(root_node)

    encoded_text = "".join([codes[character] for character in text])
    print("Encoded text: ", encoded_text)
    decoded_text = decode_huffman_coded_text(encoded_text)
    print("Decoded text: ", decoded_text)

def decode_huffman_coded_text(encoded_text):
    reversed_codes = {value: key for key, value in codes.items()}

    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ""

    return decoded_text

def assign_character_codes(condensed_node):
    explore_node(condensed_node, "")
    print(codes)

def explore_node(node, code):
    if node is None:
        return
    if node.character is not None:
        codes[node.character] = code
        return
    
    explore_node(node.left_node, code + "0")
    explore_node(node.right_node, code + "1")

def create_nodes(text):
    nodes = [Node(character, frequency) for character, frequency in get_frequencies(text).items()]
    print(nodes)

    while len(nodes) > 1:
        nodes.sort()
        left_node, right_node = nodes.pop(0), nodes.pop(0)
        parent_node = Node(None, left_node.frequency + right_node.frequency, left_node, right_node)
        nodes.append(parent_node)

    return nodes[0]
    
def get_frequencies(text):
    frequencies = {}
    for character in text:
        if character not in frequencies:
            frequencies[character] = 0
        frequencies[character] += 1
    return frequencies

class Node:
    def __init__(self, character, frequency, left_node = None, right_node = None):
        self.character = character
        self.frequency = frequency
        self.left_node = left_node
        self.right_node = right_node

    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __repr__(self):
        return f"Node({self.character}, {self.frequency})"
    
if __name__ == "__main__":
    start_huffman_coding()