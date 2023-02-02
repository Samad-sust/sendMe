## === SendMe: Solution for submitting assignments/exam paper online ===

### + Declare permanat environmental variable (variable name is given after some lines)


### + Install dependencies 

`
pip install -r requirement.txt
`

### + sendMe Environmental Variable name 

+ in production: SEND_ME_DEVELOPMENT_MODE
+ in local PC:  SEND_ME_DEVELOPMENT_MODE
+ in systemd: SEND_ME_DEVELOPMENT_MODE


### + bash file for the gunicorn
```
/home/samad/websites/django/sendme/prod_server_bin/start-sendme-server.sh
```

### + the gunicorn config

```
cd /home/samad/websites/django/sendme
source venvSendme/bin/activate
cd sendMe
gunicorn sendMe.wsgi

```

### Gunicorn service name in the /etc/systemd
```
sendme-gunicorn.service
```


### sites-available/sendme

#### file location: /etc/nginx/sites-available/sendme 


```

upstream django {
  server 127.0.0.1:8000;
}

  server {
    listen 8052;
    location /static/ {
      root /var/www/djago_files/sendme;
      try_files $uri =404;
    }
    
    location /media/ {
      root /var/www/djago_files/sendme;
      try_files $uri =404;
    }
    
    location / {
      try_files $uri @send_to_django;
    }

    location @send_to_django{
      proxy_set_header Host $http_host;
      proxy_redirect off;
      proxy_pass http://django;
    }

  }
  
 ```

### system created for gunicorn so that it can automatically be startted

file location: cat /etc/systemd/system/sendme-gunicorn.service 


```

[Unit]
Description=Gunicorn server for sendme website
After=network.target


[Service]
Type=simple
User=samad
ExecStart=/bin/bash /home/samad/websites/django/sendme/prod_server_bin/start-sendme-server.sh
Environment="SEND_ME_DEVELOPMENT_MODE=prod"
Restart=on-failure

[Install]
WantedBy=multi-user.target

```
