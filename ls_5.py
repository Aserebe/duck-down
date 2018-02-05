a,b,c=2,3,4
if(a|b|c>0):
    print("true")
else:
    print("false")
    
d=e=z=10
s=d*e-z
print(s)

my_tuple=(9,8,0)
print(my_tuple[1])
# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('same', 'same', 'same')
print(("same",) * 3)


dict={"name": "serene","sem": 2,"branch": "cs"}
print(dict["name"])


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A | B)
print(A-B)
print(A&B)

c = 5 + 3j
print(c + 3)
