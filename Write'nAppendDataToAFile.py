firstinp = input("Enter text to write to the file: ")
file = open("textfile.txt","w")
writedata = file.write(firstinp + "\n")
secondinp = input("Enter additional text to append: ")
appenddata = file.write(secondinp + "\n")
file.close()

with open("textfile.txt") as file1:
    for line in file1:
        print(line.strip())