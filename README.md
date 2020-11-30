# k8s-sdn
This tutorial will help you to understand the capabilities of Kubernetes in container orchestration and how to use its functions in practice.

## Prerequisite:
You need to have Minikube installed on your machine. Please find [here](minikube-installation.md) the instruction on how to install Minikube.

Make sure to check the IP address of the minikube VM by executing the following commands:
```
minikube ip
```
By default, the IP address is **192.168.99.100**

## Table of contents
1. [Create ONOS SDN controller (v2.2.1) Deployment](#dpl-onos-221)
2. [Create ONOS SDN controller Serivce](#svc-onos)
3. [Create GUI application (v2.0) Deployment](#dpl-gui-20)
4. [Create Mininet cluster](#dpl-mininet)
5. [Upgrade ONOS SDN controller latest version (v2.4.0)](#dpl-onos-latest)
6. [Upgrade GUI application latest version](#dpl-gui-latest)
7. [Create Forwarding application Deployment](#dpl-fwd)

## Create ONOS SDN controller (v2.2.1) Deployment <a name="dpl-onos-221"></a>
```
...
      containers:
      - name: onos-demo
        #image: onosproject/onos
        image: onosproject/onos:2.2.1
...
```
```
minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-onos.yaml
```

OR
```
kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-onos.yaml
```

## Create ONOS SDN controller Serivce <a name="svc-onos"></a>

```
minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/service/k8s-svc-onos.yaml
```
OR
```
kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/service/k8s-svc-onos.yaml
```
```
ssh -p 30101 karaf@192.168.99.100
```
The username/password is **karaf/karaf**

http://192.168.99.100:30181/onos/ui/index.html#/topo

## Create GUI application (v2.0) Deployment <a name="dpl-gui-20"></a>
```
...
      containers:
      - name: gui-app
        #image: tqhuy812/gui-app
        image: tqhuy812/gui-app:2.0
...
```
```
minikube kubectl -- create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-gui.yaml
```
OR
```
kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-gui.yaml
```

## Create Mininet cluster <a name="dpl-mininet"></a>
For Windows users, please download the Mininet VM at this link https://github.com/mininet/openflow-tutorial/wiki/Installing-Required-Software. Choose to download the VM as follows
```
...
Virtual Machine Image (OVF format, 64-bit, Mininet 2.2.2) (Recommended for most modern hardware and OSes)
...
```
Unzip then import the VM into VirtualBox. Before starting the machine, please add a new Network Adapter with "Attached to: Host-only" with Name will be the same as the one in Minikube VM

For Linux users
```
sudo mn --switch ovs --controller remote,ip=192.168.99.100,port=30653  --topo tree,depth=2,fanout=2
```

## Upgrade ONOS SDN controller latest version (v2.4.0) <a name="dpl-onos-latest"></a>

```
...
      containers:
      - name: onos-demo
        image: onosproject/onos
        #image: onosproject/onos:2.2.1
...
```
```
kubectl apply -f templates/deployment/k8s-depl-onos.yaml
```

## Upgrade GUI application latest version <a name="dpl-gui-latest"></a>

```
...
      containers:
      - name: gui-app
        image: tqhuy812/gui-app
        #image: tqhuy812/gui-app:2.0
...
```
```
kubectl apply -f templates/deployment/k8s-depl-gui.yaml
```

## Create Forwarding application Deployment <a name="dpl-fwd"></a>
```
kubectl create -f templates/deployment/k8s-depl-fwd.yaml
```

