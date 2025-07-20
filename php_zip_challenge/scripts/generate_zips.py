import zipfile
import random
import os
import shutil

# 配置参数
FLAG_PATH = '/tmp/flag.txt'
OUTPUT_DIR = '/var/www/html/downloads'
NUM_COMPRESSIONS = random.randint(30, 40)

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 清理旧文件
for f in os.listdir(OUTPUT_DIR):
    file_path = os.path.join(OUTPUT_DIR, f)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"Error cleaning files: {e}")

last_zip_path = None
password = None

# 读取 flag 文件内容
with open(FLAG_PATH, 'r') as f:
    flag_content = f.read()

# 执行多次压缩
for i in range(NUM_COMPRESSIONS):
    # 生成随机文件名
    zip_filename = f"archive_{random.getrandbits(32):08x}.zip"
    zip_path = os.path.join(OUTPUT_DIR, zip_filename)

    try:
        # 创建ZIP文件
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 最后一次压缩添加密码
            if i == NUM_COMPRESSIONS - 1:
                password = str(random.randint(1000, 9999))
                zipf.setpassword(password.encode('utf-8'))
                # 使用 AES 加密
                if hasattr(zipfile, 'ZIP_AES'):
                    info = zipfile.ZipInfo('flag.txt')
                    info.create_system = 3  # Unix 系统
                    info.flag_bits = 0x0008  # 启用加密标志位
                    zipf.writestr(info, flag_content, compress_type=zipfile.ZIP_DEFLATED)
                else:
                    # 兼容旧版本 Python，使用传统加密
                    zipf.writestr('flag.txt', flag_content, compress_type=zipfile.ZIP_DEFLATED)
            else:
                zipf.write(FLAG_PATH, arcname='flag.txt', compress_type=zipfile.ZIP_DEFLATED)

        # 保留最后一个ZIP文件的路径
        if last_zip_path and os.path.exists(last_zip_path):
            os.remove(last_zip_path)
        last_zip_path = zip_path

    except Exception as e:
        print(f"Compression error: {e}")
        if os.path.exists(zip_path):
            os.remove(zip_path)

# 创建符号链接方便访问
if last_zip_path:
    symlink_path = os.path.join(OUTPUT_DIR, 'encrypted_flag.zip')
    if os.path.exists(symlink_path):
        os.remove(symlink_path)
    os.symlink(last_zip_path, symlink_path)

# 保存密码到日志（供题目管理员参考）
if password:
    with open('/scripts/zip_password.log', 'w') as f:
        f.write(f"{password}\n")

print(f"Successfully generated {NUM_COMPRESSIONS} zip files. Last one: {last_zip_path}")

# 生成加密的 flag.zip
password = ''.join(random.choices('0123456789', k=4))
with open('/tmp/flag.txt', 'w') as f:
    f.write(flag_content)

# 使用 pyminizip 创建加密 ZIP（替换原有的 zipfile 代码）
import pyminizip  # 添加 pyminizip 导入

pyminizip.compress(
    '/tmp/flag.txt',       # 源文件路径
    None,                  # 无额外文件
    '/var/www/html/downloads/encrypted_flag.zip',  # 输出路径
    password,              # 4位数字密码
    9                      # 压缩级别
)