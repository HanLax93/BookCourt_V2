# BookCourt
## Wechat packet capture:

1.Setup [`Proxifier`](https://www.proxifier.com/)
  
  - Profiles - Proxy Servers -Add:
    
    - Address: 127.0.0.1
      
    - Port: $PORT
      
    - Protocol: HTTPS
      
  - Proxification Rules - Add:
    
    - Name: $CUSTOM
      
    - Applications: every *WeChatApp.exe*、every *WeChatAppEx.exe*
      
    - Action: Proxy HTTPS 127.0.0.1
      
  - Enable $CUSTOM and set *Localhost* as Direct
  
2.Setup [`Burp Suite`](https://portswigger.net/burp)
  
  - Proxy - Options -Proxy Listenners:
    
    - Bind to port: $PORT
      
    - Bind to adderss: *Loopback only*
    
3.Open mini program

4.Burp Suite - Proxy - Intercept - Intercept is on

## How to use:
- Choose the court and time drop-down list respectively
- Fill your token captured in the above steps
- Don't change the numbers if not necessary
- Click the button SURPRISE ME and wait for the result.

## Tips:
path of *WeChatApp.exe*:
````shell
C:\Users\$USERNAME\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\XWeb\$RANDOM_NUMBER\extracted\wechatapp.exe
````
- Note: find all WeChatApp.exe in every `$RANDOM_NUMBER` folder.

path of *WeChatAppEx.exe*:
````shell
C:\Users\$USERNAME\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\WMPFRuntime\$RANDOM_NUMBER\extracted\runtime\WeChatAppEx.exe
````
- Note: find all WeChatAppEx.exe in every `$RANDOM_NUMBER` folder.

token is here:
![img.png](src/img.png)