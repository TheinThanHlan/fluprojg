#!/bin/python3
import sys
from init import init
from TypeConfig import types,mapType
from generate import generate
from CopyResources import copyTemplate
import component_template
def helper():
    print("fluprojg\t[args]\n\n")
    print("[args] :")
    print("\t\tinit\t\t[name]\t-use to initialize the project")
    print("\t\tgen\t\t\t-use to generate the project")
    print("\t\ttemplate\t[name]\t-use to generate template file")
    print("\t\tcom\t\t[name]\t-use to generate components file in views folder")


def main():
    try:
        sys.argv[1]
        match sys.argv[1]:
            case "init":
                init()
            
            case "gen":
                generate()

            case "template":
                copyTemplate()
                
            case "com":
                component_template.generate()            
    
            case _:
                helper()
    except IndexError:
        helper()



if __name__ == "__main__":
    main()

