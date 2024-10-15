# Flutter project generator

A tool for generating flutter project from data file.

## Installation

clone the repo

```bash
git clone https://github.com/TheinThanHlan/fluprojg.git
```

give path
```
export PATH=$PATH:$HOME/path to cloned dir/fluprojg/bin/
```


## Usage

initialize project
```
mkdir test
cd test
fluprojg init test
```

add assets in pubspec.yaml file
```
assets:
    - assets/databases/
```

class configurations are inside input file.

You can create your own config file using 
```
fluprojg template Human
```

after complete configuration you can generate with 
```
fluprojg gen
```






## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

##
