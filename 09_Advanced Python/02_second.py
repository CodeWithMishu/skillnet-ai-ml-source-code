# def count_of(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# num = count_of(5)
# print(next(num))  # prints 1


import threading
def task():
    print(":running in a thread")
thread = threading.Thread(target=task)
thread.start()