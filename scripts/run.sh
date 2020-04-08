#!/bin/bash
#Activate virtual environment
source ../venv/bin/activate

#Run backend
cd ..
flask run --host 0.0.0.0 --port 5001 > /dev/null 2>&1 &
#Run Frontend
npm start  > /dev/null 2>&1 &
cd scripts
