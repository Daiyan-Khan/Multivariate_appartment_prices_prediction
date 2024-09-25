pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'multivariate_appartment_prices_prediction-server' // Change this to your desired Docker image name
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system
                git url: 'https://github.com/Daiyan-Khan/jMultivariate_appartment_prices_prediction.git', branch: 'main'
                echo "Code has been checked out from GitHub"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (add your test command here)
                    // Example: sh 'docker run --rm ${DOCKER_IMAGE} python -m unittest discover -s tests'
                    // Uncomment and modify the above line according to your test framework
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy the application (adjust this command according to your deployment method)
                    // Example: sh 'docker run -d -p 8080:8080 ${DOCKER_IMAGE}'
                    // Uncomment and modify the above line to deploy your Docker container
                }
            }
        }
    }

    post {
        always {
            // Clean up any Docker images (optional)
            sh "docker rmi ${DOCKER_IMAGE} || true"
        }
    }
}
