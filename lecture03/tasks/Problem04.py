# school = "Vasil Drumev"

# .title()
#.upper() .lower()
# .replace()
# .find()
# .strip()
# .split()
# startswith()
# endswith()

school = "   vasil drumev   "
school_title = school.title()
print(school_title)
school_upper = school.upper()
print(school_upper)
school_lower = school.lower()
print(school_lower)
school_replace = school.replace("drumev", "drumev!")
print(school_replace)
school_find = school.find("drumev")
print(school_find)
school_strip = school.strip()
print(school_strip)
school_split = school.split(" ")
print(school_split)
school_starts_with  =school.startswith("")
print(school_starts_with)
school_ends_width = school.endswith("")
print(school_ends_width)
