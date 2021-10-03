# Library template: DEVELOPMENT JUPYTER IMAGE
# Build image (development-jupyter.Dockerfile : lib_template_dev_jupyter:latest):
# Jupyter notebook has to be installed.
# TODO: Same thing has to be build with CUDA depdencies.
# NOTE: This image will always have the latest tag and version.
# docker build -t  lib_template_dev_jupyter:latest .
# TODO: logs and data folder has to be mounted in working directory.

FROM lib_template_base:latest
ENV PIP_NO_CACHE_DIR=1
ENV PATH=/root/.local/bin:$PATH
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --use-deprecated=legacy-resolver jupyter notebook && \
    rm -rf /root/.cache/pip
EXPOSE 8888
CMD ["jupyter","notebook", "--ip=0.0.0.0","--port=8888","--no-browser","--allow-root"]