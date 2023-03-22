#!/bin/bash

if [ -d "./env" ] 
then
    echo "env exist. So removing it and creating a new one"
    rm -r env
    python3 -m venv env 
else
    echo "env does not exist. So creating a new one"
    python3 -m venv env
fi