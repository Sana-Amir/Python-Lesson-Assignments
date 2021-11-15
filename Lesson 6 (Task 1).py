
x = input("Please input a sentence: ")
result= {}
for word in x.split():
    if word in result :
        result[word] += 1
    else:
        result[word]=1
print("Words: ", result)