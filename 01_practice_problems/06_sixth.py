# Important question 
# Input_string="aaabbbcccdddee"
# Expected output = 
# a= 3 
# B=3
# C=3 
# D=3 
# E=2

Input_string = "aaabbbcccdddee"
char_count = {}  # Keep this as dictionary, don't overwrite with 0

for char in Input_string:
    print(char)  # Print the character being processed
    
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"{char}= {count}")