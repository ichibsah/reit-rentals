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
        stage('GIT | Checkout code') {
            steps {
                deleteDir()
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ichibsah/reit-rentals.git']])
            }
        }
        stage('Ansible | Build Dockerfile') {
            steps {
                dir('./reit-rentals') {
                    ansiblePlaybook becomeUser: 'ibrahim', colorized: true, disableHostKeyChecking: true, installation: 'Ansible2', inventory: 'host.yml', playbook: 'rent.yml', sudoUser: 'ibrahim', tags: 'build'
                }
            }
        }
        stage('Ansible | Deploy Image') {
            steps {
                //
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