# using a title method to capitalize a string
name = "john smith"
upper_case_name = name.upper()
print(upper_case_name)             # JOHN SMITH
lower_case_name = upper_case_name.lower()
print(lower_case_name)     # john smith

print(f'id name : {id(name)}')
print(f'id lower_case_name : {id(lower_case_name)}')
print(f'id upper_case_name : {id(upper_case_name)}')


