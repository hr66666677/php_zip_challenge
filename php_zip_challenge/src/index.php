<?php
$zipFile = 'downloads/encrypted_flag.zip';
?>
<html>
<head>
    <title>安全文件下载</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .container { background-color: #f5f5f5; padding: 20px; border-radius: 5px; }
        a.download-btn { display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 4px; margin-top: 10px; }
        a.download-btn:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <div class="container">
        <h1>机密文件下载</h1>
        <p>注意：文件已使用<strong>4位纯数字密码</strong>加密，请输入密码解压</p>
        <?php if (file_exists($zipFile)): ?>
            <p>下载加密文件:</p>
            <a href="<?php echo htmlspecialchars($zipFile); ?>" class="download-btn">下载 encrypted_flag.zip</a>
        <?php else: ?>
            <p style="color: red;">错误: 文件未找到或生成失败</p>
        <?php endif; ?>
    </div>
</body>
</html>