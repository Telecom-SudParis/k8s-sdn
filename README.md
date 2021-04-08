# k8s-sdn
This tutorial will help you to understand the capabilities of Kubernetes in container orchestration and how to use its functions in practice.

## Prerequisite:
You need to be able to run the onos-minikube VM (~ 6Gb), which can be downloaded from this link https://drive.google.com/file/d/1sLxxDjChSgHRIyUOTr13hVzuLc80fMGL/view?usp=sharing

ONOS prompt
```
onos>
```

Mininet promt
```
mininet>
```

Linux user terminal
```
$
```

Super user terminal
```
#
```

You need to have Minikube installed on your machine. Please find [here](minikube-installation.md) the instruction on how to install Minikube.

Make sure to check the IP address of the minikube VM by executing the following commands:
```
minikube ip
```
By default, the IP address is **192.168.49.2** or **192.168.99.100**

Create new namespace (if necessary):
```
$ minikube kubectl -- create namespace dev
```
Set this namespace as default
```
$ minikube kubectl -- config set-context minikube  --namespace=dev
```

To enable Kubernetes Dashboard, enter the command below in another terminal:
```
$ minikube dashboard
```



## Table of contents
0. [How to create K8s components (i.e. Deployment, Service)](#how-to)
1. [Create ONOS SDN controller (v2.2.1) Deployment](#dpl-onos-221)
2. [Create ONOS SDN controller Serivce](#svc-onos)
3. [Create Mininet cluster](#dpl-mininet)
4. [Create GUI application (v1.0) Deployment](#dpl-gui-10)
5. [Upgrade ONOS SDN controller to a newer version (v2.5.0)](#dpl-onos-latest)
6. [Upgrade GUI application latest version (v2.0)](#dpl-gui-latest)
7. [Create Forwarding application Deployment](#dpl-fwd)
8. [Create Port Statistics application Deployment](#dpl-pst)

## How to create K8s components (i.e. Deployment, Service) <a name="how-to"></a>
In Kubernetes, you specify your requirement to create K8s components in YAML files. Then, you need to send this file to K8s API Server to execute accordingly by using either one of the following ways:

### a) Using K8s Dashboard (recommended)
The most convenient way to create a k8s component is to copy the content of the YAML file to k8s Dashboard then upload it. In this repo, the content for Deployment and Service creation can be found in /templates/deployment/ or /templates/service/

![Deployment by Dashboard](https://user-images.githubusercontent.com/15526152/77160326-64b6b680-6aa7-11ea-80d4-81522bef8692.png?raw=true)

### b) Using minikube commmand (apply for k8s cluster running in minikube ONLY)
Once you run the **minikube start** command on the host machine (ONOS Tutorial), it initiates the Minikube VM and deploy a k8s cluster inside. 

**minikube*** is a client command-line interface which allows you to interact with the k8s cluster deployed by Minikube. It includes commands to control both the Minikube VM and the K8s cluster.


### c) Using kubectl command (apply for all)
**kubectl** is a client command-line interface which allows you to interact with the any k8s cluster (either deployed by Minikube, Rancher, Kubespray, etc.). 


## Create ONOS SDN controller (v2.2.1) Deployment <a name="dpl-onos-221"></a>
Please make sure the following content is specified in the Deployment YAML file templates/deployment/k8s-depl-onos.yaml. In YAML, **hashtag sign (#)** is used to comment out the text.
```
...
      containers:
      - name: onos-demo
        #image: onosproject/onos
        image: onosproject/onos:2.2.1
...
```
Then you can copy the whole content to K8s dashboard
OR
```
$ minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-onos.yaml
```

OR
```
$ kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-onos.yaml
```

## Create ONOS SDN controller Serivce <a name="svc-onos"></a>
Copy the content from templates/service/k8s-svc-onos.yaml to K8s dashboard
OR
```
$ minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/service/k8s-svc-onos.yaml
```
OR
```
$ kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/service/k8s-svc-onos.yaml
```

**a) Verify that you can access the ONOS prompt via SSH**
```
$ ssh -p 30101 karaf@192.168.49.2
```
The username/password is **karaf/karaf**

**b) Verify that you can access the ONOS GUI**
http://192.168.49.2:30181/onos/ui/index.html#/topo

## Create GUI application (v1.0) Deployment <a name="dpl-gui-10"></a>
Please make sure the following content is specified in the Deployment YAML file templates/deployment/k8s-depl-gui.yaml. Then you can copy the whole content to K8s dashboard
```
...
      containers:
      - name: gui-app
        #image: tqhuy812/gui-app:latest
        image: tqhuy812/gui-app:1.0
...
```
OR
```
$ minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-gui.yaml
```
OR
```
$ kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-gui.yaml
```

## Create Mininet cluster <a name="dpl-mininet"></a>

You can start the Mininet cluster from either python executable (recommended) OR container OR mininet cmd

a/ Python executable
```
# curl https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/topo/connected_topo_args.py > connected_topo_args.py
# mn -c
# python connected_topo_args.py 192.168.49.2 30653
```
b/ Container
```
# docker run --name containernet -it --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock -e ONOS_IP=192.168.99.100 -e ONOS_PORT=30653 --net=host connected-topo
```
c/ Mininet cmd
```
# mn -c
# mn --switch ovs --controller remote,ip=192.168.99.100,port=30653  --topo tree,depth=2,fanout=2
```

## Upgrade ONOS SDN controller to a newer version (v2.5.0) <a name="dpl-onos-latest"></a>
Modify the image version from **2.2.1** to **2.5.0** in the onos Deployment template on the Dashboard
```
...
      containers:
      - name: onos-demo
        image: onosproject/onos:2.5.0
...
```
OR modify via command-line interface
```
$ minikube kubectl -- edit deployment/onos-deployment
```
OR
```
$ kubectl edit deployment/onos-deployment
```
**Verify that the ONOS version has been changed on the upper left corner of the GUI**

## Upgrade GUI application latest version (v2.0) <a name="dpl-gui-latest"></a>

Modify the image version from **1.0** to **2.0** in the gui Deployment template on the Dashboard

```
...
      containers:
      - name: gui-app
        image: tqhuy812/gui-app:2.0
...
```
OR modify via command-line interface
```
$ minikube kubectl -- edit deployment/gui-deployment
```
OR
```
$ kubectl edit deployment/gui-deployment
```

## Create Forwarding application Deployment <a name="dpl-fwd"></a>
Copy the content from templates/deployment/k8s-depl-fwd.yaml to K8s dashboard
OR
```
$ minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-fwd.yaml

```
OR
```
$ kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-fwd.yaml
```
**Verify that you can perform pingall command on the Mininet cluster**

## Create Port Statistics application Deployment <a name="dpl-pst"></a>
Copy the content from templates/deployment/k8s-depl-svc-portstats.yaml to K8s dashboard
OR
```
$ minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-svc-portstats.yaml

```
OR
```
$ kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-svc-portstats.yaml
```
**Verify that you can access the Port Stats web via this link 192.168.49.2:30500**
