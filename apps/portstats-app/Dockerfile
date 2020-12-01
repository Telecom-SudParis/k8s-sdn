FROM alpine

RUN apk add --update --no-cache py-pip

RUN pip install flask requests

COPY Dockerfile ./
COPY portstats-app.py ./

CMD ["python3","./portstats-app.py"]
