import requests
r = requests.get("http://www.google.com")
f=open("sayfa.html","w")
f.write(r.text)
f.close()
