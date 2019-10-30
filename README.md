
## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```
3. Install requirements  
```
$ pipenv install 
``` 

4. Run the server:
    * `$ pipenv run python blockchain.py` 
    * `$ pipenv run python blockchain.py -p 5001`
    * `$ pipenv run python blockchain.py --port 5002`
    
## Docker

Another option for running this blockchain program is to use Docker.  Follow the instructions below to create a local Docker container:

1. Clone this repository
2. Build the docker container

```
$ docker build -t blockchain .
```

3. Run the container

```
$ docker run --rm -p 80:5000 blockchain
```

4. To add more instances, vary the public port number before the colon:

```
$ docker run --rm -p 81:5000 blockchain
$ docker run --rm -p 82:5000 blockchain
$ docker run --rm -p 83:5000 blockchain
```

5. Jenkins setup:
In github: 
go to repo ==> settings ==>webhook==>add webhooks
Add in webhook from Jenkins
for example: http://myserver.com:8080/github-webhook/, replace with your server address

# Automatically trigger Jenkins build
### go to repo/settings/ webhooks/ add new webhook: http://proxy.chainapp.live:8085/github-webhook/
### Get webhook from jenkins (settings/ Manage Jenkins’ -> ‘Configure System’. Make sure the path to git is correctly set, and choose ‘Manually manage hook URLs” under the ‘Github Web Hook’ section. ==> Reregister hooks
### First we need to install the GitHub Integration Plugin, this will give us the ability to configure Jenkins to use our Github repository.
### Add server ssh keys to github settings, not required though

# Nginx-server integration
*Jenkinsfile2 incorporates random subdomain generation for each container launched via Jenkins, on the nginx-server docker network (assuming nginx-proxy container has been launched on this network)

### generate random number: 
```
def UU_ID

node {
  UU_ID = sh(script: "date +%s",returnStdout: true).trim()
}

pipeline {
```

### assign random subdomain
```
stage('Deploy') { 
            agent {
                docker {
                    
                    image 'python:3.6-alpine' 
                    args '-p 5000 --network nginx-proxy --expose 5000 -e VIRTUAL_HOST='+UU_ID+'.proxy.chainapp.live -e VIRTUAL_PORT=5000  '
                }
            }
```
