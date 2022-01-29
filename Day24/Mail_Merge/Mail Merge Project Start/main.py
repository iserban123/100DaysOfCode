X = "[name]"
with open("Input/Names/invited_names.txt", "r") as f:
   names = f.readlines()


with open("Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()
    print(starting_letter)
for name in names:
    sname= name.strip()
    new_letter = starting_letter.replace(X, sname)
    print(new_letter)
    with open(f"Output/ReadyToSend/{sname}.txt", mode="w") as towrite:
      towrite.write(new_letter)




# for name in list_names:
