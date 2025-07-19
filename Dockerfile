# 使用 Python 官方镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt ./

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 设置环境变量（可选）
ENV FLASK_APP=server.py

# 启动 Flask 服务（监听 0.0.0.0:10000 端口）
CMD ["python", "server.py"]
