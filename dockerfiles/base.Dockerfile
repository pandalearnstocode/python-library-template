# Stage 1: Builder/Compiler
FROM python:3.8-slim-buster as builder
ENV PIP_NO_CACHE_DIR=1
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt-get clean
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /requirements.txt --no-deps && \
    rm -rf /root/.cache/pip

# Stage 2: Runtime/Library Image
FROM python:3.8-slim-buster
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
RUN pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org -e .