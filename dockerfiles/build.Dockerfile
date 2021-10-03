# Library template: BUILD IMAGE
# build image (build.Dockerfile : lib_template_build:latest): all dependencies with data, this image can be used in ci pipeline to run tests and other stuff.
# if all the tests and other checks are passed a new library image can be build in the CI pipeline and push to docker repository. Build image has to be pushed 
# to the repository. if there is not change in setup.py, requirements.txt or data_lock it should not changed. If setup.py and requirements.txt file changes 
# dependencies has to be installed. If data lock file changes, latest files has to be download from blob.

FROM python:3.8-slim-buster
ENV PIP_NO_CACHE_DIR=1
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user --trusted-host pypi.org --trusted-host files.pythonhosted.org --use-deprecated=legacy-resolver -r /requirements.txt && \
    rm -rf /root/.cache/pip