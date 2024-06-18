# format(*args, **kwargs) -> str

# S.format(*args, **kwargs)-> str
# Return formatted version of S, using subsitutions args and kwargs. The
# substitutions are identified by braces ('{' and '}')

# injecting variables using the format method
name = "John"
print("Hello {}.".format(name)) # Hello John
# Hello John, you are 28 years old!
print("Hello {}, you are {} years old!".format(name, 28))
