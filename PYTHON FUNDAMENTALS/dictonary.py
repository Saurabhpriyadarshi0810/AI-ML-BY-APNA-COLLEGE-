info = {
    "name" : "Saurabh ",
    "cgpa" : 8.47 ,
    "Subject" : [ "COA" , "CN" ,"DAA" , "ETC", "DBMS" , "FLAT"]
}

print(info)
print(type(info))
print(info["name"])
info["name"] = "Saurabh Priyadarshi"
print(info)
print("\n\n\n\n")


# methods of dictonary 

print(info.keys())
print(info.values())
print(info.items())
print(info.get("cgpa"))
print(info.update({"pi":3.14}))

print(f"\n\n\n")
print(info )


