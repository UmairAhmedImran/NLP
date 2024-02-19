punctuations = "!()-[]\\{};\",<>./?@#$%^&*_~"

user_input = input("Enter strings to remove punctuations: ")

str = ""
for c in user_input:
    if c not in punctuations:
        str += c

print(str)
