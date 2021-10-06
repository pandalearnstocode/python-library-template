For this folder we need to have a script which can download data from a blob. Whatever files are getting generated we need to have a helper function which should be able to upload the generated result in the blob as well.


* get data from blob
* upload data from blob
* clean data directory
* initialize data directory (same as get data from blob, but in case get data from blob it will check if the data is present in local or not, but in case initialization this checking will not be required.)
