pipeline {
    agent any  // Use any available agent

    environment {
        PYTHON_ENV = "venv"  // Define the Python environment
        DOCKER_IMAGE = 'multivariate_appartment_prices_prediction-server' // Docker image name
        GITHUB_TOKEN = credentials('github-token')  // GitHub Personal Access Token stored in Jenkins credentials
        GITHUB_REPO = "Daiyan-Khan/Multivariate_appartment_prices_prediction"  // GitHub repo details
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

        // New stage to trigger a release on GitHub
        stage('Release') {
            steps {
                script {
                    // Generate the tag dynamically or use a fixed version
                    def releaseTag = "v1.0.${env.BUILD_NUMBER}"  // e.g., v1.0.1 for first build, v1.0.2 for second

                    // Create a new release on GitHub using the API
                    def response = sh(script: """
                        curl -X POST \
                        -H "Authorization: token ${GITHUB_TOKEN}" \
                        -H "Content-Type: application/json" \
                        -d '{
                              "tag_name": "${releaseTag}",
                              "target_commitish": "main",
                              "name": "${releaseTag}",
                              "body": "Release created by Jenkins Pipeline",
                              "draft": false,
                              "prerelease": false
                            }' \
                        https://api.github.com/repos/${GITHUB_REPO}/releases
                    """, returnStdout: true).trim()

                    echo "GitHub Release Response: ${response}"

                    // Optionally, print the release URL for reference
                    def releaseUrl = readJSON(text: response).html_url
                    echo "Release created: ${releaseUrl}"
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
