pipeline {
    agent none 
    stages {

        stage('Deploy') { 
            agent {
                docker {
                    image 'python:3.6-alpine' 
                    args '-p 5000 -network nginx-proxy --expose 5000 -e VIRTUAL_HOST=xx.proxy.chainapp.live -e VIRTUAL_PORT=5000  '
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh './scripts/deliver.sh'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                sh './scripts/kill.sh'
            }
        }        
    }
}
