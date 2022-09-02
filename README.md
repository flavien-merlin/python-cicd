# Python Ec2 instance scanner

This repo shows how to scan every ec2 instances with tag k8s.io/role/master and Name tag devops on AWS.
The app will run every X time according to the parameter you set on Jenkins

## Install guide

##### Build and run the app with Jenkins:

```bash
$ In order to use Sonarqube, you must have the server running.
$ Jenkins :
$ Configure two creds with your AWS config and credentials.
$ Configure pipeline job
$ on the pipeline tab choose pipeline script from scm :
$ SCM : Git, 
$ Repo url : https://github.com/flavien-merlin/python-cicd.git
$ branch  : */master
$ Script Path : Jenkinsfile
```
