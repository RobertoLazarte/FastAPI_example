# define base image
FROM python:3.6

# set working directory
WORKDIR /app

COPY . .

ENV TZ="America/Sao_Paulo"

# run command at build time
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \	
	&& echo $TZ > /etc/timezone	

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 

#CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "--workers=4", "--worker-class", "uvicorn.workers.UvicornWorker","--log-level=debug", "--capture-output", "--timeout", "1000", "--bind=0.0.0.0:8000", "api:app"] #gunicorn