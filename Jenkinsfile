
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
    }
}
