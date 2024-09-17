import os,pprint
from TypeConfig import mapType
from generators.Sql import Sql
from generators.Dart import Dart
def generate():
    #load data
    input_files=os.listdir("input")
    data={}
    config={}
    with open(os.path.join(".config"),"r") as f:
        config=eval(f.read())
    
    for a in input_files:
        print(a)
        with open(os.path.join("input",a),"r") as f:
            data[a.replace(".py","")]=eval(f.read())

    data=addMappedBy(data)
    data=addJunctionClass(data)

    Sql(data,config).generate()
    Dart(data,config).generate()





def addMappedBy(data):
    for a in data.keys():
        for b in data[a]['variables']:
            if b['map'].lower() in ["manytoone","manytomany","onetomany"] and '#_#_#' not in  b['name'] :
                bRelation=""
                bMappedBy=b['name']
                btype=b['type']
                bTypeUse=""
                bMapName="auto"
                match b['map'].lower():
                    case "manytoone":
                        bRelation="OneToMany"
                        bTypeUse=f"List<{a}>"
                        bMapName+="ListOf"

                    case "manytomany":
                        bRelation="ManyToMany"
                        btype=btype.replace("List","").replace("<","").replace(">","")
                        bTypeUse=f"List<{a}>"
                        bMapName+="ListOf"
                    
                    case "onetomany":
                        bRelation="ManyToOne"
                        btype=btype.replace("List","").replace("<","").replace(">","")
                        bTypeUse=a
                        bMappedBy=""
                        bMapName+=""
                        
                
                #get the name of variable in a class as a list
                bvar_name_list=[c['name'] for c in data[btype]["variables"]]
                bMapName+=a;
                #create a unique variable name for many to many
                c=1
                while bMapName in bvar_name_list:
                    bMapName+="_"+str(c)
                    c+=1
                
                if b['map'].lower()=="onetomany":
                    b["mappedBy"]=bMapName.replace("#_#_#","")

                bTemplate={
                    "name": "#_#_#"+bMapName,
                    "type": bTypeUse,
                    "default_value": "",
                    "optional":True,                #is optional in dart constructor
                    "constraints":"",
                    "map":bRelation,                       # OneToOne , ManyToOne , ManyToMany 
                    "mappedBy":bMappedBy,                  # name of variable that is mapped.ManyToMany needs mappedBy
                    "dbAutoValue":False,
                }   
                data[btype]['variables'].append(bTemplate)
    for a in data.keys():
        i=0
        for b in data[a]['variables']:
            data[a]['variables'][i]['name']=b['name'].replace("#_#_#","")
            i+=1;
    return data


def addJunctionClass(data):
    tmp_data={}
    for a in data.keys():
        for b in data[a]["variables"]:
            if b["map"].lower() == "manytomany" and b.get("mappedBy")=='':
                bOwnerType=a
                bNonOwnerType=b['type'].replace("list","").replace("<","").replace(">","")
                tableName="#_#_#"+bOwnerType+bNonOwnerType
                #get the name of variable in a class as a list
                #create a unique variable name for many to many
                c=0;
                while tableName in data.keys():
                    tableName+="_"+str(c)
                    c+=1

                tmp_data[tableName]={
                        "unique_constraints": [
                            
                        ],
                        "variables": [
                            {
                                "name": bOwnerType[0].lower()+bOwnerType[1:]+"Id",
                                "type": bOwnerType,
                                "default_value": "",
                                "optional":True,
                                "constraints":"not null",
                                "map":"ManyToOne",
                                "mappedBy":"",
                            },
                            {
                                "name": bNonOwnerType[0].lower()+bNonOwnerType[1:]+"Id",
                                "type": bNonOwnerType,
                                "default_value": "",
                                "optional":True,
                                "constraints":"not null",
                                "map":"ManyToOne",
                                "mappedBy":"",
                            },
                        ],
                                            
                    }


    data={**data,**tmp_data}
    return data

