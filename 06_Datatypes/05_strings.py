#ordered immutable

multiline_string = """Hello
Word
"""
print(f"multiline_string {multiline_string}")

multiline_string_no_new_line = """Hello \
Word
"""
print(f"multiline_string {multiline_string_no_new_line}")

string_hello_world = "Hello World"
substring = string_hello_world[:6]
reversed_my_string = string_hello_world[::-1]
print(f"substring: {substring}")
print(f"reversed_my_string: {reversed_my_string}")

whitespace_string = "          text         "
print(f"\nwhitespace_string: {whitespace_string}")
nospace = whitespace_string.strip()
print(f"nospace = whitespace_string.strip(): {nospace}")


print(f"""\nstring_hello_world.startswith("Hello"): {string_hello_world.startswith("Hello")}""")
print(f"""string_hello_world.endswith("ld"): {string_hello_world.endswith("ld")}""")

print(f"""\nstring_hello_world.find("l") # first_index: {string_hello_world.find("l")}""")
print(f"""string_hello_world.count("l") : {string_hello_world.count("l")}""")

print(f"""string_hello_world.replace("World", "Universe") # returns a new string : {string_hello_world.replace("World", "Universe")}""")

mystring = "this is a sample text"
mylist = mystring.split()

print(f"""\nmylist = "{mystring}".split(): {mylist}""")


print(f"""" ".join(mylist)".split(): {" ".join(mylist)}""")