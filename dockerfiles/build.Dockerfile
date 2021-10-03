# Library template: BUILD IMAGE
# Build image (build.Dockerfile : lib_template_build:latest): 
# All dependencies installed with data. This image can be used in CI pipeline to run tests and QA/QC and security other stuff.
# If all the tests and other checks are passed a new library image can be build in the CI pipeline and push to docker repository.
# Build image has to be pushed to the docker repository. If there is not change in setup.py, requirements.txt or data_lock it should not changed.
# If setup.py and requirements.txt file changes dependencies has to be installed. If data lock file changes, latest files has to be download from blob.
# TODO: Split depdency file into multiple and install all of them with depdencies.
# TODO: Install agent pool or github runner depdending on which CI pipeline this image is running.
# TODO: Install CML related depdencies in the docker image to generate CML report from the docker image.
# docker build -t lib_template_build:latest .

FROM python:3.8-slim-buster
ENV PIP_NO_CACHE_DIR=1
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user --trusted-host pypi.org --trusted-host files.pythonhosted.org --use-deprecated=legacy-resolver -r /requirements.txt && \
    rm -rf /root/.cache/pip