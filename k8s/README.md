# 3-4
```
NAME                                READY   STATUS    RESTARTS   AGE
pod/timezone-app-7b78f5fc48-sc64p   1/1     Running   1          5m37s

NAME                   TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/kubernetes     ClusterIP      10.96.0.1     <none>        443/TCP          71d
service/timezone-app   LoadBalancer   10.97.45.94   localhost     8000:30121/TCP   3m40s

```

# 7-8

```
NAME                                    READY   STATUS    RESTARTS   AGE
pod/tz-app-deployment-c5b885b49-7kjhf   1/1     Running   0          26m
pod/tz-app-deployment-c5b885b49-jnjhb   1/1     Running   0          26m
pod/tz-app-deployment-c5b885b49-l8tpg   1/1     Running   0          26m

NAME                     TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes       ClusterIP      10.96.0.1      <none>        443/TCP          71d
service/tz-app-service   LoadBalancer   10.104.33.83   localhost     8000:32207/TCP   26m
```

# Helm

```
NAME                          READY   STATUS    RESTARTS   AGE
pod/tz-app-564b797997-5xwhm   1/1     Running   0          2m

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          71d
service/tz-app       LoadBalancer   10.99.174.44   localhost     8000:31317/TCP   2m
```
