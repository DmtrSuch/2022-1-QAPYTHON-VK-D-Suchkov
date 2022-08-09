pipeline {

        agent any
        stages {
            stage("Clear") {
                steps {
                    cleanWs()
                }
            }

            stage('Run docker-compose') {
                steps {
                    step([
                        $class: 'DockerComposeBuilder',
                        dockerComposeFile: 'FinProject/docker-compose.yml',
                        option: [$class: 'StartAllServices'],
                        useCustomDockerComposeFile: true
                    ])
                }
            }
        }

        post {
            always {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'alluredir']]
                ])
                cleanWs()
            }
        }
    }