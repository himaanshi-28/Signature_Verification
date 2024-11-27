pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                script {
                    sh 'docker build -t myapp:latest .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                // Stop and remove existing container
                script {
                    sh '''
                    docker stop myapp-container || true
                    docker rm myapp-container || true
                    '''
                }
                // Run new Docker container
                script {
                    sh 'docker run -d --name myapp-container -p 8080:8080 myapp:latest'
                }
            }
        }
    }
    
    post {
        always {
            // Send email notification
            emailext (
                to: 'himaanshi.sharma21@st.niituniversity.in, heshica.vanapalli21@st.niituniversity.in, monit.singh21@st.niituniversity.in',
                subject: "Jenkins Pipeline Execution: ${currentBuild.fullDisplayName}",
                body: """
                Build Status: ${currentBuild.currentResult}
                Build URL: ${env.BUILD_URL}
                Commit Triggered the Build: ${env.GIT_COMMIT}
                """
            )
        }
    }
}
