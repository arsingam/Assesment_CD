# Assesment_CD
Assessment repo

Files

Web application Files:
1. Flask_app.py
2. requirements.txt
3. Login.html

DockerFile:
1. Dockerfile

Configuration management scripts:
They are Ansible Playbook scripts
1. Tomcat.yml --> Install and configure tomcat application with static content
2. NGNIX.yml --> Install and configure NGNIX application with static content


DockerFile usage

Docker build -t <container name> <path to the file>

Spin a container

Docker run -ti -p 5001:5001 <container name>
