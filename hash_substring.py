# python3

def read_input():
    # this function acquires input from both keyboard and file
    # use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    input_type = input().rstrip().lower()
    if input_type == 'i':
        # read input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'f':
        # read input from file
        filename = input().rstrip()
        with open(filename, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        raise ValueError("Invalid input type specified. Must be 'i' or 'f'.")
    
    # return both lines in one return
    return pattern, text

def print_occurrences(output):
    # this function controls output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function finds the occurrences using Rabin-Karp algorithm
    
    # calculate the hash of the pattern
    pattern_hash = sum(ord(pattern[i]) * pow(26, len(pattern)-i-1) for i in range(len(pattern)))
    
    # initialize variables
    text_hash = 0
    output = []
    prime = 101
    
    # calculate the hash of the first substring of the text of the same length as the pattern
    for i in range(len(pattern)):
        text_hash += ord(text[i]) * pow(26, len(pattern)-i-1)
    
    # check if the hash of the first substring of text matches the hash of the pattern
    if text_hash == pattern_hash and text[:len(pattern)] == pattern:
        output.append(0)
    
    # calculate the hash of each subsequent substring of text and check if it matches the hash of the pattern
    for i in range(1, len(text)-len(pattern)+1):
        text_hash = (text_hash - ord(text[i-1]) * pow(26, len(pattern)-1)) * 26 + ord(text[i+len(pattern)-1])
        if text_hash == pattern_hash and text[i:i+len(pattern)] == pattern:
            output.append(i)
    
    # return the list of occurrences
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
