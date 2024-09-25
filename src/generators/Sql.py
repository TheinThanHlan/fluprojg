from enum import unique
import os,pathlib
from TypeConfig import mapType,types


class Column:
    constraint_list=["not null", "unique", "primary key"]
    
    def __init__(self,name,dataType,constraints,foreignKey=None):
        self.name=name
        self.dataType=dataType
        self.constraints=constraints
        
        #foreign key must be map of
        #{
        #   classname=""
        #   primaryKey=Column()
        #}
        self.foreignKey=foreignKey



    def __repr__(self):
        foreignKey_str=""
        column_type=mapType(self.dataType,"sqlite")
        if self.foreignKey!=None:
            foreignKey_str=f"REFERENCES '{self.foreignKey['classname']}'('{self.foreignKey['primaryKey']['name']}')"
            column_type=mapType(self.foreignKey["primaryKey"]["type"],"sqlite")
        sqlDefaultValue=types[self.dataType].langs['sqlite'].defaultValue if 'primary key' not in self.constraints.lower() and 'not null' in self.constraints.lower() and self.dataType in types.keys() else ''
        return f"'{self.name}' {column_type} {self.constraints} {foreignKey_str} {'Default 'if sqlDefaultValue!='' else ''}  {sqlDefaultValue}  "

class Table:
    def __init__(self,name="",unique_constraints=[],primary_keys=[]):
        self.name=name
        self.unique_constraints=unique_constraints
        self.primary_keys=primary_keys
        self.columns=[]
    


    def addColumn(self,column):
        self.columns.append(column)
        
    def __repr__(self):
        table_create_str="CREATE TABLE IF NOT EXISTS '"+self.name+"'(\n"   
        #create column
        column_str_list=[str(a) for a in self.columns]
        #create unique constraints str
        unique_constraints=[] #",".join([f"UNIQUE( {','.join([+b+"'" for b in a ])} )" for a in self.unique_constraints])
        for a in self.unique_constraints:
            tmp=[]
            for b in a:
                tmp.append("'"+b+"'")
            unique_constraints.append(tmp)

        unique_constraints_str=",".join([f"UNIQUE( {','.join(a)} )" for a in unique_constraints])


        if unique_constraints_str!="":
            column_str_list.append(unique_constraints_str)
        #add to table create str
        table_create_str+=",\n".join(column_str_list)+"\n);"
        return  table_create_str


    

class Sql:
    save_dir=""
    def __init__(self,data,config):
        self.save_dir=os.path.join(os.getcwd(),config["name"],"assets/databases")
        pathlib.Path(self.save_dir).mkdir(exist_ok=True,parents=True)
        self.data=data
    
    def generate(self):
        print("\n[sqllite]")
        tables=[]
        for a in self.data.keys():
            tmp=Table(name=a.replace("#_#_#",""),unique_constraints=self.data[a]["unique_constraints"]) 
            primaryKey=None
            for b in self.data[a]["variables"]:
                foreignKey=None
                if "primary key" in b["constraints"].lower():
                    primaryKey=b
                    
                elif b["map"].lower() in ["onetoone","manytoone"]:
                    foreignKey={
                        'classname':b["type"] if b["type"] in self.data.keys() else None,
                        'primaryKey':[abc for abc in self.data[b['type']]['variables'] if "primary key" in abc["constraints"].lower()][0]
                    }
                    
                    if foreignKey["classname"]==None:
                        raise Exception("there is no table name :"+b["type"]+" in "+"a")
                    
                    if 'primaryKey'==None:
                        raise Exception("there is no primary key in table name : "+b["type"]+";\nPlease add primary key constraints")

                    #if one to one add unique constraints
                    if b["map"].lower() == "onetoone":
                        tmp.unique_constraints.append([b["name"]])

                elif b["map"].lower() in ["manytomany","onetomany"]:
                    continue
                


                tmp.addColumn(
                    Column(name=b['name'],dataType=b['type'],constraints=b['constraints'],foreignKey=foreignKey)
                )

                

            tables.append(tmp)
            print(f"\t~=> \"{tmp.name}\"")
    
        with open(os.path.join(self.save_dir,"database.sql"),"w") as f:
            f.write("\n".join([str(a) for a in tables]));
            
        print(f"\t~=> \"assets/database.sql\"")
