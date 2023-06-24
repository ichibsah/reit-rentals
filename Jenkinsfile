pipeline {
    agent { 
        node {
            label 'local-agent-ansible'
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