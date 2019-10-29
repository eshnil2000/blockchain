pipeline {
    agent none 
    stages {
        stage('Test') { 
            agent {
                docker {
                    image 'python:3.6-alpine' 
                }
            }
            steps {
                sh 'python --version' 
                sh 'pip install -r requirements.txt'
                sh 'python tests/test_blockchain.py'
            }
        }
        stage('Deploy') { 
            agent {
                docker {
                    image 'python:3.6-alpine' 
                    args '-p 5000:5000'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'chmod +x ./scripts/deliver.sh'
                sh './scripts/deliver.sh'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                sh 'chmod +x ./scripts/kill.sh'
                sh './scripts/kill.sh'
            }
        }        
    }
}


