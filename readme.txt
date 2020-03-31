Installation Requirements:

pip install djangorestframework
pip install django-cors-headers
pip install django-debug-toolbar
sudo apt-get install python-pygments
pip install findtools

#Install Websocket Thingy
sudo apt-get install libpq-dev python-dev 
+ https://github.com/GetBlimp/django-websocket-request-example

C:\Users\landv\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\findtools\find_files.py
# Add 

try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring

# Directly after the import statement

#Start Motioneye:
sudo -u pi meyectl startserver -b -c /home/pi/motioneye/motioneye.conf

sudo systemctl restart motioneye
sudo systemctl stop motioneye.service
sudo systemctl start motioneye.service