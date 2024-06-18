# converting a string into a list of words
s = "These words are separated by spaces."
l = s.split(" ")
print(l)
my_tuple = tuple(l)
print(my_tuple)

for el in l:
    print(el)


print("--------------")

for el in l:
    for i in el:
        print(i, end=" ")
    print("----")
    print("----")

print("-----")    
