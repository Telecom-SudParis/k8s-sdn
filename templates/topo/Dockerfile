FROM containernet/containernet

COPY connected_topo_args.py ./examples/
COPY Dockerfile ./

#RUN util/docker/entrypoint.sh

CMD ["python3","examples/connected_topo_args.py"]
#docker run --name containernet -it --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock -e ONOS_IP=192.168.49.2 -e ONOS_PORT=30653 --net=host connected-topo