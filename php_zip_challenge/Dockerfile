FROM php:7.4-apache
RUN apt-get update && apt-get install -y python3 python3-pip john wget && rm -rf /var/lib/apt/lists/*
RUN pip3 install pyminizip
WORKDIR /var/www/html

# 安装依赖（已修复python3-zipfile问题）
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pyminizip  # 添加 pyminizip 安装

# 复制代码和脚本
COPY src/ /var/www/html/
COPY scripts/ /scripts/
RUN chmod +x /scripts/*.sh /scripts/*.py

# 配置Apache
RUN a2enmod rewrite
EXPOSE 80

CMD ["/scripts/start.sh"]