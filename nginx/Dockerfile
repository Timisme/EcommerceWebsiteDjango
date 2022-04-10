FROM nginx

# COPY index.html /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf 
COPY my_nginx.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]

# 為何用 nginx -g daemon off 啟動 nginx?
# 不用一般 /etc/init.d/nginx start？
# 要讓 Nginx 一直保持服務，否則 Container 會退出並且停止。