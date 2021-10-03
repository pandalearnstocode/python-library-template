# Features

## Data:

Right now this feature is being developed for just csv files. Later we need to extend this.

1. __Initialize data folder:__
2. __Download data:__
3. __Upload data:__
4. __Clean data:__


__Notes:__

* Use async python sdk for azure storage.
* Have entry-point notebook and function in cli app.
* Have the same feature in makefile.

## Docker:

Process of building docker images,

1. __build image__: Done
2. __base image:__ WIP
3. __job runner image:__ TODO
4. __development jupyter image:__ TODO
5. __development image:__ TODO
6. __streamlit image:__ TODO
7. __Fast API image:__ TODO
8. __Flask image:__ TODO

__Notes:__

* build multi-stage docker images
* make sure that there no cache folder
* do not embed secrets inside docker images
* do not keep build level dependencies in final docker image
* once docker image is build, check with dive is there any further optimization of docker image size is possible.
