#!/bin/bash -e
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 437408603168.dkr.ecr.us-east-2.amazonaws.com

docker build -t beer-model .

docker tag beer-model:latest 437408603168.dkr.ecr.us-east-2.amazonaws.com/beer-model:latest

docker push 437408603168.dkr.ecr.us-east-2.amazonaws.com/beer-model:latest