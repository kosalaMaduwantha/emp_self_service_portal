pipeline { 
  environment { 
      registry = "kosalama/essp" 
      registryCredential = 'dockerhub_id' 
      dockerImage = '' 
  }
  agent any 
  stages {
      stage('Cloning Git') { 
          steps { 
              git 'https://github.com/jpolara2016/test_app' 
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