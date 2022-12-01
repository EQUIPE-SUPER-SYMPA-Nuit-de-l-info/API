FROM python:3.9

# copies des requirements.txt et installation des dépendances
COPY requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

# expose le port 8080
EXPOSE 8080

# copie du dossier api
COPY ./app /app

# vérification de la disponibilité de l'API
HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://localhost:8080/ping || exit 1

# commande de lancement de l'API
CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "8080"]