pipeline {
    agent { 
        node {
            label 'docker-agent-ansible'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    environment {
        ANSIBLE_VAULT = ''
    }
    stages {
        stage('GIT | Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ichibsah/reit-rentals.git']])
                pwd()
            }
        }
        stage('BASH | Provisions') {
            steps {
                ansiColor('xterm') {
                    sh '''
                    sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common

                    '''

                }
            }
        }        
        stage('Ansible | Build Dockerfile') {
            steps {
                ansiColor('xterm') {
                    ansiblePlaybook(
                        playbook: 'rent.yml',
                        inventory: 'host.yml',
                        tags: 'build',
                        extras: '-vvvv',
                        colorized: true
                    )
                }
            }
        }
        stage('Ansible | Deploy Image') {
            steps {
                echo "Testing.."
                sh '''
                #cd myapp
                #python3 hello.py
                #python3 hello.py --name=Brad
                '''
            }
        }
            
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                #cd myapp
                #python3 hello.py
                #python3 hello.py --name=Brad
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}