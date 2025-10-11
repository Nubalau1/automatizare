FROM python:3.11-slim

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY currency_exchange_rate.py /app/
COPY cronjob /etc/cron.d/cronjob
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh
RUN pip install requests

# Fix permissions
RUN chmod 0644 /etc/cron.d/cronjob

# Create log file
RUN touch /var/log/cron.log

ENTRYPOINT ["/app/entrypoint.sh"]
