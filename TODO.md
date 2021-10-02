# Features

## Data:

Right now this feature is being developed for just csv files. Later we need to extend this.


__Initialize data folder:__

Read all the files present in the data/input folder. create a files.lock file dict with key as data hash and value as file name. upload the datasets present in input folder along with the files.lock.

__Download data:__

Read the local file.lock file and file.lock file present in blob. If they are different then download the datasets for which they are different. update the local lock file.

__Upload data:__

Read the local file.lock and online file.lock file, upload the datasets for which the hash value is different between local and remote. Update the lock file in remote.

__Clean data:__

Delete all the files in input and output directory and also delete the content of file.lock dict in local.
