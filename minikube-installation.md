# MINIKUBE INSTALLATION

Note: This document will help you to install Minikube on your Windows and Linux machine. For the instruction on macOS, please refer to this link https://kubernetes.io/docs/tasks/tools/install-minikube/

Minikube implements a local Kubernetes cluster (consisting of one Master node and one Worker node) on a single virtual machine. Minikube's primary goals are to be the best tool for local Kubernetes application development and to support all Kubernetes features that fit.

## Prerequisite
You need to have VirtualBox installed on your machine. Please also ENABLE Virtualization and DISABLE Secure Boot in the BIOS Settings.

## Install Minikube on Linux
Execute the following commands from your terminal

1/ Download and add the minikube executable script to $PATH
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```


