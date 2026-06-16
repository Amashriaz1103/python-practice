# Prime number

num = 13

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")


# Factorial

    num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)