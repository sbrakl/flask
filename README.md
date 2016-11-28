# flask
This repository containers the docker file and simple Flask application which would display the machine IP and Host Name

It uses Python 2.7 images with Flask 1.10

Build the image using the following command

```bash
$ docker build -t sbrakl/flask:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 sbrakl/flask
```
