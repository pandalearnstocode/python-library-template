# Library template generation


URL: https://pandalearnstocode.github.io/python-library-template/code/

## Features

### __Data__: 

There should be a function in library which will do the following things,
  * download data from blob
  * upload data in blob
  * clean data folder

__Note:__

* all the content of the data folder should be in gitignore.
* env variables should be used to store the blob related details.

### __Jupyter Notebooks:__

There should be two notebooks in notebooks folder showing,

* calling function from installed library
* call scripts from source folder
* in both the cases a data file from data directory has to be passed

__Note:__

* configure pre-commit hook so that no notebook with output can be sent to remote repository.

### __Docs:__

This folder should contain two things,

* library documentation (sphinx): how each function works
* project documentation (mkdocs): how project works, user guide and other details

__Note:__

Both the above should be generated using cmd and makefile. In CI pipeline whenever there is a version change both these has to be generated and has to be sent to the blob storage. from blob storage these should be published to a azure static web site.


### __Dockerfiles:__

This folder should have all the docker images which can be used during different process.

* base image
* test image
* development image
* job runner image

The base image should have minimal setup. All the other images should be built using the base image.

### __Others__:

Other reusable components which can be used for different operations in a library repository has to be stored here. Some of the examples can be,

* docker-compose files
* ci pipeline for azure
* ci pipeline for github action

### __lib_template (Source):__

Source folder is the folder where all the python scripts has to be stored. There has to be two sub-modules in the source folder. All of these will have their own tests module in the sub-module directory. All the tests which are independent from the other sub-module should live here. Any other tests which are dependent on the other module or needs interaction with the other modules can live in the main tests folder in the root directory.

### __Tests:__

All the tests which are at library or main module level should be here. No independent unit tests for sub-modules should be here. For tests we are going to use the following tools,

* pytest
* pytest-xdist
* hypothesis works


### Functionality of make file:

* upload, download content of data folder
* install and uninstall, dist generation, upload or download in blob, publish in repository, install from repository
* generate api docs
* generate project docs
* clean cache files, clean log directory, clean data folder
* generate docker, publish docker, pull docker
* format, lint and quality check, show test coverage
* run tests, generate test report, coverage report, flake8, bandit, pylint reports generation
* check static typing
* bump library version
* deep clean git repository or delete larger files from git repository history



