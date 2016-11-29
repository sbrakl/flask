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
### Flask with HTTPS
If you need to refer files in WithSSL folder.
Copy all file from WithSSL to root on this folder and then do a docker build as above
Certificate are created using OpenSSL for Common name *localhost* i.e. ```CN=localhost```
If you need certificate for you domain (www.myawesomedomain.com), then you need to generate your own certificates.

**Caution**
This demo uses the Flask developmental server, do not use for Production where you have heavy traffic