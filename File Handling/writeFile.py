Str = "This is line1\nThis is line1\nThis is line3"

# This will overwrite the file i.e. it will not add the text it will end 
# instead it will replace the text entirely
with open("new.txt", mode="w") as f:
    f.write("This is line4\n")
    
print("File without using append:\n")    
with open('new.txt', 'r') as file:
    content = file.read()
    print(content)

# using append mode to add the content at EOF

with open("new1.txt", mode="a") as f:
    f.write("\nThis is line4\n")
    
print("File using append:\n")
with open('new1.txt', 'r') as file:
    content = file.read()
    print(content)