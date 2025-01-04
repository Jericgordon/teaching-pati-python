#create some sort of data structure to store the text in
text_of_file = []

with open("test_read_file.txt","r") as file: # this is
    line = file.readline()
    while line != "":
        text_of_file.append(line)
        line = file.readline()

with open("test_read_file.txt","w") as file: #this writes to a file, overwriting anything that was there
    file.write("'Hi Michael Pati!'\n")


with open("test_read_file.txt","a") as file: # this appends to a file, merely adding to the end of it
    file.write("'Hi Michael Pati!'\n")

print(text_of_file)
    