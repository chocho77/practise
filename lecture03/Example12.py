# removing white space with strip
something = " something !"
name = "     john     "
full_name = name + something
print(full_name)
name1 = name.strip()
full_name = name1 + something
print(full_name)
name2 = name.lstrip()
full_name = name2 + something
print(full_name)
name3 = name.rstrip()
full_name = name3 + something
print(full_name)

