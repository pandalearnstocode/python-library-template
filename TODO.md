# Features

## Data:

Right now this feature is being developed for just csv files. Later we need to extend this.

* __Initialize data folder:__
* __Download data:__
* __Upload data:__
* __Clean data:__


__Notes:__

* Use async python sdk for azure storage.
* Have entry-point notebook and function in cli app.
* Have the same feature in makefile.

## Docker:

Process of building docker images,

1. build image (build.Dockerfile : lib_template_build): all dependencies with data, this image can be used in ci pipeline to run tests and other stuff. if all the tests and other checks are passed a new library image can be build in the CI pipeline and push to docker repository. Build image has to be push to the repository. if there is not change in setup.py, requirements.txt or data_lock it should not changed. If setup.py and requirements.txt file changes dependencies has to be installed. If data lock file changes, latest files has to be download from blob.

2. library image: library dependency only
3. job runner image: library dependency with CLI app as entry point
4. development image: library image with jupyter notebook as entry point


__Notes:__

* build multi-stage docker images
* make sure that there no cache folder
* do not embed secrets inside docker images
* do not keep build level dependencies in final docker image
* once docker image is build, check with dive is there any further optimization of docker image size is possible.
