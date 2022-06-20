# check numbers in 2 different files and print a list of all common no
with open("file1.txt") as file:
 num = file.readlines()
 l = [int(n.strip()) for n in num]
with open("file2.txt") as file2:
 num2 = file2.readlines()
 l2 = [int(n.strip()) for n in num2]
all = [x for x in l if x in l2]
print(all)
# Write your code above 👆

#print(result)
