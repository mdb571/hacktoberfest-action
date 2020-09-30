FROM python:3.7-slim
COPY . /hacktober
WORKDIR /hacktober
RUN pip install --target=/hacktober pygithub datetime
CMD ["python", "/hacktober/app.py"]