pipeline {
    agent any
    triggers {
        githubPush() 
    }
    environment {
        RECIPIENTS = "himaanshi.sharma21@st.niituniversity.in, heshica.vanapalli21@st.niituniversity.in, monit.singh21@st.niituniversity.in"
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                // Add build steps here
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                // Add test steps here
            }
        }
    }
    post {
        success {
            emailext (
                subject: "Jenkins Job Success: ${env.JOB_NAME}",
                body: """<p>The Jenkins job <b>${env.JOB_NAME}</b> has succeeded.</p>
                         <p>Changes were pushed to the repository.</p>""",
                recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                to: "${RECIPIENTS}"
            )
        }
        failure {
            emailext (
                subject: "Jenkins Job Failure: ${env.JOB_NAME}",
                body: """<p>The Jenkins job <b>${env.JOB_NAME}</b> has failed.</p>
                         <p>Please check the logs for details.</p>""",
                recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                to: "${RECIPIENTS}"
            )
        }
    }
}
