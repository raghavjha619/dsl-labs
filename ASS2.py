def intersection(a, b):
    c = []
    for x in a:
        if x in b:
            c.append(x)
    return c

def union(a, b):
    c = a[:]
    for x in b:
        if x not in c:
            c.append(x)
    return c

def difference(a, b):
    c = []
    for x in a:
        if x not in b:
            c.append(x)
    return c

n = int(input("Total number of students: "))
cricket = input("Enter list of students who play cricket: ").split()
badminton = input("Enter list of students who play badminton: ").split()
football = input("Enter list of students who play football: ").split()

print("\nList of students who play both cricket and badminton:", intersection(cricket, badminton))
print("List of students who play either cricket or badminton but not both:", difference(union(cricket, badminton), intersection(cricket, badminton)))
print("Number of students who play neither cricket nor badminton:", n - len(union(cricket, badminton)))
print("Number of students who play cricket & football but not badminton:", len(difference(intersection(cricket, football), badminton)))
print("Number of students who do not play any game:", n - len(union(union(cricket, badminton), football)))
print("List of students who play at least one game:", union(union(cricket, badminton), football))
print("List of students who play all the games:", intersection(intersection(cricket, badminton), football))
