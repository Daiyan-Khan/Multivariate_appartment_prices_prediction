pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'multivariate_appartment_prices_prediction-server' // Change this to your desired Docker image name
        PYTHON_ENV = "venv"  // Define the Python environment
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
                bat '''
                call %PYTHON_ENV%\\Scripts\\activate.bat && pip install -r requirements.txt
                '''
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

        stage('Run Tests') {
            steps {
                // Run your pytest tests
                bat '''
                venv\\Scripts\\activate.bat
                pytest test_multivariate_linear_reg.py
                '''
            }
        }

    }
}
