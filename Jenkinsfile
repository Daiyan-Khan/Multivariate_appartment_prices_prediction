pipeline {
    agent any  // Use any available agent

    environment {
        PYTHON_ENV = "venv"  // Define the Python environment
        DOCKER_IMAGE = 'multivariate_appartment_prices_prediction-server' // Docker image name
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Task: Checkout the source code from GitHub
                git url: 'https://github.com/Daiyan-Khan/Multivariate_appartment_prices_prediction.git', branch: 'main'
                echo "Code has been checked out from GitHub"
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment
                bat 'python -m venv %PYTHON_ENV%'  // Use 'bat' for Windows commands
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && pip install pandas numpy==1.26.3 pytest'  // Correct activation for Windows
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install required dependencies
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests (add your test command here)
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && python test.py'  // Example using pytest
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy your application (adjust this command according to your deployment method)
                    bat "docker run -d -p 8080:8080 ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo 'Build and Tests passed!'
        }
        failure {
            echo 'Build or Tests failed!'
        }
        always {
            // Cleanup actions if needed
            echo 'Cleaning up...'
            script {
                // Stop and remove any running containers using the image
                bat '''
                FOR /F "tokens=*" %%i IN ('docker ps -q --filter "ancestor=%DOCKER_IMAGE%"') DO (
                    docker stop %%i
                    docker rm %%i
                )
                '''
                // Clean up any Docker images
                bat "docker rmi ${DOCKER_IMAGE} || exit 0"
            }
        }
    }
}
