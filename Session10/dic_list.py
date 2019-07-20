person = {
    "name" : "E",
    "age" : 16,
    "fav" : ["eat", "sleep", "code"],
}

print(person)
person["Fav"] = ["eat", "sleep", "code"]
person["Location"] = "hanoi"

print("======================================================================")

fs = person["fav"] 
fs.append("pokemon")
fs.pop(1)
print(fs)

print("========================================================================")

person["fav"].append("movie")
person["fav"][2] = "program"

print("=====================================================================")


print(person)
