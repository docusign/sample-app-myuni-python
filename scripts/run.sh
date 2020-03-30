#!/bin/bash
cd ..
#Activate virtual environment
source venv/bin/activate
#Run Frontend
npm start > /dev/null 2>&1 &
#Run backend
flask run --host 0.0.0.0 --port 5001 > /dev/null 2>&1 &
cd scripts
