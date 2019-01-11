def connect():
    import network
    import time
    SSID1 = 'Reza'
    PASS1 = 'reza1236'
    SSID2 = 'Reza-WIMAX'
    PASS2 = 'rezareza58'
 
    while True:
     
      sta_if = network.WLAN(network.STA_IF)
      if not sta_if.isconnected():
          print('connecting to network_1...')
          sta_if.active(True)
          sta_if.connect(SSID1, PASS1)
          time.sleep(10)
          
      if  sta_if.isconnected(): 
        print('network config_1:', sta_if.ifconfig())
        break   
   
      if not sta_if.isconnected():
          print('connecting to network_2...')
          sta_if.active(True)
          sta_if.connect(SSID2, PASS2)
          time.sleep(10)
        
      if  sta_if.isconnected(): 
        print('network config_2:', sta_if.ifconfig())
        break   
      
       
       
def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    try:
     addr = socket.getaddrinfo(host, 80)[0][-1]
     s = socket.socket()
     s.connect(addr) 
     print( "connection successful")
     s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
     while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    
    except Exception as err:
     
     print( "connection Unsuccessful")
      




def thingspeak_post(API_key,temp,humid):
    temp = str(temp)
    humid = str(humid)
    API_key = str(API_key)
    base_url = 'https://api.thingspeak.com/update'
    API_key = '?api_key=' + API_key
    field1 = '&field1='
    field2 = '&field2='
    url = base_url + API_key + field1 + temp + field2 + humid
    http_get(url)

























