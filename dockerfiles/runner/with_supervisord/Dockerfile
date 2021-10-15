FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# ________________Change the following line to with the real library whl file________________

# COPY ["<__LIBRARY NAME__>-0.0.1-py2.py3-none-any.whl", "requirements.txt", "/tmp/"]

# ________________Change the following line to with the real library whl file________________

# RUN apt-get update \
#     && apt-get -y install supervisor\
#     && apt-get clean \
#     && pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --use-deprecated=legacy-resolver /tmp/<<__LIBRARY NAME__>-0.0.1-py2.py3-none-any.whl> \
#     && pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --use-deprecated=legacy-resolver -r /tmp/requirements.txt \
#     && rm -rf /root/.cache/pip

WORKDIR /usr/src/app
COPY . /usr/src/app
CMD ["/usr/bin/supervisord"]