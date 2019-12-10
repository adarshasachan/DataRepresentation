import json


data={
    'name':'joe',
    'age':21,
    'student':True
}
#print(data)

file=open("Simple.joson",'w')
#json.dump(data,file,indent=4)
josonSrting=json.dumps(data)
print(josonSrting)