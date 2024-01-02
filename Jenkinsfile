pipeline { 
  environment { 
      registry = "${env.DOCKER_REGISTRY}" 
      registryCredential = "${env.DOCKER_REGISTRY_CREDENTIAL}" 
      dockerImage = ""
      repository = "${env.SERVICE_REPOSITORY}"
  }
  agent any 
  stages {
      stage('Cloning Git') { 
          steps { 
              git repository 
          }
      } 
      stage('Building image') { 
          steps { 
              script { 
                  dockerImage = docker.build registry + ":latest" 
              }
          } 
      }
      stage('Deploy image') { 
          steps { 
              script { 
                  docker.withRegistry( '', registryCredential ) { 
                      dockerImage.push() 
                  }
              } 
          }
      }
  }
}