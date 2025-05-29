FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000   # retriever agent
EXPOSE 8001   # orchestration agent
EXPOSE 8501   # streamlit app

CMD ["bash", "start.sh"]