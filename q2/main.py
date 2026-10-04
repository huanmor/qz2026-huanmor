import json

class UsersManage:
    def __init__(self): 
        pass 
    def clear(self):
        with open("users.json", "w",encoding="utf-8") as file:
            file.write("")
    def add_user(self, name, age):
        self.name = name
        self.age = age
        with open("users.json","r",encoding="utf-8") as file:
            i =  len(file.readlines()) + 1
        with open("users.json", "a",encoding="utf-8") as file:
            json.dump({"id": i, "name": self.name, "age": self.age}, file ,ensure_ascii=False)
            file.write("\n")
        
    #    i += 1 
    
    
    




um = UsersManage()
um.add_user("John Doe", 30)
um.add_user("Jane Smith", 25)
print(um.name)  
#um.clear()