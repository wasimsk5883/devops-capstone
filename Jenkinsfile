pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code'
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

        stage('Install Test Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv-ci
                    .venv-ci/bin/pip install -r product-service/requirements.txt
                '''
            }
        }

        stage('Run Product Service Tests') {
            steps {
                dir('product-service') {
                    sh '../.venv-ci/bin/python -m pytest -v tests/'
                }
            }
        }

        stage('Run Cart Service Tests') {
            steps {
                dir('cart-service') {
                    sh '''
                        ../.venv-ci/bin/pip install -r requirements.txt
                        ../.venv-ci/bin/python -m pytest -v tests/
                    '''
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t product-service:1.0 ./product-service'
                sh 'docker build -t cart-service:1.0 ./cart-service'
                echo 'Both Docker images built successfully!'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'CI pipeline failed. Check the stage logs.'
        }
    }
}
