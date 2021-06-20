FROM python:3-alpine

# set work directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

#environment variables
ENV FLASK_APP server.py
ENV FLASK_ENV development


# copy project
COPY . /app/

# expose and run the app on port 5000
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]







