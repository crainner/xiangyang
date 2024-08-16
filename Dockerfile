# 使用Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 创建存储库目录（可选，实际运行时可以通过挂载本地目录实现）
RUN mkdir -p /app/cc1 /app/cc2 /app/cc3 /app/cc4

# 运行Python脚本
CMD ["python", "xiangyangmovie.py"]
