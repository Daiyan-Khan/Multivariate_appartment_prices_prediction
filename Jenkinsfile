pipeline {
    agent any  // Use any available agent (machine) to execute the pipeline

    environment {
        PYTHON_ENV = "venv"  // Define the Python virtual environment
        DOCKER_IMAGE = 'multivariate_appartment_prices_prediction-server'  // Docker image for your app
        AWS_REGION = 'us-west-2'  // AWS region where resources like S3 and CodeDeploy are hosted
        S3_BUCKET = 'daiyans-bucket'  // S3 bucket where the deployment package will be uploaded
        DEPLOYMENT_GROUP = 'JenkinsHD'  // AWS CodeDeploy deployment group for deploying the app
        APPLICATION_NAME = 'AppartmentPPredictionrice'  // CodeDeploy application name
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Step 1: Checkout the code from the specified GitHub repository (main branch)
                git url: 'https://github.com/Daiyan-Khan/Multivariate_appartment_prices_prediction.git', branch: 'main'
                echo "Code has been checked out from GitHub"
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Step 2: Set up a Python virtual environment and install necessary packages
                bat 'python -m venv %PYTHON_ENV%'  // Create a virtual environment (for Windows)
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && pip install pandas numpy==1.26.3 pytest flake8 jupyter'  
                // Activate the virtual environment and install Python dependencies (like pandas, numpy, pytest, etc.)
            }
        }

        stage('Install Dependencies') {
            steps {
                // Step 3: Ensure the virtual environment is activated (for running further steps)
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat'
            }
        }

        stage('Run Tests') {
            steps {
                // Step 4: Run any test cases that you have (e.g., using pytest)
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && python test.py'  
                // Example of running a test script, adjust to your testing framework
            }
        }

        stage('Code Q/A') {
            steps {
                // Step 5: Convert the Jupyter Notebook (if any) to a Python script for quality assurance
                bat "%PYTHON_ENV%\\Scripts\\jupyter nbconvert --to script multivate_linear_reg.ipynb"
                // Converts Jupyter notebook to Python script format (.py)
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Step 6: Build a Docker image for your application
                    bat "docker build -t ${DOCKER_IMAGE} ."
                    // The Docker image is built from the current working directory and tagged with the name stored in the `DOCKER_IMAGE` variable
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Step 7: Deploy the Docker container locally (or in your Docker environment)
                    bat "docker run -d -P ${DOCKER_IMAGE}"
                    // Run the Docker image as a container in detached mode (-d), automatically mapping ports (-P)
                }
            }
        }

        stage('Package for CodeDeploy') {
            steps {
                script {
                    // Step 8: Package the application for AWS CodeDeploy and upload it to S3
                    bat """
                    IF NOT EXIST deploy (
                        mkdir deploy
                    )
                    cd deploy

                    REM Create the appspec.yml file needed for AWS CodeDeploy to understand how to deploy the application
                    echo version: 0.0 > appspec.yml
                    echo os: linux >> appspec.yml
                    echo files: >> appspec.yml
                    echo   - source: / >> appspec.yml
                    echo     destination: /var/www/html >> appspec.yml
                    
                    cd ..

                    REM Create a tarball (compressed archive) of the deployment package
                    tar -cvf deployment-package.tar.gz -C deploy .

                    REM Upload the tarball to your S3 bucket using AWS CLI
                    "C:\\Program Files\\Amazon\\AWSCLIV2\\aws" s3 cp deployment-package.tar.gz s3://${S3_BUCKET}/deployment-package-${env.BUILD_NUMBER}.tar.gz ^
                        --region ${AWS_REGION}
                    """
                    // This stage packages the app (creates a tarball) and uploads it to S3 to be deployed by AWS CodeDeploy
                }
            }
        }
    }

    post {
        success {
            // If the pipeline completes successfully, output a message
            echo 'Build and Tests passed!'
        }
        failure {
            // If the pipeline fails, output a failure message
            echo 'Build or Tests failed!'
        }
    }
}
