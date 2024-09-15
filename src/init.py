import os,sys
def init():
    config={}
    try:
        config["name"]=sys.argv[2]
    except IndexError:
        print("Enter name of your project :",end="")
        config["name"]=input()

    data_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)),"dart","data/mvc_template")
    with open(os.path.join(os.getcwd(),".config"),'w') as f:
        f.write(str(config))
    os.system("flutter create "+os.path.join(os.getcwd(),config["name"]))
    os.system("cd "+config["name"]+" && flutter pub add sqflite sqflite_common_ffi go_router get_it")
    os.system("cp "+data_dir+" "+os.path.join(os.getcwd(),config["name"],"lib")+" -r")
    os.system("cp "+os.path.join(os.path.dirname(os.path.realpath(__file__)),"input")+" "+os.path.join(os.getcwd())+" -r")

