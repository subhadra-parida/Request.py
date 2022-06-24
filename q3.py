import json
import requests
a=requests.get("http://saral.navgurukul.org/api/courses")
data=a.json()
with open("Subhadra.json","w") as file:
    h=json.dump(data,file,indent=3)
    b=json.dumps(a)
    def course():
        position=1
        for i in data["present_course"]:
            print(position,i,["name"],i["id"])
            position=position+1
        for k in data["present_course"]:
            course=int(input("selecet your course:"))
            select=data["present_course"][course-1]["id"]
            b=requests.get("http://saral.navgurukul.org/api/courses")
            data2=b.json()
            print(data2)
    course()