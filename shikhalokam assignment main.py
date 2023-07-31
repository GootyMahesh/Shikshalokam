#Assignment1
def find_shortest_substrings(s, x):
    shortest_substrings = []
    for i in range(len(s)):
        for j in range(i + x, len(s)):
            if s[i] == s[j]:
                substring = s[i:j + 1]
                if len(substring) >= x and (not shortest_substrings or len(substring) < len(shortest_substrings[0])):
                    shortest_substrings = [substring]
                elif len(substring) == len(shortest_substrings[0]):
                    shortest_substrings.append(substring)
    return shortest_substrings

def print_shortest_substrings(s, x):
    shortest_substrings = find_shortest_substrings(s, x)
    if shortest_substrings:
        print(" ".join(shortest_substrings))
    else:
        print("not-found")

# Example usage
s = "abccdbacca"

x = 3
print("x =", x)
print_shortest_substrings(s, x)

x = 4
print("\nx =", x)
print_shortest_substrings(s, x)

x = 5
print("\nx =", x)
print_shortest_substrings(s, x)

x = 6
print("\nx =", x)
print_shortest_substrings(s, x)

x = 7
print("\nx =", x)
print_shortest_substrings(s, x)

x = 8
print("\nx =", x)
print_shortest_substrings(s, x)

#Assignment2
def modify_string(s):
    new_string = []
    changed_chars = set()

    for i, char in enumerate(s):
        ascii_val = ord(char)

        if i not in changed_chars:
            if ascii_val % 2 == 0:
                next_ascii_val = (ascii_val + (ascii_val % 7)) % 128
                new_char = chr(next_ascii_val)
                new_string.append(new_char)
                if i + 1 < len(s):
                    changed_chars.add(i + 1)
            else:
                prev_ascii_val = (ascii_val - (ascii_val % 5)) % 128
                new_char = chr(prev_ascii_val)
                new_string.append(new_char)
                if i - 1 >= 0:
                    changed_chars.add(i - 1)

    return ''.join(new_string)

# Test example
s = "sHQen}"
result = modify_string(s)
print("Final Answer:", result)
