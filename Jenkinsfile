pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build("employee_management:latest")
        }
      }
    }
    stage('Deploy Docker container in docker') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}