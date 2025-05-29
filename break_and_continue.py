# This code snippet is a while loop in Python that will continuously print the value of `n` starting
# from 0 and incrementing it by 1 in each iteration. The loop will continue indefinitely (`while
# True:`) until the value of `n` exceeds 5. Once `n` becomes greater than 5, the `break` statement is
# executed, which will exit the loop.
# for n in range(4):
#     if n == 2:
#         print("there goes 2")
#         continue
#     print(n)


# This code snippet initializes a variable `n` with a value of 0 and enters an infinite loop using
# `while True:`. Within each iteration of the loop, the current value of `n` is printed. If the value
# of `n` exceeds 5, the `break` statement is executed, which exits the loop.
# n = 0
# while True:
#     print(n)
#     if n > 5:
#       break
#     n += 1

# This code snippet initializes a variable `n` with a value of 0 and enters an infinite loop using
# `while True:`. Within each iteration of the loop, the current value of `n` is printed. If the value
# of `n` is less than 5, it is incremented by 1 and the loop continues to the next iteration using
# `continue`. Once `n` becomes greater than or equal to 5, a message "n is greater than or equal to 5,
# exiting loop." is printed, and the loop is exited using the `break` statement.
n = 0
while True:
    print(n)
    if n < 5:
        n = n + 1
        continue
    else:
        print("n is greater than or equal to 5, exiting loop.")
        break

