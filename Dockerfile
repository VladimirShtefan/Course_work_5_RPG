FROM python:3.10-slim

ENV FLASK_DEBUG=False \
    FLASK_APP=run_app.py
WORKDIR .

RUN apt-get update -y && apt-get install -y --no-install-recommends curl && apt-get autoclean && apt-get autoremove && \
    rm -rf var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
#CMD ["gunicorn", "run_app:app", "-b", "0.0.0.0:5000", "-w", "4", "--log-level=debug"]