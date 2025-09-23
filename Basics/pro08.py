name = "Python"

print(name[0])       # P
print(name[-1])      # n
print(len(name))     # 6

text = "Hello World"

print(text[0:5])   # Hello (from index 0 to 4)
print(text[:5])    # Hello (start to 4)
print(text[6:])    # World (from 6 to end)
print(text[::-1])  # Reverse string → dlroW olleH

message = "  python is fun!  "

print(message.upper())    # "  PYTHON IS FUN!  "
print(message.lower())    # "  python is fun!  "
print(message.strip())    # "python is fun!" (removes spaces)
print(message.replace("fun", "awesome"))  # "  python is awesome!  "

print("python" in message)  # True
print("java" not in message) # True

name = "Meenakshi"
age = 22

# Concatenation
print("Hello " + name)

# f-strings (Recommended)
print(f"My name is {name} and I am {age} years old.")

