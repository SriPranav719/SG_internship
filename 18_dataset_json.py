import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data) #loading the data from the json file.
    
    
    
#filtering the students with score greater than 80
for student in data :
    if student["score"] > 80:
        print(f"name :{student["name"]} , marks: {student["score"]}")
        

#updating one of the student Marks

for student in data:
    if student["name"] == "Krishna":
        student["score"] = 81
        print(f"Updated marks of Krishna")
        
        
with open("updated_data.json", "w") as file:
    json.dump(data, file, indent=3)