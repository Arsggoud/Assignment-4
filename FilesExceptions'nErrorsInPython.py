try:
    with open("sample.txt","r") as file:
        for line in file:
            print(line)
except:
    FileNotFoundError
    print("Error:The File does not exist.")