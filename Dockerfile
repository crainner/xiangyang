# 使用 Python 3.9 的基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制应用程序文件到容器中
COPY generate_document.py import_to_db.py app.py directories.txt ./

# 安装 Flask 和 requests
RUN pip install flask requests

# 创建存储库目录（可选，实际运行时可以通过挂载本地目录实现）
RUN mkdir -p /app/cc1 /app/cc2 /app/cc3 /app/cc4

# 生成目录文档
RUN python generate_document.py

# 创建数据库并导入数据
RUN python import_to_db.py

# 暴露应用程序端口
EXPOSE 5000

# 运行 Flask 应用程序
CMD ["python", "app.py"]
