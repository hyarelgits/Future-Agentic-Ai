# base image
FROM python:3.11

# working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt .

# install packages
RUN pip install -r requirements.txt

# copy source code
COPY . .

# expose FastAPI port
EXPOSE 8002

# start application
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8002"]
