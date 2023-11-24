pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Checkout the repository
                checkout scm
                
                // Build the Docker image
                script {
                    docker.build("employee:${env.BUILD_NUMBER}")
                }
            }
        }
    }
}
