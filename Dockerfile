FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libzbar0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install torch==2.3.0+cpu torchvision==0.18.0+cpu torchaudio==2.3.0+cpu --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
