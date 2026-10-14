def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer:
# it prints 3 and then 4. The for loop goes through 1, 2, 3 one at a time. the if checks number > 1, so 1 is skipped. only 2 and 3 are passed to add_one, which returns 3 and 4, and print shows them.


# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:
# it returns 3. return gives the value back to the code that called the function, so it can be stored or used, but it does not show anything on screen. print only displays a value on the screen. In the loop, add_one returns the number and print is what makes it visible in the output.
