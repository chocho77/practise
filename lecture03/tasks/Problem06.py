filename = "hello.py"
if(filename.endswith('.java')):
    print("Yes.")
else:
    print("No.")

find_index_py = filename.find("py")
print(find_index_py)

word_check = filename.startswith('word')

if word_check:
    print('Yes')
else:
    print('No')

