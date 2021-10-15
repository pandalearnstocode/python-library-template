For this folder we need to have a script which can download data from a blob. Whatever files are getting generated we need to have a helper function which should be able to upload the generated result in the blob as well.


* get data from blob
* upload data from blob
* clean data directory
* initialize data directory (same as get data from blob, but in case get data from blob it will check if the data is present in local or not, but in case initialization this checking will not be required).
* All the values of the `supervisor` will be maintained from `supervisord.conf` file. If any changes are required make the changes in this file.
* `docker build -t job_runner:latest .` to build the docker image and test all the required functionality is working fine.
* The expectation is that the docker image will trigger the python scipt as entry point and keep running this. It will restart this automatically even if the process dies because of some reason. Also, it will store all the logs in a file which can be used later to understand the running process in the container.

