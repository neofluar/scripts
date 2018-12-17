#! python3
# apod_download.py - downloads the last 10 jpg pictures from www.apod.nasa.gov

import os, requests, bs4
from datetime import date, timedelta

path = 'D:\\python\\automate_boring_staff\\apod_10'
os.makedirs(path, exist_ok=True)
d = date.today() + timedelta(days=1)
i = 0
while i < 10:
    # Generate url and download image page
    d -= timedelta(days=1)
    url = 'https://apod.nasa.gov/apod/ap' + d.strftime('%y%m%d') + '.html'
    res = requests.get(url)
    res.raise_for_status()
    
    # Find the URL of the image.
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    elems = soup.select('p a')
    picture_url = 'https://apod.nasa.gov/apod/' + elems[1].get('href')
    if picture_url.endswith('.jpg'):
        # Download the image
        i += 1
        print('%s Downloading image %s...' % (i, picture_url))
        res = requests.get(picture_url)
        res.raise_for_status()
            
        # Save the image to 'path'
        imageFile = open(os.path.join(path, os.path.basename(picture_url)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('The last date was', d, '\nDone.')
