x = 5
y = 2
print(f'x = {x}, y = {y}')
if x > y:
    x, y = y, x
    print(f'x = {x}, y = {y}')
else:
    print(f'x = {x}, y = {y}')

