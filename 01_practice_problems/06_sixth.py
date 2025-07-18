# Important question 
# Input_string="aaabbbcccdddee"
# Expected output = 
# a= 3 
# B=3
# C=3 
# D=3 
# E=2

# khud solve kiya gya 
Input_string = "aaabbbcccdddee"
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_e = 0
for char in Input_string:
    if char=="a":
        count_a +=1
    elif char=="b":
        count_b +=1
    elif char=="c":
        count_c +=1
    elif char=="d":
        count_d +=1
    elif char=="e":
        count_e += 1
    else:
        pass
print(f" The no. of a is : {count_a} \n The no. of b is : {count_b} \n The no. of c is : {count_c} \n The no. of d is : {count_d} \n The no. of e is : {count_e} \n Badi mehnat lagi par kar hi diya ! ")


# Ai dwara diya gya 
# char_count = 0
# for char in Input_string:
#     print(char)
#     char_upper = char.upper()  # Convert to uppercase for consistent output
#     if char_upper in char_count:
#         char_count[char_upper] += 1
#     else:
#         char_count[char_upper] = 1

# for char, count in char_count.items():
#     print(f"{char}= {count}")