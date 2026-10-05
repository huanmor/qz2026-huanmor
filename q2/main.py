import json
class UserManager:
    def __init__(self):
        self.users = []
        #self.load_users()

    

    #添加用户
    def add_user(self,name,age):
        id = len(self.users) + 1
        user = {"id": id, "name": name, "age": age}
        self.users.append(user)
        #with open("users.json", "a",encoding="utf-8") as file:
        #    json.dump(user,file,ensure_ascii=False)

    def get_user(self,id):
        for user in self.users:
            if user["id"] == id:
                print(user)
                return
        print("None")

    def update_age(self,id,new_age):
        for user in self.users:
            if user["id"] == id:
                user["age"] = new_age
                #self.save_users()
                print("True")
                return
        print("None")

    def remove_user(self,id):
        for user in self.users:
            if user["id"] == id:
                self.users.remove(user)
                #self.save_users()
                print("True")
                return
        print("False")

    def list_users(self):
        for user in self.users:
            print(user)

    def save_to_json(self,des_path):
        with open(des_path, "w",encoding="utf-8") as file:
            for user in self.users:
                json.dump(user, file, ensure_ascii=False)
                file.write("\n")

    def load_users(self):
            with open("users.json", "r",encoding="utf-8") as file:
                for line in file:
                    user = json.loads(line)
                    self.users.append(user)

    #加载用户数据
    def load_from_json(self,src_path):
        with open(src_path, "r",encoding="utf-8") as file:
              for line in file:
                user = json.loads(line)
                self.users.append(user)
um = UserManager()
um.add_user("张三", 18)    
um.add_user("李四", 20)    
um.get_user(1)          
um.get_user(99)         
um.update_age(1, 19)      
um.remove_user(2)         
um.remove_user(2)         
um.list_users()           
um.save_to_json("users.json")
um2 = UserManager()
um2.load_from_json("users.json")
um2.list_users()         