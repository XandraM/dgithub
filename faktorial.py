# input for number
n = int(input('enter a number: '))

# define factorial
f = 1
i = 1

# loop
while i <= n:
    f = f * i
    i = i + 1

# print the result
print('Factorial of the number', n, 'is number', f, '.')
