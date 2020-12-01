FROM alpine

RUN apk add --update --no-cache py-pip

RUN pip install flask requests

COPY Dockerfile ./
COPY port_stats.py ./

CMD ["python3","./port_stats.py"]


