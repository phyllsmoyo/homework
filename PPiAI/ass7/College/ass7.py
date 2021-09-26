import os

# Questions 1
user_file = input("What is the filename: ")
# if the file name is empty or is not a text then exit the program
if user_file == "" or not user_file.endswith(".txt"):
    print("Invalid user_file.")
    exit(0)
else:
    # Open a file for writing and create it if it does not exist
    f = open(user_file, "w")

# Question 2
import os
user_file_name = input('What is the fil name: ')
if user_file_name == "":
    print("File name is empty")
    exit(0)
elif not user_file_name.endswith(".txt"):
    print("File name is invalid")
else:
    f = open(user_file_name,"w+")
    f.write("id,enroll_year,name,stream,student,faculty,source_file_path")
    f.close()


# Question 3
import os
user_file_name = input('What is the fil name: ')
if user_file_name == "":
    print("File name is empty")
    exit(0)
elif not user_file_name.endswith(".txt"):
    print("File name is invalid")
else:
    f = open(user_file_name,"w+")
    f.write("id,enroll_year,name,stream,student,faculty,source_file_path")
    f.close()

path = '/home/phyllsmoyo/Desktop/practice/College'
user_file_root = os.path.dirname(os.path.abspath(user_file_name))
user_file_path = os.path.join(user_file_root, user_file_name)

# Generate the file names in a directory tree by walking the tree
for root, folders, files in os.walk(path):
    # Loop through the list of files
    
    # print(files)
    for file in files:
        # Join the folder path and the name of the file
        # to form a file_path
        file_path = os.path.join(root, file)
        #print(file_path)
        # Check if file path is valid and the file is not empty
        if os.path.isfile(file_path) and (os.path.getsize(file_path) > 0):
            #print("The file is valid")
            with open(file_path, mode='r') as input_file, open(user_file_path, mode='a') as output_file:
            # Iterate over each line in the file
                for line in input_file.read().splitlines():
                    #Separate each item in the line
                    #print(line)
                    items = line.split(",")
                    #print(items)
                    #print(file)
                    stream = os.path.basename(os.path.dirname(file_path))
                    items.extend(["Y", "N", file_path,"\n"])
                    item_string = ",".join(items)
                    
                    output_file.write(item_string)
                    
                    
        
            #print(items)