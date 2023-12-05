print("File handling: ")

# try: 
#     f = open('english.txt')
#     f.read()
# except FileNotFoundError:
#     print("File not found!!")
    
# with open('example.txt', 'w') as file:
#     file.write('Hello, World!')

with open('english.txt', 'r') as file:
    content = file.readline(12)
    print(content)