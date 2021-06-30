#!/usr/bin/python3 

print("content-type: text/html")
print()

import cgi 
import subprocess 

f1 = cgi.FieldStorage()
c = f1.getvalue("x")

if c=="1":
    x=subprocess.getoutput("sudo kubectl create deployment dep1 --image=vimal13/apache-webserver-php --kubeconfig /root/kubews/admin.conf")
    print(x)

if c=="2":
    x=subprocess.getoutput("sudo kubectl run pod1 --image=vimal13/apache-webserver-php  --kubeconfig /root/kubews/admin.conf")
    print(x)

if c=="3":
    x=subprocess.getoutput("sudo kubectl delete pod pod1 --kubeconfig /root/kubews/admin.conf")
    print(x)

if c=="4":
    x=subprocess.getoutput("sudo kubectl delete deployment dep1 --kubeconfig /root/kubews/admin.conf")
    print(x)

if c=="5":
    x=subprocess.getoutput("sudo kubectl expose deployment dep1 --port=8081 --type=NodePort  --kubeconfig /root/kubews/admin.conf")
    print(x)

if c=="6":
    x=subprocess.getoutput("sudo kubectl scale deployment dep1 --replicas=2  --kubeconfig /root/kubews/admin.conf")
    print(x)
if c=="7":
    x=subprocess.getoutput("sudo kubectl get pods  --kubeconfig /root/kubews/admin.conf")
    print(x)
if c=="8":
    x=subprocess.getoutput("sudo kubectl get deployments --kubeconfig /root/kubews/admin.conf")
    print(x)
if c=="9":
    x=subprocess.getoutput("sudo kubectl get svc  --kubeconfig /root/kubews/admin.conf")
    print(x)
if c=="10":
    x=subprocess.getoutput("sudo kubectl delete all --all  --kubeconfig /root/kubews/admin.conf")
    print(x)
if c=="404":
    x=subprocess.getoutput("command not found")
    print(x)

