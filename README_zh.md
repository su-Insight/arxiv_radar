# ArXiv Radar

[English Version](README.md)

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
├── main.py                  # 主程序文件，包含所有核心逻辑
├── src/
│   ├── llm.py              # LLM相关函数和工具
│   ├── paper.py            # 论文数据结构和ArXiv API交互
│   ├── rerank.py           # 使用LLM的论文重新排序逻辑
│   └── construct_email.py  # 邮件构建和发送函数
├── requirements.txt         # 依赖列表
├── README.md               # 项目文档（英文）
├── README_zh.md            # 项目文档（中文）
└── .github/
    └── workflows/          # GitHub Actions工作流
        └── main.yml        # 每日执行工作流
```

## 安装步骤

### 1. 环境要求

- Python 3.7+
- 足够的磁盘空间（用于存储LLM模型，根据模型大小约100MB-2GB）

### 2. 安装依赖

```bash
# 安装项目依赖
pip install -r requirements.txt
```

## 配置

### 1. GitHub Actions Secrets 和 Variables

在您的GitHub仓库中配置以下secrets和variables：

**Secrets：**
- `ARXIV_QUERY`：ArXiv搜索查询
- `SMTP_SERVER`：SMTP服务器地址
- `SMTP_PORT`：SMTP服务器端口
- `SENDER`：发送者邮箱地址
- `RECEIVER`：接收者邮箱地址
- `SENDER_PASSWORD`：发送者邮箱密码
- `USE_LLM_API`：是否使用OpenAI API (true/false)
- `OPENAI_API_KEY`：OpenAI API密钥（如果USE_LLM_API为true则必需）
- `OPENAI_API_BASE`：OpenAI API基础URL（可选）
- `MODEL_NAME`：OpenAI模型名称（可选，默认：gpt-4o）

**Variables：**
- `REPOSITORY`：仓库名称（默认：您的GitHub用户名/arxiv_radar）
- `REF`：分支名称（默认：main）
- `SEND_EMPTY`：当没有找到论文时是否发送空邮件 (true/false)
- `MAX_PAPER_NUM`：推荐的最大论文数量
- `RETRIEVER_TARGET`：兴趣领域，每行一个
- `LANGUAGE`：TLDR生成的语言（默认：English）

## 使用方法

### 本地运行

```bash
python main.py
```

### GitHub Actions（推荐）

1. Fork此仓库
2. 按照上述说明配置secrets和variables
3. 工作流将在每天的计划时间自动运行

## 故障排除

### 1. 无法连接到SMTP服务器

**解决方案：**
- 检查SMTP服务器地址和端口是否正确
- 确保TLS/SSL加密已正确配置
- 验证邮箱用户名和密码
- 对于Gmail用户，启用"Less secure app access"或使用应用专用密码

### 2. 模型加载失败

**解决方案：**
- 检查网络连接，确保模型可以下载
- 尝试使用较小的模型
- 手动下载模型并指定本地路径

### 3. 未找到相关论文

**解决方案：**
- 检查关键字是否正确，尝试使用更广泛的关键字
- 减少ArXiv分类限制
- 增加`MAX_PAPER_NUM`参数值

### 4. 执行速度慢

**解决方案：**
- 使用较小的LLM模型
- 减少`MAX_PAPER_NUM`参数值
- 考虑在具有GPU的环境中运行（sentence-transformers支持GPU加速）

## 技术栈

- **Python 3.7+**：主要开发语言
- **arxiv**：ArXiv API客户端
- **llama_cpp**：本地LLM集成
- **openai**：OpenAI API集成（可选）
- **sentence-transformers**：文本嵌入生成
- **scikit-learn**：相似度计算
- **schedule**：定时任务管理
- **smtplib**：邮件发送
- **GitHub Actions**：持续集成和部署

## 许可证

MIT许可证

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### v1.0.0 (2024-01-15)
- 初始版本发布
- 实现了核心功能：ArXiv检索、本地LLM解析、相似度计算、邮件发送和定时执行

---

**注意**：首次运行时，程序会自动将指定的LLM模型下载到本地`./models`目录。请确保网络连接可用。