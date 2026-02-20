with open("data.txt","r") as file:
    content = file.read()
print(content)

with open("output.txt","w") as file:
    file.write("Hello Python\n")
    file.write("Using with statement")


with open("output.txt","a") as file:
    file.write("\nLearning best practices")

