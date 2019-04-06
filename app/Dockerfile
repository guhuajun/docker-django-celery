FROM python:3.6

ADD src/requirements.prod.txt /app/
RUN pip install -r /app/requirements.prod.txt \
        --index-url http://mirrors.aliyun.com/pypi/simple/ \
        --trusted-host mirrors.aliyun.com

ADD src/ /app/
WORKDIR /app/

EXPOSE 8000
EXPOSE 5555

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers=2", "project.wsgi:application"]