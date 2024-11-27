pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-app-image'
        CONTAINER_NAME = 'my-app-container'
        EMAIL_RECIPIENT1 = 'himaanshi250803@gmail.com'
        EMAIL_RECIPIENT2 = 'heshica2003@gmail.com'
        EMAIL_RECIPIENT3 = 'monit.singh1626@gmail.com'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/himaanshi-28/Signature_Verification.git' 
            }
        }
        stage('Fetch and Integrate CNN Model') {
            steps {
                script {
                    bat """
                    REM Fetch the CNN model branch
                    git fetch origin CNN_Model
                    git checkout CNN_Model
                    
                    REM Copy CNN model files to a temporary folder
                    if not exist CNN_Model mkdir CNN_Model
                    xcopy * ..\\CNN_Model /E /I /Y

                    REM Switch back to the main branch and integrate the model
                    git checkout main
                    xcopy ..\\CNN_Model\\* CNN_Model /E /I /Y
                    git add CNN_Model
                    git commit -m "Integrated CNN model from branch"
                    """
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    bat 'docker stop %CONTAINER_NAME% || true'
                    bat 'docker rm %CONTAINER_NAME% || true'
                    
                    bat 'docker run -p 8888:8888 %IMAGE_NAME%'
                }
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
        failure {
            mail to: "${EMAIL_RECIPIENT1}, ${EMAIL_RECIPIENT2}, ${EMAIL_RECIPIENT3}",
                 subject: "🔴 Jenkins Pipeline Build Failed - ${env.JOB_NAME}",
                 body: """
                 <h1 style="color:red;">Pipeline Build Failed</h1>
                 <p>The build for <b>${env.JOB_NAME}</b> failed.</p>
                 <h3>Details:</h3>
                 <ul>
                    <li><b>Build Number:</b> ${env.BUILD_NUMBER}</li>
                    <li><b>Project:</b> ${env.JOB_NAME}</li>
                    <li><b>Build URL:</b> <a href="${env.BUILD_URL}">View Build Logs</a></li>
                 </ul>
                 <p>Please check the logs for more details.</p>
                 """,
                 mimeType: 'text/html'
        }
        success {
            mail to: "${EMAIL_RECIPIENT1}, ${EMAIL_RECIPIENT2}, ${EMAIL_RECIPIENT3}",
                 subject: "🟢 Jenkins Pipeline Build Successful - ${env.JOB_NAME}",
                 body: """
                 <h1 style="color:green;">Pipeline Build Successful</h1>
                 <p>The build for <b>${env.JOB_NAME}</b> was completed successfully!</p>
                 <h3>Details:</h3>
                 <ul>
                    <li><b>Build Number:</b> ${env.BUILD_NUMBER}</li>
                    <li><b>Project:</b> ${env.JOB_NAME}</li>
                    <li><b>Build URL:</b> <a href="${env.BUILD_URL}">View Build Logs</a></li>
                    <li><b>App Status:</b> Running in a Docker container (<b>${CONTAINER_NAME}</b>).</li>
                 </ul>
                 <p>Thank you for your effort!</p>
                 """,
                 mimeType: 'text/html'
        }
    }
}
