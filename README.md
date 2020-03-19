# k8s-sdn
This tutorial will help you to understand the capabilities of Kubernetes in container orchestration and how to use its functions in practice.

## Prerequisite:
You need to have Minikube installed on your machine. Please find [here](minikube-installation.md) the instruction on how to install Minikube.

## Table of contents
1. [Create ONOS SDN controller deployment](#dpl-onos)
2. [Create ONOS SDN controller serivce](#svc-onos)
3. [Create Mininet deployment](#dpl-mininet)
4. [Question](#question)

## Deploy ONOS SDN controller <a name="dpl-onos"></a>

```
kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/deployment/k8s-depl-onos.yaml
```


## Deploy ONOS SDN controller Service <a name="svc-onos"></a>

```
kubectl create -f https://raw.githubusercontent.com/Telecom-SudParis/k8s-sdn/master/templates/service/k8s-svc-onos.yaml
```


## Deploy Mininet <a name="dpl-mininet"></a>
```
sudo mn --switch ovs --controller remote,ip=192.168.99.100,port=30653  --topo tree,depth=2,fanout=2
```

