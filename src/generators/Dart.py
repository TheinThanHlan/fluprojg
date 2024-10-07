import os,sys,pathlib
from TypeConfig import DataType, TypeMapping, mapType,types

class Class:
    def __init__(self,name,variables=[]):
        self.name=name
        self.variables=variables

    def model(self):
        class_str=f"import '../../all.dart';\nclass {self.name} implements IMVCModel{{ \n\t"

        #create variable
        assign_variable_str="\n\t".join([
           f"{'late' if a['optional']!=True and a['default_value']=='' else '' } {mapType(a['type'],'dart')}{'?' if a['optional']==True else ''} {a['name']}{'='if a['default_value'] !='' else ''}{a['default_value']};".strip() for a in self.variables
        ])
        class_str+=assign_variable_str

        #create constructor
        constructor_assign_str=",".join([f"{'required' if a['optional']==False else ''} {'this.'+a['name']}" for a in self.variables])
        constructor_str=f"{self.name}({{{constructor_assign_str}}});"
        class_str+="\n\t"+constructor_str


        #create toJson method
        method_toJson_str="Map<String, dynamic> toJson() => {"
        method_toJson_str+=",".join([f"\"{a['name']}\":{a['name']}" for a in self.variables])
        method_toJson_str+="};"
        class_str+="\n\t"+method_toJson_str


        #create toJson without db_auto
        method_toJson_str="Map<String, dynamic> toJsonWithoutDbAuto() => {"
        method_toJson_str+=",".join([ f"\"{a['name']}\":{a['name']}"  for a in self.variables if a['dbAutoValue']==False and a['map']==''] )
        method_toJson_str+="};"

        class_str+="\n\t"+method_toJson_str

        #create fromJson method
        method_fromJson_str=f"{self.name}.fromJson(Map<String,dynamic> data): "
        _tmp_list=[]
        for a in self.variables:
            _tmp_str=f"{a['name']}="
            _tmp_str+= types.get(a['type'],TypeMapping(langs={'dart':DataType()})).langs['dart'].fromJsonFunction.format(value=f"data[\"{a['name']}\"]")
            _tmp_list.append(_tmp_str)

        method_fromJson_str+=",".join(_tmp_list)
        method_fromJson_str+=";\n"
        class_str+="\n\t"+method_fromJson_str

        method_clone=f"{self.name} clone(){{"
        method_clone+=f"return {self.name}.fromJson(this.toJson());"
        method_clone+="}"
        class_str+="\n\t"+method_clone

        class_str+="\n}\n"
        return class_str


    #create dao for user modifycations
    def dao(self):
        class_str=f"import 'package:sqflite/sqflite.dart';\nimport '../all.dart';\nclass {self.name}Dao extends {self.name}GeneratedDao{{ \n\t"
        class_str+="\n}\n"
        return class_str

    #create class for dao that include auto generated CURD
    def generatedDao(self):
        class_str=f"import 'package:sqflite/sqflite.dart';\nimport '../../all.dart';\nabstract class {self.name}GeneratedDao implements IMVCDao<{self.name}>{{ \n\t"
        class_str+="\tfinal Database db=getIt<Database>();\n"
        method=""

        #insert
        method+=f"\nFuture<int> insert({self.name} data){{\n"
        method+=f"\treturn this.db.insert(\"{self.name}\",data.toJson());"
        method+="\n}\n"

        #insert without db auto
        method+=f"\nFuture<int> insertWithoutDbAuto({self.name} data){{"
        method+=f"return this.db.insert(\"{self.name}\",data.toJsonWithoutDbAuto());"
        method+="\n}\n"



        pk_type=""
        pk_name=""
        for a in self.variables:
            if "primary key" in a['constraints'].lower():
                pk_type=mapType(a["type"],"dart")
                pk_name=a["name"]


        #delete
        method+=f"\nFuture<void> delete({pk_type} id)async{{\n"
        method+=f"\nawait this.db.delete(\"{self.name}\",where:\"{pk_name}=$id\");"
        method+="\n}\n"


        #method+="\nvoid update(){}"
        #read by id
        method+=f"\nFuture<{self.name}?> read({pk_type} id)async{{"
        method+=f"List t =await db.query(\"{self.name}\", where: \"{pk_name}=$id\");\n"
        method+=f"if (t.length == 1) {{\n"
        method+=f"return {self.name}.fromJson(t[0]);\n"
        method+="}"
        method+=f"return null;"
        method+="}\n"

        #read all
        method+=f"Future<List<{self.name}>> readAll() async {{"
        method+=f"List tmp = await db.query(\"{self.name}\");"
        method+=f"return tmp.map((value) => {self.name}.fromJson(value)).toList();"
        method+="\n}\n"


        for a in self.variables:
            if(a["map"].strip()=="" and 'primary key' not in a['constraints'].lower()):
                method+=f"Future<List<{self.name}>> searchWith_{a['name']}({mapType(a['type'],'dart')} {a['name']}) async {{"
                if(a['type']!="String" and a['type']!="char"):
                    method+=f"List tmp=await db.query('{self.name}',where:\"{a['name']}=${a['name']}\");"
                else:
                    method+=f"List tmp=await db.query('{self.name}',where:\"{a['name']}=\\\"${a['name']}\\\"\");"

                method +=f"return tmp.map((value)=>{self.name}.fromJson(value)).toList();"
                method+="\n}\n"






        class_str+=method
        class_str+="\n}\n"
        return class_str






class Dart:
    def __init__(self,data,config):
        self.save_dir=os.path.join(os.getcwd(),config["name"],"lib")

        self.data_dir=os.path.join(self.save_dir,"data")
        self.model_dir=os.path.join(self.data_dir,"generated","model")
        self.dao_dir=os.path.join(self.data_dir,"generated","dao")

        self.custom_dao_dir=os.path.join(self.data_dir,"dao")

        #create path
        pathlib.Path(self.data_dir).mkdir(exist_ok=True,parents=True)
        pathlib.Path(self.model_dir).mkdir(exist_ok=True,parents=True)
        pathlib.Path(self.dao_dir).mkdir(exist_ok=True,parents=True)
        pathlib.Path(self.custom_dao_dir).mkdir(exist_ok=True,parents=True)

        self.data=data
        self.config=config

    def generate(self):
        self.generateExports()
        self.generateInjects()
        for a in self.data.keys():
            if "#_#_#" not in a:
                ac=Class(name=a,variables=self.data[a]["variables"])
                with open(os.path.join(self.model_dir,a+".dart"),"w") as f:
                    f.write(ac.model())
                print(f"\t~=> \"data/generated/model/{a}.dart")

                with open(os.path.join(self.dao_dir,a+"GeneratedDao.dart"),"w") as f:
                    f.write(ac.generatedDao())
                print(f"\t~=> \"data/generated/dao/{a}GeneratedDao.dart\"")

                if not os.path.isfile(os.path.join(self.custom_dao_dir,a+"Dao.dart")):
                    with open(os.path.join(self.custom_dao_dir,a+"Dao.dart"),"w") as f:
                        f.write(ac.dao())
                    print(f"\t~=> \"data/dao/{a}Dao.dart\";")






    def generateExports(self):
        exports=[]
        exportFormat="export './{class_dir}.dart';"

        #generate exports
        exports=[exportFormat.format(class_dir=os.path.join("generated","model",a)) for a in self.data.keys() if "#_#_#" not in a]
        exports+=[exportFormat.format(class_dir=os.path.join("generated","dao",a+"GeneratedDao")) for a in self.data.keys() if "#_#_#" not in a]
        exports+=[exportFormat.format(class_dir=os.path.join("dao",a+"Dao")) for a in self.data.keys() if "#_#_#" not in a]
        exports.append("\nexport '../mvc_template/all.dart';")


        print("\n[dart]")
        with open(os.path.join(self.data_dir,'all.dart'),'w') as f:
            f.write("\n".join(exports))
        print(f"\t~=> \"data/generated/all.dart\"")


    def generateInjects(self):
        #generate injections
        INJECT="getIt.registerSingleton({class_name}());"
        inject_function="import '../mvc_template/all.dart';\nimport './all.dart';\nimport 'package:get_it/get_it.dart';\nvoid injectData(GetIt getIt){"
        inject_function+="\n".join([ INJECT.format(class_name=a+"Dao") for a in self.data.keys() if "#_#_#" not in a])
        inject_function+="}"
        with open(os.path.join(self.data_dir,"InjectData.dart"),"w") as f:
            f.write(inject_function);
