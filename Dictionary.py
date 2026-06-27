# Dictionary: store data using key value pairs. Uses key to acces values, keys must be unique and they use {}
book ={
    "title":"Pyhton Basics",
    "aouthor":"M. Carter",
    "price":5000,
    "Available":True
}
print(book)
print(book["title"])
print(book["price"])

#get(): access value using keys
print(book.get("publisher"))
#update a dictionary value
book["price"] = 6000
print(book)
#add a new key_value pair
book["category"] = "programing"
print(book)
#pop.remove a key_value pair
book.pop("available")
print(book)
#keys(): retirns all keys
print(book.keys())
#values():returns all values
print(book.values())
#items():returns key value pairs
print(book.items())

#looping thru a dictionary
for key,value in book.items():
    print(f{key}:{value})

account = {
        "username" : "coder_2025",
        "gmail" : "coder@gmail.com",
        "role" : "admin"
    }
print(account["username"])
age = 25
is active = True
skills= ["python", "HTML", "CSS"]
coordinate = (10, 40)
#mutaple and immutable
skills[1] = "JavaScript"
print(skills)
