# Question 2
print("What is your number:")
num_str = str(input())

num_list = []
sum = 0
# Loop through the numbers
for i in num_str:
  # create a list of numbers with each number as a string 
  num_list.append(i)
  # sum the elements 
  sum += int(i)
# join all items into one string seperated by " + "
a = " + ".join(num_list)

# print the output
print(f"{a} = {sum}")
