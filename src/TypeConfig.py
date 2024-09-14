from types import DynamicClassAttribute
from typing import Any

def mapType(dataType,to):
    for a in types.keys():
        dataType=dataType.replace(a,types[a].langs[to].dataType)
    return dataType

class TypeMapping:
    def __init__(self, langs):
        self.langs = langs




class DataType:
    def __init__(self, dataType='', defaultValue='',fromJsonFunction="{value}"):
        self.dataType = dataType
        self.defaultValue = defaultValue
        self.fromJsonFunction=fromJsonFunction
# Define the type mappings for Dart and SQLite
types = {
    "byte": TypeMapping(
        langs={
            "dart": DataType(dataType="int", defaultValue=0),
            "sqlite": DataType(dataType="INTEGER", defaultValue=0)
        }
    ),
    "short": TypeMapping(
        langs={
            "dart": DataType(dataType="int", defaultValue=0),
            "sqlite": DataType(dataType="INTEGER", defaultValue=0)
        }
    ),
    "int": TypeMapping(
        langs={
            "dart": DataType(dataType="int", defaultValue=0),
            "sqlite": DataType(dataType="INTEGER", defaultValue=0)
        }
    ),
    "long": TypeMapping(
        langs={
            "dart": DataType(dataType="int", defaultValue=0),
            "sqlite": DataType(dataType="INTEGER", defaultValue=0)
        }
    ),
    "float": TypeMapping(
        langs={
            "dart": DataType(dataType="double", defaultValue=0.0),
            "sqlite": DataType(dataType="REAL", defaultValue=0.0)
        }
    ),
    "double": TypeMapping(
        langs={
            "dart": DataType(dataType="double", defaultValue=0.0),
            "sqlite": DataType(dataType="REAL", defaultValue=0.0)
        }
    ),
    "char": TypeMapping(
        langs={
            "dart": DataType(dataType="String", defaultValue=""),
            "sqlite": DataType(dataType="TEXT", defaultValue="")
        }
    ),
    "boolean": TypeMapping(
        langs={
            "dart": DataType(dataType="bool", defaultValue=False),
            "sqlite": DataType(dataType="INTEGER", defaultValue=0)  # 0 for false, 1 for true
        }
    ),
    "DateTime": TypeMapping(
        langs={
            "dart": DataType(dataType="DateTime", defaultValue=None,fromJsonFunction="DateTime.parse({value})"),
            "sqlite": DataType(dataType="Text", defaultValue="CURRENT_TIMESTAMP")
        }
    ),
    "List": TypeMapping(
        langs={
            "dart": DataType(dataType="List", defaultValue=[]),
            "sqlite": DataType(dataType="BLOB", defaultValue='"[]"')
        }
    ),
    "Map": TypeMapping(
        langs={
            "dart": DataType(dataType="Map", defaultValue={}),
            "sqlite": DataType(dataType="BLOB", defaultValue='"{}"')
        }
    ),
    "String": TypeMapping(
        langs={
            "dart": DataType(dataType="String", defaultValue='""'),
            "sqlite": DataType(dataType="Text", defaultValue='""')
        }
    ),

}
