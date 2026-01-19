# QR Reader API

API REST desenvolvida em Python para leitura e decodificação de QR Codes a partir de imagens.

O projeto utiliza Flask como framework web, OpenCV para processamento de imagens e a biblioteca QReader para detecção e leitura de QR Codes. A aplicação é totalmente containerizada com Docker, facilitando o deploy em ambientes de desenvolvimento, homelab ou produção.

## 🚀 Funcionalidades
- Upload de imagens via multipart/form-data
- Suporte a formatos PNG, JPG, JPEG, WEBP e GIF
- Detecção e leitura de um ou múltiplos QR Codes por imagem
- Retorno em JSON
- Pronta para execução via Docker ou Docker Compose

## 🛠️ Tecnologias
- Python 3.12
- Flask
- OpenCV
- QReader
- Docker / Docker Compose

## 📦 Executando com Docker
```bash
docker compose up --build
