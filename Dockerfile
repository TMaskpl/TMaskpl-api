FROM python:3

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /tmaskpl
WORKDIR /tmaskpl
COPY . .
RUN chmod +x /tmaskpl/script.sh
RUN 

EXPOSE 8000

ENTRYPOINT [ "/tmaskpl/script.sh" ]