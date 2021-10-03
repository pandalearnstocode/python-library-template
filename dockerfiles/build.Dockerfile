FROM python:3.8-slim-buster
ENV PIP_NO_CACHE_DIR=1
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user --trusted-host pypi.org --trusted-host files.pythonhosted.org --use-deprecated=legacy-resolver -r /requirements.txt && \
    rm -rf /root/.cache/pip