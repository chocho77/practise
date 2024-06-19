width = 60
print("*" * width)
header = "Coding Temple, Inc"
intervals = (width - len(header)) // 2
print(header.center(width))
print(' ' * (intervals - 1), "283 Franklin St.")
print(' ' * (intervals - 1), "Boston, MA")
print("=" * width)
product = "Product Name"
price = "Product Price"
print(product.rjust(26), price.rjust(14))
print("Books".rjust(19), "$49.95".rjust(15))
print("Computer".rjust(22), "$579.99".rjust(13))
print("Monitor".rjust(21), "$124.89".rjust(14))
print("=" * width)
print("Total".rjust(34))
print("$754.83".rjust(36))
print("=" * width)
bye = "Thanks for shopping with us today!"
intervals_bye = (width - len(bye))
print(" " * (intervals_bye - 1), bye)
print("*" * width)
