FROM python:slim

COPY requirements.txt characters.yml liked_meals.yml pairer.py ./
RUN pip install -r requirements.txt && \
    chmod a+x pairer.py

EXPOSE 5000
ENTRYPOINT [ "python pairer.py" ]
