# MIT License
#C opyright (c) 2019 https://github.com/HammiKnuff

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import urllib.request,json,notify2,time
notify2.init('Hackerspace State')
url = 'https://portal.hsbne.org/api/spacedirectory/' #link to Space API. This Links as an Example
state = False
rerun = True
req = urllib.request.Request(url)
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
while rerun is True:
    while (state == (cont['state']['open'])) is True:
        req = urllib.request.Request(url)
        urllib.request.urlopen(req).read()
        json.loads(r.decode('utf-8'))
        print((cont['state']['open'])) #for debugging
        time.sleep(5)
        continue
    else:
        if (cont['state']['open']) is True:
            n = notify2.Notification((cont['space']), 'is now Open',icon="security-high")
            state = True
            #print('Open Notify') #for debugging
            time.sleep(2)
            n.show()
            continue

        else: n = notify2.Notification((cont['space']), 'is now Closed',icon="security-low")
        state = False
        #print('Closed Notify') #for debugging
        time.sleep(2)
        n.show()
