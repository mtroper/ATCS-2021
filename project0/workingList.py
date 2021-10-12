careers = ["programmer","lawyer","farmer","singer"]
index = careers.index("farmer")
if "farmer" in careers:
    print("Farmer is in the list")
else:
    print("Farmer is not in the list")
careers.append("teacher")
careers.insert(0,"builder")
for i in careers:
    print(i)