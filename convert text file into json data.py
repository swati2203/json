
import json


text="""Name Abhishek
designation CEO of Navgurukul
Gender Male
Age 29"""
d=open("txt.data","w")
file=d.write(text)
d.close()
dict={}
filename="txt.data"
with open(filename) as fh:
    for line in fh:
        command,description=line.strip().split(None,1)
        dict[command]=description.strip()

out_file=open("json_data","w")
json.dump(dict,out_file,indent=4,sort_keys=False)
out_file.close()
