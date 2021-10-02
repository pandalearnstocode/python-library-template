FROM python:3.8-slim-buster as builder
ENV PIP_NO_CACHE_DIR=1
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /requirements.txt && \
    rm -rf /root/.cache/pip
FROM python:3.8-slim-buster
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
RUN python setup.py install && python echo_lib.py