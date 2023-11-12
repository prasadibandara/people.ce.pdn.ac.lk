# get all users from FEeLS
# you need to copy the cookie value in order for this to wrok
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import requests
from urllib.parse import urlparse

fileOpened = open("batch_all.txt", "w")
s = requests.Session()
url = 'https://feels.pdn.ac.lk/user/profile.php?id=1'
s.headers.update({
    'Origin': urlparse(url).netloc,
    'Referer': url
})
r = s.get(url)
# add your cookie here
s.cookies['MoodleSession'] = 'q4s60b297suihk00pjc79njkh3'
for x in range(2870, 10000):
    url = f'https://feels.pdn.ac.lk/user/profile.php?id={x}'
    r = s.get(url, headers={'X-Requested-With': 'XMLHttpRequest'})
    text = r.text

    if text.find("The details of this user are not available to you") != -1:
        print("not available to me")
        continue
    else:
        # link = r.text[text.find('''<div class="page-context-header"><div class="page-header-image"><img src="''') +
        #               74:text.find('''class=''', text.find('''<div class="page-context-header"><div class="page-header-image"><img src="''') +
        #               74)-2]
        name = text[text.find("<title>")+7:text.find("</title>")-14]
        # if len(name+link) > 200:
        #     print(name)
        #     continue
        # print(name, link)
        print(name)
        fileOpened.write(name + "\n")
fileOpened.close()
