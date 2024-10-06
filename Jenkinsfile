pipeline {
    agent any  // Use any available agent

    environment {
        PYTHON_ENV = "venv"  // Define the Python environment
        DOCKER_IMAGE = 'multivariate_appartment_prices_prediction-server' // Docker image 
        AWS_REGION = 'us-west-2'  // Set your AWS region
        S3_BUCKET = 'my-bucket'  // S3 bucket for storing the deployment archive
        DEPLOYMENT_GROUP = 'JenkinsHD'  // Your CodeDeploy deployment group
        APPLICATION_NAME = 'AppartmentPPredictionrice'  // Your CodeDeploy application name
        AWS_ACCESS_KEY_ID = 'AKIAXEFUNVV6TPLYLQMW'  // AWS credentials from Jenkins
        AWS_SECRET_ACCESS_KEY = 'CliINtqAD6I6AVJFCELDXa0jefAH8PPddu9zJ9Zt'
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
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && pip install pandas numpy==1.26.3 pytest flake8 jupyter'  // Correct activation for Windows
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

        stage("Code Q/A") {
            steps {
                bat "%PYTHON_ENV%\\Scripts\\jupyter nbconvert --to script multivate_linear_reg.ipynb"
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
                    bat "docker run -d -P ${DOCKER_IMAGE}"
                }
            }
        }

       stage('Package for CodeDeploy') {
    steps {
        script {
            // Check if the deploy directory exists, and create it if it doesn't
            bat """
            IF NOT EXIST deploy (
                mkdir deploy
            )
            cd deploy

            // Create the appspec.yml file if it doesn't exist
            echo "version: 0.0" > appspec.yml
            echo "os: linux" >> appspec.yml
            echo "files:" >> appspec.yml
            echo "  - source: /" >> appspec.yml
            echo "    destination: /var/www/html" >> appspec.yml
            
            // Package files
            tar -czvf deployment-package.tar.gz *   // Package files
            cd ..

            // Upload to S3
            aws s3 cp deploy/deployment-package.tar.gz s3://${S3_BUCKET}/deployment-package-${env.BUILD_NUMBER}.tar.gz \
                --region ${AWS_REGION} \
                --access-key ${AWS_ACCESS_KEY_ID} \
                --secret-key ${AWS_SECRET_ACCESS_KEY}
            """
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
