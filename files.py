with open("file.txt", "a+") as file:
    file.write("123")
    file.seek(0)
    print(file.read())


