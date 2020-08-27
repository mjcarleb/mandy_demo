FROM python:3.7

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

LABEL maintainer="Mark J. Carlebach <markjcarlebach@gmail.com>" \
      version="1.0"

# Change default command to run at start when someone runs the image
#CMD flask run --host=0.0.0.0 --port=5000:5001

# Save this dockerfile and go to command line
# Build image and tag as web1 from current directory
# tag so we do not have to remmeber image's hash
# docker image build -t web1 .

# Then to run container
# docker container run -it --rm --name web1 -p 5000:5000 -e FLASK_APP=app.py web1
#
# daemon mode
# docker container run -it --rm --name web1 -p 5000:5000 -e FLASK_APP=app.py -d web1
#
# tail log
# docker container logs -f web1
#
# stats
# docker container stats
#
# run 2 containers....drop optional port mapping and change name
# docker container run -it --rm --name web2 -p 5000 -e FLASK_APP=app.py -d web1
#
# auto restart
# docker container run -it --name web3 -p 5000 -e FLASK_APP=app.py -d --restart on-failure web1
#
# stop
# docker container stop web1
#
# repeating
# docker container run -it -p 5000:5000 -e FLASK_APP=app.py --rm --name web1 web1
#
# Mount local filesystem to for live code updates
# docker container run -it -p 5000:5000 -e FLASK_APP=app.py --rm --name web1  FLASK_DEBUG=1 -v $PWD:/app web1
#
# exec into container
# docker container exec -it web1 sh
#
# To run single command in container and leave (get flask version)
# docker container exec -it web1 flask --version
#
# make sure file created is owned by me
# docker container exec -it --user "$(id -u) $(id =g)" web1 touch hi.txt
#
# etc.
# to drop into interactive version of 'new' programming language in a container
# docker container run -it --rm --name testingpython python:3.5-alpine python

# Run with mounting
# docker run -it --volumne host:docker