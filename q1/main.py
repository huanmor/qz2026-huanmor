import json

result = {} 

def analyze_log(filepath: str) -> dict:
    result = {"total": 0, "by_level":{"INFO": 0 , "ERROR": 0} , "by_user":{} , "last_error": None}
    try :
        with open(filepath, 'r', encoding="utf-8") as file:
            #log_data = [json.loads(line) for line in file]
            pass
    except FileNotFoundError:
        return result 

    with open(filepath, 'r', encoding="utf-8") as file:
        try:
            log_data = [json.loads(line) for line in file]
            for entry in log_data:

                result["total"] += 1
                level = entry["level"]
                if level in result["by_level"]:
                    result["by_level"][level] += 1
                user = entry["user"]
                if user in result["by_user"]:
                    result["by_user"][user] += 1
                else :
                    result["by_user"][user] = 1 

                if level == "ERROR":
                    result["last_error"] = entry["message"]; #只记录最后一次ERROR
                return result 
        except  json.JSONDecodeError:
            continue


result = analyze_log("app.jsonl")
#print(f"\"total\":{result["total"]}")        # 5
print(result["total"])          # 5
print(result["by_level"])     # {'INFO': 3, 'ERROR': 2}
print(result["by_user"])      # {'张三': 2, '李四': 2, '王五': 1}
print(result["last_error"])   # 超时