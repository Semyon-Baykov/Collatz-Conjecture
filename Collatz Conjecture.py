num = int(input("\n\nPick an integer: "))
iteration = 0

show_the_math = input("(y) Show calculations? ")
if show_the_math == "y":
    show_the_math = True
else:
    show_the_math = False

print("")

# Algorithm
while not num == 1:

    iteration += 1

    if num % 2 == 0:

        if show_the_math:
            print(str(int(num)) + " is even, diving by two: " + str(int(num/2)))

        num /= 2

    else:

        if show_the_math:
            print(str(int(num)) + " is odd, multiplying by three and adding one: " + str(int((3 * num) + 1)))

        num = (3 * num) + 1


# Output
print("\n" + str(iteration) + " iterations before getting to 1 and establishing the loop")