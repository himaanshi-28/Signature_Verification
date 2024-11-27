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
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker stop ${CONTAINER_NAME} || true'
                    sh 'docker rm ${CONTAINER_NAME} || true'
                    
                    sh 'docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME}'
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
                 subject: "Jenkins Pipeline Build Failed",
                 body: "The build for the repository ${env.JOB_NAME} has failed. Please check the logs for more details."
        }
        success {
            mail to: "${EMAIL_RECIPIENT1}, ${EMAIL_RECIPIENT2}, ${EMAIL_RECIPIENT3}",
                 subject: "Jenkins Pipeline Build Successful",
                 body: "The build for the repository ${env.JOB_NAME} was successful. Your app is running in a Docker container."
        }
    }
}
