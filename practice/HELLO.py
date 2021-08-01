# Reading files in python

# Reading the number of lines
fhand = open("practice/mbox.txt")
count = 0

for line in fhand:
    count += 1
print(f"Line Count {count}")

# Read the whole file

fhand = open("practice/mbox-short.txt")
inp = fhand.read()
print(len(inp))

print(inp[0:20])

# Searching through the file
fhand = open("practice/mbox-short.txt")
for line in fhand:
    line = line.strip()
    if line.startswith("From:"):
        print(line)

##Skipping with Continue
fhand = open("practice/mbox-short.txt")
for line in fhand:
    line = line.strip()
    if not line.startswith("From: "):
        continue
    print(line)
