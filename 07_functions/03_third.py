# def is_palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
# word = input("Enter a word:")
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

import random
def guess_number(secret, attempts=1):
     while True:
             guess=int(input(f"Attempt {attempts}: Guess the number (between 1 and 10): "))
             if guess <secret:
              print("Too low! Try again.")
             return guess_number(secret, attempts + 1)
             elif guess>secret:
             print("Too high! Try again.")
             return guess_number(secret, attempts + 1)
            elif guess==secret:
             print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts.")
            return attempts
            


guess_number(random.randint(1,10))