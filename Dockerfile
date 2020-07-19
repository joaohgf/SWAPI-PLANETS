FROM python:3.7-alpine
COPY . .
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]
