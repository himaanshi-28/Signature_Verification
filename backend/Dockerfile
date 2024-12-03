FROM python:3.9-slim

WORKDIR /backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y curl

RUN mkdir -p /app/backend/verification

RUN curl -L -o /app/backend/verification/siamese_model_final.keras https://github.com/himaanshi-28/Signature_Verification/releases/download/v1.0/siamese_model_final.keras

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
