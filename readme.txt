to set it up:

1) install python3x (the rest of the readme assumes python3.6)
2) install pip3: 
   wget https://bootstrap.pypa.io/get-pip.py
   sudo python36 get-pip.py
3) install dependencies via pip:  
   sudo pip3 install flask
   sudo pip3 install flask_cors
   sudo pip3 install flask_restful
   sudo pip3 install pymongo
   sudo pip3 install gunicorn
4) change mongodb settings to match yours in file: rc_search.py (modify lines 6 and 7 to match your RC db location,name,port, etc)
5) run ./start
6) browse to http://localhost:5002/search/<yoursearchterm>  for example: http://localhost:5002/search/stuff

