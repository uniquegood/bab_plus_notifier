FROM python:3.11-bullseye AS builder
WORKDIR /app

COPY [".", "."]
RUN apt update && apt install -y libgl1-mesa-glx
RUN pip install -r src/requirements.txt

CMD ["python", "src/test.py", "0", "."]