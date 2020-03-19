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

## Create ONOS SDN controller (v2.2.1) Deployment <a name="dpl-onos"></a>
```
...
      containers:
      - name: onos-demo
        #image: onosproject/onos
        image: onosproject/onos:2.2.1
...
```

```
kubectl create -f templates/deployment/k8s-depl-onos.yaml
```




## Create ONOS SDN controller Serivce <a name="svc-onos"></a>

```
kubectl create -f templates/service/k8s-svc-onos.yaml
```
```
ssh -p 30101 karaf@192.168.99.100
```


http://192.168.99.100:30181/onos/ui/index.html#/topo

## Create GUI application (v2.0) Deployment <a name="dpl-gui"></a>
```
...
      containers:
      - name: gui-app
        #image: tqhuy812/gui-app
        image: tqhuy812/gui-app:2.0
...
```

```
kubectl create -f templates/deployment/k8s-depl-gui.yaml
```

## Create Mininet cluster <a name="dpl-mininet"></a>
```
sudo mn --switch ovs --controller remote,ip=192.168.99.100,port=30653  --topo tree,depth=2,fanout=2
```

## Upgrade ONOS SDN controller latest version (v2.4.0)
```
kubectl apply -f templates/deployment/k8s-depl-onos.yaml
```

```
...
      containers:
      - name: onos-demo
        image: onosproject/onos
        #image: onosproject/onos:2.2.1
...
```

## Upgrade GUI application latest version
```
kubectl apply -f templates/deployment/k8s-depl-gui.yaml
```
```
...
      containers:
      - name: gui-app
        image: tqhuy812/gui-app
        #image: tqhuy812/gui-app:2.0
...
```

## Create Forwarding application Deployment <a name="dpl-fwd"></a>
```
kubectl create -f templates/deployment/k8s-depl-fwd.yaml
```

