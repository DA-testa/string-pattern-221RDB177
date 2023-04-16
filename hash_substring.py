def read_input():
    # This function acquires input both from keyboard and file
    # As before, use capital 'I' (input from keyboard) and capital 'F' (input from file) to choose which input type will follow
    input_type = input().strip()
    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "F":
        with open("tests/06", mode='r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    # Read the two lines (pattern and text) after input type choice
    # and return both lines in one return
    return pattern, text

def print_occurrences(occurrences):
    # Control the output and print the occurrences
    print(' '.join(map(str, occurrences)))

def find_occurrences(pattern, text):
    q = 256
    b = 13
    pattern_hash = 0
    text_hash = 0
    occurrences = []
    
    # Find the occurrences using the Rabin Karp algorithm
    pattern_len = len(pattern)
    text_len = len(text)
    for i in range(pattern_len):
        pattern_hash = (pattern_hash * q + ord(pattern[i])) % b
        text_hash = (text_hash * q + ord(text[i])) % b
        
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pattern_len]:
                occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = (q * (text_hash - ord(text[i]) * pow(q, pattern_len - 1, b)) + ord(text[i+pattern_len])) % b
            if text_hash < 0:
                text_hash += b
    
    # Return the occurrences as an iterable variable
    return occurrences

# Launch the functions
if __name__ == '__main__':
    text_pattern_occurrences = read_input()
    occurrences = find_occurrences(*text_pattern_occurrences)
    print_occurrences(occurrences)
