
import time

import requests
from datetime import datetime
while True:

    r = requests.get("https://fcd.terra.dev/v1/circulatingsupply/luna")

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M")

    f = open("luna.csv","a")
    rfloat = float (r.text)
    f.write(date_time+","+r.text+"\n")
    print (date_time,rfloat)

    time.sleep(3600)