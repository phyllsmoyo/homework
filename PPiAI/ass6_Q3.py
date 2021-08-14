# Question 3
print("What is your number:")
num_str = str(input())

num_list = []
sum = 0
# Loop through the numbers
for i in num_str:
  if i == "2":
    continue

  elif i == "9":
    i = int(i)
    i *= 2
    # create a list of numbers with each number as a string 
    num_list.append(str(i))
    # sum the elements 
    sum += int(i)
  
  else:
    # create a list of numbers with each number as a string 
    num_list.append(i)
    # sum the elements 
    sum += int(i)

# join all items into one string seperated by " + "
a = " + ".join(num_list)

# print the output
print(f"{a} = {sum}")
