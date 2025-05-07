"""
Escape characters in Python are special characters preceded by a backslash ('\') and used to 
represent characters that cannot neccesarily be type directly. Escape characters are used for 
things like including special characters in strings, and to format output.
"""

# Common Escape Characters:


#           Escape              Meaning:
#           Character:
#          -----------        ---------------
           
#              \\                Backslash

#              \'                Single quote

#              \"                Double quote

#              \n                Newline

#              \r                Carriage return

#              \t                Tab

#              \b                Backspace

#              \f                Form feed

#              \ooo              Octal value

#              \xhh              Hexadecimal value

print()

# escaping the backslash character:
print("File path: C:\\\\python_files\\\\python_file.py")
print()

# escaping single quotes:
print('Carbone\'s a python developer!')
print()

# escaping double quotes:
print("Carbone says \"Howdy!\"")
print()

# escaping the newline character:
print("This is the first line\nThis is the second 'newline'")
print()

# escaping the carriage return character:
print("Hello\rJ")  # '\r' moves the cursor to the beginning of the current line without advancing to the next line.
print()

# escaping the tab character:
print("First Name\tMI\tLast Name\tUsername")
print()

# escaping the backspace character:
print("Bo\bones")
print()

# escaping the form feed character:
print("Page One\fPage Two\fPage Three")
print()

# escaping octal value characters:
print("\103\141\162\142\157\156\145")
print()

# escaping hex value characters:
print("\x48\x61\x6d\x6d\x65\x72\x73\x63\x68\x6c\x61\x67\x65\x72")
print()

print("Until next timme developer!")
print()