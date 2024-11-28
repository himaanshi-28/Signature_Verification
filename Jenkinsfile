pipeline {
    agent any

    environment {
        IMAGE_NAME = 'signurture-image:latest'
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
        stage('Configure Git User') {
            steps {
                script {
                    bat 'git config --global user.email "himaanshi.28.2021@doonschool.com"'
                    bat 'git config --global user.name "himaanshi-28"'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t signurture/signurture-app-image:latest .'
                bat 'docker push signurture/signurture-app-image:latest'
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    bat 'docker run -d -p 5000:5000 signurture/signurture-app-image:latest'
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
