# k8s-sdn
This tutorial will help you to understand the capabilities of Kubernetes in container orchestration and how to use its functions in practice.

## Prerequisite:
You need to have Minikube installed on your machine. Please find [here](minikube-installation.md) the instruction on how to install Minikube.

## Table of contents
1. [Create ONOS SDN controller Deployment](#dpl-onos)
2. [Create ONOS SDN controller Serivce](#svc-onos)
3. [Create Mininet cluster](#dpl-mininet)
4. [Create Forwarding application Deployment](#dpl-fwd)
5. [Create GUI application Deployment](#dpl-gui)

## Create ONOS SDN controller Deployment <a name="dpl-onos"></a>

```
kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-onos.yaml
```


## Create ONOS SDN controller Serivce <a name="svc-onos"></a>

```
kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/service/k8s-svc-onos.yaml
```


## Create Mininet cluster <a name="dpl-mininet"></a>
```
sudo mn --switch ovs --controller remote,ip=192.168.99.100,port=30653  --topo tree,depth=2,fanout=2
```

## Create Forwarding application Deployment <a name="dpl-fwd"></a>


## Create GUI application Deployment <a name="dpl-gui"></a>

