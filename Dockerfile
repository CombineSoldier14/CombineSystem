FROM alpine:latest

WORKDIR /CombineSystemImg

RUN apk add git

RUN apk add python3

RUN apk add py3-pip

RUN git clone https://github.com/CombineSoldier14/CombineSystem

WORKDIR /CombineSystemImg/CombineSystem

RUN pip install -r requirements.txt --break-system-packages

CMD ["python", "main.py"]
