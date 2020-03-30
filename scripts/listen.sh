#!/bin/bash

#Looking for process run on 3000 port
fe_port=3000
pid=$(lsof -i :$fe_port | grep LISTEN | head -n1 | awk '{print $2}')
if [[ $pid =~ ^[0-9]+$ ]]; then
    echo 'Current FrontEnd process - ' $pid
else
    echo 'Current FrontEnd process - empty'
fi

#Looking for process run on 5001 port
be_port=5001
pid=$(lsof -i :$be_port | grep LISTEN | head -n1 | awk '{print $2}')
if [[ $pid =~ ^[0-9]+$ ]]; then
    echo 'Current Backend process - ' $pid
else
    echo 'Current Backend process - empty'
fi
