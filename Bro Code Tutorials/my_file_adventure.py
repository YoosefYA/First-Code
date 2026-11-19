file = open("Bro Code Tutorials/my_file.txt", 'r')#'r' here is to open it in reading mode

try:
    #Read the whole file
    content = file.read()
    print("Whole file contents:\n",content)

    #Read Line by Line
    file = open("Bro Code Tutorials/my_file.txt", "r")
    for line in file:
        print("Line from file:",line.strip())
    print("-------Finished reading-------")

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if file is not None and not file.closed:
        file.close()
        print("File has been closed")

try:
    file = open("output.txt", 'w')
    file.write("Hello, world!\n")
    file.write("This is a second Line\n")
    file.close()

    file = open("output.txt", 'a')
    file.write("This file was appended to the end\n")
    file.close()

except IOError as e:
    print(f"Error opening files for reading / appending: {e}")