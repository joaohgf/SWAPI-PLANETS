FROM python:3.7-alpine
COPY . /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]
