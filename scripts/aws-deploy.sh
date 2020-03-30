#!/bin/bash
# Script to Deploy (Upload and install) application to AWS EC2

# Directory name that will be created in EC2 instance inside /opt
AWS_PROJ_DIR='dsep'
# AWS user that will be used for authentication
AWS_USER='ec2-user'
# AWS Hostname where applciation will be host
AWS_HOST="$AWS_USER@ec2-13-56-213-50.us-west-1.compute.amazonaws.com"
# AWS SSH Key that will be user to send SSH commands
AWS_SSH_KEY='dspw.pem'

cd ..
# Put all sources into zip archive
zip -r app.zip app public scripts src .env requirements.txt package.json README.MD

# Upload zipped sources to AWS
scp -i $AWS_SSH_KEY app.zip $AWS_HOST:~/

# Remove zip archive
rm app.zip

# Stop and clean currenly run application
ssh -i $AWS_SSH_KEY $AWS_HOST "cd /opt/$AWS_PROJ_DIR/scripts && pwd && sudo ./stop.sh && sudo ./clean.sh"
# Extract newly uploaded application to destination folder
ssh -i $AWS_SSH_KEY $AWS_HOST "cd /home/$AWS_USER/ && unzip -o app.zip -d /opt/$AWS_PROJ_DIR/"
# Run new application
ssh -i $AWS_SSH_KEY $AWS_HOST "cd /opt/$AWS_PROJ_DIR/scripts && ./install.sh && ./run.sh && sudo ./listen.sh"
cd scripts
