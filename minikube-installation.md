# MINIKUBE INSTALLATION

Note: This document will help you to install Minikube on your Windows and Linux machine. For the instruction on macOS, please refer to this link https://kubernetes.io/docs/tasks/tools/install-minikube/

Minikube implements a local Kubernetes cluster (consisting of one Master node and one Worker node) on a single virtual machine. Minikube's primary goals are to be the best tool for local Kubernetes application development and to support all Kubernetes features that fit.

## Prerequisite
You need to have VirtualBox installed on your machine. Please also **ENABLE** Virtualization and **DISABLE** Secure Boot in the BIOS Settings.

## Table of contents
1. [Install Minikube on Linux](#install-linux)
2. [Install Minikube on Windows](#install-windows)

## Install Minikube on Linux <a name="install-linux"></a>
Execute the following commands from your terminal

1/ Download and add the minikube executable script to $PATH (you will need to input your root password during the process)
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```
2/ Run minikube VM
```
minikube start
```
After this command, a VM will be initialized. This may take 5-10 minutes depending on your machine. The VM is completely set up once you see this output
![alt text](https://github.com/Telecom-SudParis/k8s-sdn/blob/master/static/output-linux-minikube-start.png "minikube start output Linux")
3/ Verify the status of the Kubernetes cluster running inside the VM
```
minikube status
```
4/ After you have confirmed whether Minikube is working, you can continue to use Minikube or you can stop your cluster. To stop your cluster, run:
```
minikube stop
```

## Install Minikube on Windows <a name="install-windows"></a>
