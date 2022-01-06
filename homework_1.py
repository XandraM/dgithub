# three arrays for cars
g1 = ["Ford", "BMW", "Lamborghini"]
g2 = ["Mitsubishi", "Fiat", "Jaguar"]
g3 = ["Mazda", "Nissan", "Subaru"]

# make variable
q = " "

# while loop
while q not in g1 and q not in g2 and q not in g3:
    q = input('Enter a car brand: ')
else:
    if q in g1:
        print(q, 'is located in fisrt garage.')
    elif q in g2:
        print(q, 'is located in second garage.')
    elif q in g3:
        print(q, 'is located in third garage.')