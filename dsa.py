#arrays

A = [1,2,3]

#add element at the end of the array - o(1)

A.append(4)

print(A)

# remove element from the end of the array - o(1)

A.pop()

print(A)

# add element at any position in the array - o(n)

A.insert(2 , 4)

print(A)

# modify an element at any position - o(1)

A[0] = 7
print(A)

# Accessing an element - o(1)

print(A[2])

# checking if an element is present in an array

if 7 in A:
    print(True)
else:
    print(False)


# string

s = "heelloo"

# append at the end

add = s + 'z'

print(add)

# length

print(len(s))

#accessing an element

print(s[2])