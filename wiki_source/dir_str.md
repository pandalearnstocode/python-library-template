# Directory structure of the python project


## Directory tree

```
├───data
│   ├───persistent
│   └───temporary
├───dockerfiles
│   ├───base
│   ├───build
│   ├───development
│   ├───development_jupyter       
│   ├───fastapi
│   ├───flask
│   ├───runner
│   └───streamlit
├───docs
│   ├───build
│   │   ├───doctrees
│   │   └───html
│   │       ├───_sources
│   │       └───_static
│   │           ├───css
│   │           │   └───fonts
│   │           └───js
│   └───source
│       ├───_static
│       └───_templates
├───lib_template
│   ├───sub_module_1
│   │   └───tests
│   ├───sub_module_2
│   │   └───tests
│   └───tests
├───logs
├───notebooks
├───others
│   ├───cd
│   └───ci
├───tests
└───wiki_source
    ├───css
    └───js
```

## Directory description

* __data:__ data folder will have all the datasets. any datasets which we want to push to blob or download from blob has to be placed in `temporary` folder. `persistent` folder is the folder which will have the files and hash value based mapping. this folder will be synced with a blob in a periodic basis.
* __dockerfiles:__ this directory will have multiple reusable `*.Dockerfile`, all the supporting files required to build these docker images will be in respect folder inside the `dockerfiles` directory.
* __docs:__ this folder will have all the library function related documentation in this. after running Sphinx all the API level documentation will be stored in `docs/build/html` folder. this folder has to be stored in a azure static website or should be publish in gh-pages along with the project level documentation.
* __lib_template:__ this is the source directory. All the python code to be packaged has to be placed here.
* __logs__: all the log files generated during development will be stored here. This can be synced with blob (need to think about this approach and better use-case.)
* __notebooks:__ this is the place where all the development notebook will live.
* __others:__ other reusable resources such as deployment file, blog post, reference etc will be here. Also, some of the reusable components in CI/CD pipeline can be stored here as configs files.
* __test:__ all the library level tests, regression tests, integration tests and property based tests will be stored here. Here tests must be using the installed library from existing python interpreter. 
* __wiki_source:__ all the project level documentation will live in this folder. This content will generated a HTML site using `mkdocs`. After doc generation it will produce a folder called `site` in the root directory which has to be published to a azure static website/netlify or github page for project level documentation and user guide.
