# k8s-sdn
This tutorial will help you to understand the capabilities of Kubernetes in container orchestration and how to use its functions in practice.

## Prerequisite:
You need to have Minikube installed on your machine. Please find [here](minikube-installation.md) the instruction on how to install Minikube.

## Deploy ONOS SDN controller 

```
kubectl create -f k8s-depl-onos.yaml
```


```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: onos-deployment
  labels:
    deployment: sdn-controller
spec:
  replicas: 1
  selector:
    matchLabels:
      sdn-controller: onos
  template:
    metadata:
      labels:
        sdn-controller: onos
    spec:
      containers:
      - name: onos-demo
        image: onosproject/onos

```

## Deploy ONOS SDN controller Service

```
kubectl create -f k8s-svc-onos.yaml
```

```
apiVersion: v1
kind: Service
metadata:
  name: onos-ext
  labels:
    sdn: onos-ext
spec:
  type: NodePort
  ports:
  - name: gui
    port: 8181
    nodePort: 30004
  - name: openflow
    port: 6653
    targetPort: 6653
    nodePort: 30006
  selector:
    sdn-controller: onos

```
