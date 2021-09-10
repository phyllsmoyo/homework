import os

# Questions 1
filename = input("What is the filename: ")
# if the file name is empty or is not a text then exit the program
if filename == "" or not filename.endswith(".txt"):
    print("Invalid filename.")
    exit(0)
else:
    # Open a file for writing and create it if it does not exist
    f = open(filename, "w")


# Question 2
# if the file name is empty or is not a text then exit the program
filename = input("What is the filename: ")
if filename == "" or not filename.endswith(".txt"):
    print("Invalid filename.")
    exit(0)
else:
    # Open a file for writing and create it if it does not exist
    f = open(filename, "w+")

    f.write("id,enroll_year,name,stream,student,faculty,source_file_path")
