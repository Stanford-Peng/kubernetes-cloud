FROM jjanzic/docker-python3-opencv
WORKDIR /code
ADD server /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "/code/iWebLens_server.py"]

