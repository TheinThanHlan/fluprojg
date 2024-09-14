# File name is used as class Name and Table name
# Naming rules are same as java naming rules
# supported types are - 
# java premitive types and DateTime , String , List<> , Map<>
#
#
# map       = OneToOne , ManyToOne , ManyToMany
#           # OneToMany will be added automatically in other table if we mapped with ManyToOne
#
# mappedBy  = name of variable that is mapped
{
    #columns names in 2D array
    "unique_constraints": [
        #["a","b"],
        #["c"]
    ],
    #variables
    "variables": [

        # I highly recommand the id as a primary key
        # only primary key id are supported
        {
            "name": "id",
            "type": "long",
            "default_value": 0,
            "optional":True,                #is optional in dart constructor
            "constraints":"not null primary key",
            "dbAutoValue":True,                 #use the db default value 
            "map":"",
        },
        {
            "name": "createdDateTime",
            "type": "DateTime",
            "default_value": "",
            "optional":True,                #is optional in dart constructor
            "constraints":"not null",
            "dbAutoValue":True,                 #use the db default value 
            "map":"",                       # OneToOne , ManyToOne , ManyToMany 
        },
    ],

}

