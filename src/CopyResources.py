import os,sys,pathlib
def copyTemplate():
    config_file_name=""
    try:
        config_file_name=sys.argv[2]
    except IndexError:
        config_file_name=input()
    
    config_file_name=config_file_name+".py" if ".py" not in config_file_name else config_file_name
        
    if("input" not in os.path.split(os.getcwd())):
        config_file_name=os.path.join("input",config_file_name)

    
    to=os.path.join(os.getcwd(),config_file_name)

    if(pathlib.Path(to).is_file()):
        print("the file already exist. Do you want to override it? y/n :",end="")
        if(input()=="y"):
            os.system("cp "+os.path.join(os.path.dirname(os.path.realpath(__file__)),"input/Template.py")+" "+os.path.join(os.getcwd(),config_file_name))
    else:
        os.system("cp "+os.path.join(os.path.dirname(os.path.realpath(__file__)),"input/Template.py")+" "+os.path.join(os.getcwd(),config_file_name))

