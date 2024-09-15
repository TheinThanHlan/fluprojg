import pathlib
import os,sys
import user_config
def generate():
    if sys.argv[2][0].isupper():
        data_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)),"dart","data")
        componentTemplate="Component"
        files=os.listdir(os.path.join(data_dir,componentTemplate))
        to=os.path.join(os.getcwd(),user_config.getConfig()['name'],'lib','views',sys.argv[2])
        pathlib.Path(to).mkdir(parents=True,exist_ok=False)
        for a in files:
            b=""
            with open(os.path.join(data_dir,componentTemplate,a),"r") as f:
                b=f.read().replace(componentTemplate,sys.argv[2])
            
            with open(os.path.join(to,a.replace(componentTemplate,sys.argv[2])),"w") as f:
                f.write(b)
    else:
        print("ERR : component name must start with uppercase");
