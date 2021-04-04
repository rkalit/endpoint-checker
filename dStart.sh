#!/bin/bash

imageName="endpoint-checker"
#build image
docker build -t $imageName .

#run container
docker run --name=$imageName -d $imageName