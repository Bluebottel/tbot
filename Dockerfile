FROM python:3.7.0
EXPOSE 80
ENV NAME tbot
RUN pip install --trusted-host pypi.python.org -r requirements.txt
WORKDIR .
COPY . .
CMD ["python3",  "main.py",  "authkeys.txt",  "@wasdmurai"]
