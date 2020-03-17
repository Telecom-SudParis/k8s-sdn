# MINIKUBE INSTALLATION

**Note**: This document will help you to install Minikube on your Windows and Linux (Debian based) machine. For the instruction on macOS or other Linux distros please refer to this link https://kubernetes.io/docs/tasks/tools/install-minikube/ and https://kubernetes.io/docs/tasks/tools/install-kubectl/

Minikube implements a local Kubernetes cluster (consisting of one Master node and one Worker node) on a single virtual machine. Minikube's primary goals are to be the best tool for local Kubernetes application development and to support all Kubernetes features that fit.

## Prerequisite
You need to have VirtualBox installed on your machine. Please also **ENABLE** *Virtualization* and **DISABLE** *Secure Boot* in the BIOS Settings.

## Table of contents
1.1 [Install Minikube on Linux](#install-linux)
1.2 [Install kubectl on Linux](#install-linux-kubectl)
2.1 [Install Minikube on Windows](#install-windows)
2.2 [Install kubectl on Windows](#install-windows-kubectl)

## Install Minikube on Linux <a name="install-linux"></a>
Execute the following commands from your terminal



1/ Download and add the minikube executable script to $PATH (you will need to input your root password during the process). If you haven't install curl please do it first ```sudo apt install curl```
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
If your cluster is running, the output from minikube status should be similar to:
```
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```
4/ After you have confirmed whether Minikube is working, you can continue to use Minikube or you can stop your cluster. To stop your cluster, run:
```
minikube stop
```
## Install kubectl on Linux <a name="install-linux-kubectl"></a>
kubectl is the Command Line Interface (CLI) to access the Kubernetes cluster. 
1/ Download the latest release of kubectl script using curl:

```
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
```
2/ Make the kubectl binary executable.
```
chmod +x ./kubectl
```
3/ Move the binary into your PATH
```
sudo mv ./kubectl /usr/local/bin/kubectl
```

## Install Minikube on Windows <a name="install-windows"></a>
1/ Download Minikube installer executable from the following link and install
```
https://github.com/kubernetes/minikube/releases/latest/download/minikube-installer.exe
```
2/ After the installation, open Command Prompt (cmd) and run Minikube VM
```
minikube start
```
After this command, a VM will be initialized. This may take 5-10 minutes depending on your machine. The VM is completely set up once you see this output
![alt text](https://github.com/Telecom-SudParis/k8s-sdn/blob/master/static/output-windows-minikube-start.png "minikube start output Windows")

3/ Verify the status of the Kubernetes cluster running inside the VM
```
minikube status
```
If your cluster is running, the output from minikube status should be similar to:
```
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```
4/ After you have confirmed whether Minikube is working, you can continue to use Minikube or you can stop your cluster. To stop your cluster, run:
```
minikube stop
```
## Install kubectl on Windows <a name="install-windows-kubectl"></a>
kubectl is the Command Line Interface (CLI) to access the Kubernetes cluster. 
1/ Download the latest release of kubectl script using curl from your cmd:

```
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.17.0/bin/windows/amd64/kubectl.exe
```
2/ If you want to execute kubectl command at any directory, you need to add the binary in to your PATH.
