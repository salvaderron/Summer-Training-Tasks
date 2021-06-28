#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print("Access-Control-Allow-Origin:*")
print()

f=cgi.FieldStorage()
x1=f.getvalue("x")
y1=f.getvalue("y")
o=subprocess.getoutput("kubectl expose deployment "+x1+" --port="+y1+" --type=NodePort --kubeconfig admin.conf")
print(o)

