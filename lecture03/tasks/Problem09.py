width = 80
header = "header"
print( "*" * width)
print(header.center(width))
name = "Name"
print(name.rjust(5))
print(name.rjust(13))
print("*" * width)
for i in range(1,35,2):
    print(name.rjust(i * 2))
