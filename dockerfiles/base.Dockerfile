# Library template: BASE IMAGE
# Build image (base.Dockerfile : lib_template_base:latest): 
# This image has to be a multi-stage docker image with only the core depdencies and library installed in it.
# This image will be used as the base image for all the other images other than the build image.
# There will other depdencies and entry point for the other image. Once the library installed it has to be validaed with a echo command.
# There should not be any tests, docs, data, wiki, logs, notebooks, others folder and other files in the image just the library has to be installed.
# This image will be build and push to the docker repository only if all the checks are passed in the CI pipeline.
# There will be always two image push to repository while building this image one will be with library version and another will be with the latest tag.
# NOTE: only core dependencies will be installed in the base image with `--no-deps` flag.
# TODO: Same thing has to be build with CUDA depdencies.
# docker build -t lib_template_base:latest .
# docker build -t lib_template_base:v1 .
# TODO: make this multi-stage and split depdency and pin used libraries to a version
# TODO: logs and data folder has to be mounted in working directory.

FROM python:3.8-slim-buster
ENV PIP_NO_CACHE_DIR=1
ENV PATH=/root/.local/bin:$PATH
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --use-deprecated=legacy-resolver -r /requirements.txt && \
    rm -rf /root/.cache/pip
COPY . .
RUN python setup.py install