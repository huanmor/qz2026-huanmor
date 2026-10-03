import json

result = {} 

def analyze_log(filepath: str) -> dict:
    result = {"total": 0, "by_level":{"INFO": 0 , "ERROR": 0} , "by_user":{} , "last_error": None}
    try :
        with open(filepath, 'r', encoding="utf-8") as file:
            pass
    except FileNotFoundError:
        return result 

    with open(filepath, 'r', encoding="utf-8") as file:
        for line in file:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            entry= json.loads(line)
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
            

result = analyze_log("bad.jsonl")
print(result["total"]) 
print(result["by_level"])    
print(result["by_user"])      
print(result["last_error"])   