# Personal-Project for QA Consulting

# Intro
I have been using ubuntu 16.04 and a vm on gcp

# Pre-Requisites

Please ensure you run these pre-requisite commnands before anything else

>sudo apt-get update  
>sudo apt-get install python3-pip  
>sudo apt-get install python3-pip  
>sudo apt install git  

# Clone the Repo
>git clone https://github.com/SamJones1331/Personal-Project.git  

# Running the App
To run the app run the following command  
>cd into the Personal-Project/application directory
>sudo mv -f venv ~/venv
.python3 -m venv venv
>run the command . venv/bin/activate
>cd ..
>pip install flask
>pip install pyopenssl
>openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
>hit enter at each prompt following this command until your get back to the command line
>run the startup.sh script
>flask run
>in a browser, navigate to https://(your_ip):5000/
>you will probably get a security warning, if so just go straight to the website anyways
>You should then be able to access the front-end of my Personal Project
>Please Enjoy

# System D
If you wish to run the app as a systemD process, then please execute the following commands
>curl https://get.docker.com | sudo bash
>sudo usermod -aG docker $(whoami)
>restart your shell
