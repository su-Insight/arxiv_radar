# ArXiv Radar

ArXiv Radar是一个自动化工具，用于每日从ArXiv检索最新论文，使用本地LLM解析摘要，计算与用户定义关键字的相似度，并将最相关的前K篇论文通过邮件发送给用户。

## 功能特点

- 📚 **每日更新**：自动从ArXiv获取过去24小时内的最新论文
- 🔍 **智能检索**：支持多关键字/短语检索，可选择ArXiv分类
- 🧠 **本地LLM**：使用本地部署的LLM解析和理解论文摘要，保护隐私
- ⚡ **相似度计算**：基于余弦相似度算法筛选最相关的论文
- 📧 **邮件推送**：将筛选后的论文列表发送到指定邮箱
- ⏰ **定时执行**：可配置的每日执行时间
- 📁 **轻量级设计**：仅包含4个核心文件，易于部署和使用

## 项目结构

```
arxiv_radar/
├── main.py          # 主程序文件，包含所有核心逻辑
├── config.py        # 配置文件，管理所有参数
├── requirements.txt # 依赖库列表
├── README.md        # 项目说明文档
└── arxiv_radar.log  # 运行日志（自动生成）
```

## 安装步骤

### 1. 环境要求

- Python 3.7+
- 足够的磁盘空间（用于存储LLM模型，约100MB-2GB，取决于模型大小）

### 2. 安装依赖

```bash
# 安装项目依赖
pip install -r requirements.txt
```

## 配置说明

编辑`config.py`文件，设置以下关键参数：

### 1. 核心配置

```python
# 搜索关键字列表（必填）
keywords = ["machine learning", "artificial intelligence", "deep learning"]

# ArXiv分类筛选（可选，留空表示不限制）
# 常用分类示例：cs.AI, cs.CL, cs.CV, cs.LG, stat.ML
arxiv_categories = []

# 每次最多获取的论文数量
max_papers = 100

# 发送前K篇最相关论文
top_k = 10
```

### 2. LLM模型配置

```python
# 本地LLM模型名称或路径
# 推荐模型：
# - 小型模型（适合低配置设备）: all-MiniLM-L6-v2, distilbert-base-nli-stsb-mean-tokens
# - 中型模型: all-mpnet-base-v2
# - 大型模型: all-roberta-large-v1
llm_model = "all-MiniLM-L6-v2"
```

### 3. 邮件发送配置

```python
# 发件人邮箱
email_sender = "your_email@example.com"

# 收件人邮箱（可以与发件人相同）
email_receiver = "your_email@example.com"

# SMTP服务器设置
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_tls = True  # 是否使用TLS加密

# SMTP登录凭据（如果需要）
smtp_username = "your_email@example.com"
smtp_password = "your_email_password"
```

### 4. 调度配置

```python
# 每日执行时间（24小时制）
schedule_time = "09:00"
```

## 运行方式

### 单次运行

```bash
python main.py
```

### 后台持续运行

```bash
# Linux/Mac
nohup python main.py > output.log 2>&1 &

# Windows（使用PowerShell）
Start-Process python -ArgumentList "main.py" -WindowStyle Hidden
```

## 常见问题

### 1. 无法连接到SMTP服务器

**解决方案**：
- 检查SMTP服务器地址和端口是否正确
- 确认是否启用了TLS/SSL加密
- 验证邮箱用户名和密码是否正确
- 对于Gmail用户，需要启用"不太安全的应用访问"或使用应用专用密码

### 2. 模型加载失败

**解决方案**：
- 检查网络连接，确保能够下载模型
- 尝试使用更小的模型（如all-MiniLM-L6-v2）
- 手动下载模型并指定本地路径

### 3. 没有找到相关论文

**解决方案**：
- 检查关键字是否正确，尝试使用更广泛的关键字
- 减少ArXiv分类限制
- 增加max_papers参数值

### 4. 运行速度慢

**解决方案**：
- 使用更小的LLM模型
- 减少max_papers参数值
- 考虑在有GPU的环境中运行（sentence-transformers支持GPU加速）

## 技术栈

- **Python 3.7+**：主要开发语言
- **arxiv**：ArXiv API客户端
- **sentence-transformers**：本地LLM和文本嵌入生成
- **scikit-learn**：相似度计算
- **schedule**：定时任务调度
- **smtplib**：邮件发送

## 扩展建议

- 添加论文PDF自动下载功能
- 支持更多学术论文来源（如IEEE Xplore、ACM Digital Library等）
- 实现Web界面用于配置管理
- 添加论文分类和主题聚类功能
- 支持多用户配置

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### v1.0.0 (2024-01-15)
- 初始版本发布
- 实现核心功能：ArXiv检索、本地LLM解析、相似度计算、邮件发送和定时调度

---

**注意**：首次运行时，程序会自动下载指定的LLM模型到本地`./models`目录，请确保网络连接正常。