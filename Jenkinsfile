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
        stage('Install Dependencies') {
            steps {
                // Install Python and necessary packages
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
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
                // Run your pytest tests
                sh '''
                source venv/bin/activate
                pytest test_multivariate_linear_reg.py
                '''
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy the application (adjust this command according to your deployment method)
                    // Uncomment and modify the line below to deploy your Docker container
                    // sh "docker run -d -p 8080:8080 ${DOCKER_IMAGE}"
                    echo "Deploying application (uncomment and modify the above line to deploy your Docker container)"
                }
            }
        }
    }

    post {
        always {
            // Clean up any Docker images (optional)
            script {
                sh "docker rmi ${DOCKER_IMAGE} || true"
            }
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
