
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is managed in GitHub'
                checkout scm
            }
        }

        stage('Verify Project Files') {
            steps {
                sh 'ls -la'
                sh 'test -f docker-compose.yml'
                sh 'test -f product-service/app.py'
                sh 'test -f cart-service/app.py'
                echo 'Project files verified successfully'
            }
        }

        stage('Python Syntax Check') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile product-service/app.py'
                sh 'python3 -m py_compile cart-service/app.py'
                echo 'Python syntax checks passed'
            }
        }
    }
}
