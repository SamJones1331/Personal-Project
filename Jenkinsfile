pipeline{
    agent any
    stages{
        stage('---Build Image---'){ 
            steps{
                sh "sudo docker build -t flask-app ."
                }
            }
        stage('---clean---'){ 
            steps{
                sh label: '', script: '''if [ "$(sudo docker ps -a -q -f name=flask-app)" ];
                    then sudo docker rm -f flask-app
                    fi'''
                }
            }
        stage('---run---'){
            sudo docker run -d --name flask-app -p 5000:5000 flask-app
            }
        }
    }
}
