FROM python:3-slim

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY images/ images/
COPY backend.py .

ENTRYPOINT ["python3", "backend.py"]
