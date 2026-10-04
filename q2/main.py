import json
class UsersManage:
    #清空用户数据
    def clear(self):
        with open("users.json", "w",encoding="utf-8") as file:
            file.write("")

    #添加用户
    def add_user(self, name, age):
        self.name = name
        self.age = age
        with open("users.json","r",encoding="utf-8") as file:
            i =  len(file.readlines()) + 1
        with open("users.json", "a",encoding="utf-8") as file:
            json.dump({"id": i, "name": self.name, "age": self.age}, file ,ensure_ascii=False)
            file.write("\n")

    #查询用户
    def get_users(self,id):
        with open("users.json", "r",encoding="utf-8") as file:
            for line in file:
                user = json.loads(line)
                if user["id"] == id:
                    print(user)
                    break
            else:
                print("None")

    #更新用户年龄
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
    #删除用户
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
    #列出所有用户
    def list_users(self):
        with open("users.json", "r",encoding="utf-8") as file:
            for line in file:
                user = json.loads(line)
                print(user)

    #保存用户数据到JSON文件
    def save_to_json(self,des_path):
        with open("users.json", "r",encoding="utf-8") as file:
            users = [json.loads(line) for line in file]
        with open(des_path, "w",encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=False)

    #从JSON文件加载用户数据
    def load_from_json(self, src_path):
        with open(src_path, "r",encoding="utf-8") as file:
            users = json.load(file)
        with open("users.json", "w",encoding="utf-8") as file:
            for user in users:
                json.dump(user, file, ensure_ascii=False)
                file.write("\n")
    




um = UsersManage()
um.clear()
um.add_user("张三", 18)   
um.add_user("李四", 20)   
#um.list_users()  


#um.get_users(1)            
um.get_users(99)           
um.update_age(1, 19)     

um.remove_user(2)         
um.remove_user(2)         
um.list_users()          
um.save_to_json("users.json")
um2 = UsersManage()
um2.load_from_json("users.json")
um2.list_users()       
