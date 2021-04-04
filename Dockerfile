FROM python:3.9.2-alpine3.13

LABEL Maintainer="ruli simanungkalit"

COPY checkPV.py .
COPY checkRunner.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "-u", "checkRunner.py"]