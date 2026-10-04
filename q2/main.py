import json
def rewrite():
    with open("users.json", "w",encoding="utf-8") as f:
                for line in lines:
                    json.dump(line,f,ensure_ascii=False) 
                    f.write("\n")
class UsersManage:
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

    
    def get_users(self,id):
        with open("users.json", "r",encoding="utf-8") as file:
            for line in file:
                user = json.loads(line)
                if user["id"] == id:
                    print(user)
                    break
            else:
                print("None")


    def update_age(self,id,new_age):
        lines = []
        flog = True
        with open("users.json", "r", encoding="utf-8") as file:
            for line in file:
                user = json.loads(line)
                if user["id"] == id:
                    user["age"] = new_age
                    flog = False 
                lines.append(user)    
            
        if(flog):
            print("None")
            #重新写入   

        #print(lines)
        with open("users.json", "w",encoding="utf-8") as f:
            for line in lines:
                json.dump(line,f,ensure_ascii=False) 
                f.write("\n")

    def remove_user(self,id):
        lines = []
        flog = True
        with open("users.json", "r", encoding="utf-8") as file:
            for line in file:
                user = json.loads(line)
                if user["id"] == id:
                    flog = False   
                    continue 
                lines.append(user)
        if(flog):
            print("None")
        else:
            print("True")
                  
        
        with open("users.json", "w",encoding="utf-8") as f:
            for line in lines:
                json.dump(line,f,ensure_ascii=False) 
                f.write("\n")

       
    
    
    




um = UsersManage()
um.clear()
um.add_user("John Doe", 30)
um.add_user("Jane Smith", 25)
um.add_user("Alice Johnson", 28)
um.add_user("Bob Brown", 35)
um.add_user("Charlie Davis", 22)
#um.get_users(1)
um.remove_user(3)
um.remove_user(3)
um.update_age(1, 31)
