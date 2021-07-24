FROM python:3.9.5-slim

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade setuptools -i https://www.piwheels.org/simple
RUN pip3 install cython -i https://www.piwheels.org/simple
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install pystan
RUN pip3 install fbprophet
RUN pip3 install flask

WORKDIR /app

COPY . /app

# Following CMD keeps the container running
# Modify CMD to run the app that you require. 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
