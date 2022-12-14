properties([pipelineTriggers([githubPush()])])
pipeline {
    agent any
    parameters {
        string defaultValue: '300', name: 'INTERVAL'
    }
    environment {
        NAME = "flav"
        VERSION = "${env.BUILD_ID}"
        IMAGE = "${NAME}:${VERSION}"
        CRED = credentials('credentials')
        CONFIG = credentials('config')
    }

    stages {
        stage('Init') {
            steps {
                cleanWs()
                sh "docker kill ${NAME} || true"
                sh "docker rm ${NAME} || true"
                sh "docker rmi -f ${NAME}|| true"
            }
        }
        stage('SCM') {
            steps {
                git url: 'https://github.com/flavien-merlin/python-cicd.git', branch: 'master'
            }
        }
        stage('Build') {
            steps {
                sh "cat $CRED > credentials"
                sh "cat $CONFIG > config"
                sh "docker build -t ${IMAGE} ."
            }
        }
        stage('Deploy') {
            steps {
                sh "docker run -itd --name ${NAME} --env INTERVAL=${params.INTERVAL} ${IMAGE}"
            }
        }
    }
}