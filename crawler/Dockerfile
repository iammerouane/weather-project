# This file defines the Docker container that will contain the Crawler app.
# From the source image #python

FROM python:3.6-slim
# Set the default working directory
WORKDIR /app/
COPY crawler.py requirements.txt  /app/
RUN pip install -r requirements.txt
CMD ["python3","./crawler.py"]
CMD tail -f /dev/null
# When the container starts, run this
ENTRYPOINT python3 ./crawler.py
