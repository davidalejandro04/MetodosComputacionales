"""
File I/O and Text Parsing in Python
======================================
Demonstrates reading a text file line by line, extracting
structured fields (name, date, location, message) using
string methods like rstrip() and split().

Usage:
    Requires 'contacto_de_JaimeForero.txt' in the working
    directory. Run fetch_contact_data.sh to download it.
"""

# ── 1. Open and Read the File ───────────────────────────────────────────────
infile = open('contacto_de_JaimeForero.txt', 'r')
text   = infile.readlines()   # returns list of lines (including '\n')

# Raw fields (still contain newline characters)
name    = text[0]
date    = text[1]
place   = text[2]
message = text[3]

print("=== Raw lines (with newline characters) ===")
print(name)
print(date)
print(place)
print(message)

# ── 2. Clean and Parse the Fields ───────────────────────────────────────────
name    = text[0].rstrip('\n')       # strip trailing newline → plain string
date    = text[1].split()            # split on whitespace → list of tokens
place   = text[2].split(',')         # split on comma → list of parts
message = text[3].rstrip('\n')

print("=== Parsed fields ===")
print("Name:   ", name)
print("Date:   ", date)
print("Place:  ", place)
print("Message:", message)

infile.close()
