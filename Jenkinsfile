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
        stage('Ansible | Build Dockerfile') {
            steps {
                pwd()
                dir('./') {
                    ansiblePlaybook becomeUser: 'ibrahim', colorized: true, disableHostKeyChecking: true, inventory: 'host.yml', playbook: 'rent.yml', tags: 'build'
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