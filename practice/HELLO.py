filename = input("What is the filename: ")
if filename == "" or not filename.endswith(".txt"):
    print("Invalid filename.")
    exit(0)
else:
    # Open a file for writing and create it if it does not exist
    f = open(filename, "w+")

    f.write("id,enroll_year,name,stream,student,faculty,source_file_path")
