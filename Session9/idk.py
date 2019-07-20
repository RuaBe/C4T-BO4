
# color = ["Blue", "Red", "Green", "Teal"]
# a = input("Enter What U Want : ")
# color.append(a)
# print("Our Color List :", color, sep= " , ")

# color = ["Blue ", "Red", "Green"]
# i = int(input("Enter NUmber Here : "))
# print(color[i])


colour =['red','blue','green','teal']
for i ,colour in enumerate(colour):
    print(i+1,colour,sep =",")
a = int(input("Number: "))
colour.pop(a)
for i ,colour in enumerate(colour):
    print(i+1,colour,sep =",")
b =input("Word: ")
colour.remove(b)
for i ,colour in enumerate(colour):
    print(i+1,colour,sep =",")

