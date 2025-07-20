#!/bin/bash

# 生成动态flag
if [ -z "$GZCTF_FLAG" ]; then
    FLAG="FLAG{$(cat /proc/sys/kernel/random/uuid)}"
fi
echo "$GZCTF_FLAG" > /var/www/html/flag.txt

# 运行Python压缩脚本
python3 /scripts/generate_zips.py

# 启动Apache
apache2-foreground