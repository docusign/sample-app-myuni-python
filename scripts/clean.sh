#!/bin/bash
#Clean project installation

#Deactivate virtual environment
deactivate

#Remove python virtual environment
rm -rf ../venv
rm -rf ../flask_session

#Clean react files
rm -rf ../node_modules
rm -rf ../build
rm ../package-lock.json
