#!/bin/bash

#Looking for process run on 3000 port
fe_port=3000
pid=$(lsof -i :$fe_port | grep LISTEN | head -n1 | awk '{print $2}')
if [[ $pid =~ ^[0-9]+$ ]]; then
    echo 'Previous FrontEnd process - kill ' $pid
    lsof -i :$fe_port | grep LISTEN | awk '{print $2}' | xargs kill
else
    echo 'Previous FrontEnd process - empty'
fi

#Looking for process run on 5001 port
be_port=5001
pid=$(lsof -i :$be_port | grep LISTEN | head -n1 | awk '{print $2}')
if [[ $pid =~ ^[0-9]+$ ]]; then
    echo 'Previous Backend process - kill ' $pid
    lsof -i :$be_port | grep LISTEN | awk '{print $2}' | xargs kill
else
    echo 'Previous Backend process - empty'
fi
