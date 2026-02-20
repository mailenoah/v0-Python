newfile =open("output.txt","w")
newfile.write("Hello Python\n")
newfile.write("File handling is useful")
newfile.close()

newfile =open("output.txt","a")
newfile.write("Hello Python, is easy to learn\n")
newfile.write("File handling is useful and we must use em")
newfile.close()

name =input("Enter student name: ")

file =open("students.txt","a")
file.write(name +"\n")
file.close()
