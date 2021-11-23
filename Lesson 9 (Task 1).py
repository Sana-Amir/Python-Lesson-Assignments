
#f = open('myfile.txt', 'r')
#print(f.read())

f = open("myfile.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())
