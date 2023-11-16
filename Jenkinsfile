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
    
  }
}