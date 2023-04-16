def read_input(): input_type = input() # Check for input type - "I" or "F"

if "I" in input_type: # If input type is "I"
    first_pattern = input().strip() # Input the first line which contains pattern
    second_text = input().strip() # Input the second line which contains text
    return (first_pattern, second_text) # Return both lines

if "F" in input_type: # If input type is "F"
    with open("tests/06") as file: # Open the file "tests/06" and save as file
        first_line = file.readline().strip()   # Read the first line which contains pattern
        second_line = file.readline().strip()  # Read the second line which contains text
    return (first_line, second_line) # Return both lines
def print_occurrences(output): # This function controls the output, it doesn't need to return anything print(' '.join(map(str, output)))

def get_occurrences(pattern, text): # This function finds the occurrences using Rabin-Karp algorithm p = len(pattern) t = len(text)

occurrences = []

ph = hash(pattern) # Calculate the hash of the pattern
th = hash(text[:p]) # Calculate the hash of the first substring of the text

for i in range(t-p+1):
    if ph == th and text[i:i+p] == pattern: # If the hashes match and the substring equals the pattern
        occurrences.append(i) # Add the index of the substring to the list of occurrences

    if i < t-p: # If there are more substrings to check
        th = hash(text[i+1:i+p+1]) # Calculate the hash of the next substring

# Return an iterable variable
return occurrences

if name == 'main': print_occurrences(get_occurrences(*read_input()))