while True:
    file_name = input("Enter the name of the text file you want to open: ")

    try:
        file = open(file_name, 'w')
        # file_contents = file.read()
        # print(f"File '{file_name}' contents:")
        # print(file_contents)
        file.close()  
        break
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please enter a valid file name.")
    # except ValueError:
    #     print("Invalid input. Please enter a valid file name.")