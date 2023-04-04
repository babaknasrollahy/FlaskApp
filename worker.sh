#!/bin/bash

docker tag flaskapp 172.25.4.78:5000/flaskapp:latest

docker push 172.25.4.78:5000/flaskapp:latest

