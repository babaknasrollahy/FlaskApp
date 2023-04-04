node('linux')
{
    stage('Pull_Source_Code'){

        git branch: 'main', url: 'https://github.com/babaknasrollahy/FlaskApp.git'

    }
    

    stage('Build_Image'){

        sh "docker build -t flaskapp ."
        sh "sudo chmod +x worker.sh"
        sh "worker.sh"
        stash "CopyEveryThing"
        input message: 'Everythings is ok . Would you like to continue??'

    }
}

node('master')
{
    stage('Run_Kubernetes_Pods'){

        unstash "CopyEveryThing"
        sh "sudo su -c 'kubectl applay -f deployment.yaml' babak"
        
    }


}
