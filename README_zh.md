<p align="center">
   <a href="" rel="noopener">
  <img width=200px height=200px src="https://via.placeholder.com/200?text=ARXIV+RADAR" alt="logo"></a>
 </p>
 
 <h3 align="center">ArXiv Radar</h3>
 
 <p align="center">
   <a href="README.md" target="_blank">English Version</a>
 </p>
 
 <div align="center">
 
   ![Status](https://img.shields.io/badge/status-active-success.svg)
   ![Stars](https://img.shields.io/github/stars/yourusername/arxiv_radar?style=flat)
   ![Issues](https://img.shields.io/github/issues/yourusername/arxiv_radar)
   ![Pull Requests](https://img.shields.io/github/issues-pr/yourusername/arxiv_radar)
   ![License](https://img.shields.io/github/license/yourusername/arxiv_radar)
 
 </div>

 <p align="center"> 根据您的研究兴趣，每日自动检索和排序 ArXiv 论文。 
     <br>  
 </p>
 
 > [!IMPORTANT]
 > 请关注此仓库，及时合并上游更新，以享受新功能和修复的 bug。
 
 ## 🧐 关于 <a name = "about"></a>
 
 > 以最小的努力了解您领域的最新研究进展！
 
 *ArXiv Radar* 是一个自动化工具，每天检索最新的 ArXiv 论文，使用本地 LLM 分析它们与您定义的兴趣的相关性，并将最相关的论文直接发送到您的邮箱。它可以作为 GitHub Actions 工作流部署，具有 **零成本**、**无需安装** 和 **最少配置** 的特点，支持每日自动交付。
 
 ## ✨ 功能特性
 
 - **完全免费**：所有计算在 GitHub Actions 配额内本地运行（针对公共仓库）。
 - **AI 生成的 TL;DR**：论文的快速摘要，帮助您决定阅读哪些论文。
 - **论文相关性排序**：根据与您研究兴趣的相似度对论文进行排序。
 - **多兴趣支持**：跟踪多个研究领域的论文。
 - **自动邮件发送**：直接在收件箱中获取每日更新。
 - **轻量级设计**：易于部署和配置，设置最少。
 - **本地 LLM 支持**：使用本地语言模型保护您的隐私。
 - **可选的 LLM API 支持**：使用云 LLM API（如 OpenAI）获取高级功能。
 - **可定制搜索**：定义您自己的 ArXiv 查询和兴趣领域。

 ## 📷 截图
 
 ![screenshot](https://via.placeholder.com/800x600?text=ArXiv+Radar+邮件截图)
 
 ## 🚀 使用方法
 
 ### 快速开始
 
 1. Fork（并 star 😉）此仓库。

 2. 设置 GitHub Action 密钥和变量。
 
 以下是您需要设置的所有密钥。设置后，它们对任何人（包括您自己）都是不可见的，以确保安全。
 
 | 密钥 | 必填 | 类型 | 描述 | 示例 |
 | :--- | :---: | :---  | :---  | :--- |
 | ARXIV_QUERY | ✅ | str  | 目标 ArXiv 论文的分类。使用 `+` 连接多个分类。 | cs.AI+cs.CV+cs.LG+cs.CL |
 | SMTP_SERVER | ✅ | str | 发送邮件的 SMTP 服务器。 | smtp.qq.com |
 | SMTP_PORT | ✅ | int | SMTP 服务器的端口。 | 465 |
 | SENDER | ✅ | str | 发送邮件的邮箱账户。 | your_email@example.com |
 | RECEIVER | ✅ | str | 接收论文列表的邮箱地址。 | your_email@example.com |
 | SENDER_PASSWORD | ✅ | str | 发送者账户的密码或授权码。 | your_password |
 | USE_LLM_API | ✅ | bool | 是否使用 OpenAI API (true/false)。 | false |
 | OPENAI_API_KEY | | str | OpenAI API 密钥（如果 USE_LLM_API 为 true 则必填）。 | sk-xxxxxxxx |
 | OPENAI_API_BASE | | str | OpenAI API 基础 URL（可选）。 | https://api.openai.com/v1 |
 | MODEL_NAME | | str | OpenAI 模型名称（可选，默认：gpt-4o）。 | gpt-4o |
 
 **仓库变量**（公开，易于编辑）：
 
 | 变量 | 必填 | 类型 | 描述 | 示例 |
 | :--- | :---  | :---  | :--- | :--- |
 | REPOSITORY | | str | 仓库名称（默认：yourusername/arxiv_radar）。 | yourusername/arxiv_radar |
 | REF | | str | 分支名称（默认：main）。 | main |
 | SEND_EMPTY | | bool | 当没有找到论文时是否发送空邮件（true/false）。 | false |
 | MAX_PAPER_NUM | | int | 推荐的最大论文数量。 | 50 |
 | RETRIEVER_TARGET | | str | 兴趣领域，每行一个。 | 机器学习<br>人工智能 |
 | LANGUAGE | | str | TLDR 生成的语言（默认：English）。 | Chinese |
 
 3. 手动触发工作流进行测试：
 
 转到您 fork 的仓库中的 Actions 选项卡，手动运行工作流。
 
 > [!NOTE]
 > 工作流将在每日计划时间自动运行。您也可以随时手动触发它。
 
 ## ⚙️ 配置
 
 ### 兴趣目标
 
 在 `RETRIEVER_TARGET` 变量中定义您的研究兴趣，每行一个：
 
 ```
 机器学习
 深度学习
 自然语言处理
 计算机视觉
 ```
 
 ### ArXiv 查询
 
 在 `ARXIV_QUERY` 密钥中自定义您的 ArXiv 搜索查询：
 
 - 使用来自 [ArXiv 分类法](https://arxiv.org/category_taxonomy) 的分类缩写
 - 使用 `+` 连接多个分类
 - 示例：`cs.AI+cs.CV+cs.LG+cs.CL`
 
 ## 🛠️ 技术栈
 
 - **Python 3.7+**：主要开发语言
 - **arxiv**：ArXiv API 客户端
 - **llama_cpp**：本地 LLM 集成
 - **openai**：OpenAI API 集成（可选）
 - **sentence-transformers**：文本嵌入生成
 - **scikit-learn**：相似度计算
 - **schedule**：定时任务管理
 - **smtplib**：邮件发送
 - **GitHub Actions**：持续集成和部署
 
 ## � 调试与测试

### 测试工作流
我们提供了一个专门的 **Test-Workflow Action**，用于快速测试配置是否正确：
- 无论日期如何，始终检索5篇ArXiv论文
- 适合调试配置和查看邮件格式
- 不影响日常自动运行的主工作流

### 主工作流
- **自动触发**：每天自动运行，检索前一天发布的新论文
- **默认时间**：UTC时间22:00执行
- **自定义时间**：可通过编辑 `.github/workflows/main.yml` 文件修改运行时间
- **周末和节假日**：这些时间段ArXiv通常不发布新论文，可能会在日志中看到"未找到新论文"的提示

## 💻 本地运行

如果您希望在本地运行此工具，可以使用uv包管理器（推荐）：

```bash
# 设置环境变量
export ARXIV_QUERY=cs.AI+cs.CV+cs.LG
export SMTP_SERVER=smtp.example.com
# ... 设置其他必要的环境变量

# 运行项目
cd arxiv_radar
uv run main.py
```

> ⚠️ **注意**：其他包管理器（如pip或conda）未经过全面测试，可能存在潜在问题。虽然项目包含pyproject.toml文件，但建议优先使用uv以获得最佳体验。

## 📦 LLM资源需求

- 系统将自动下载并运行 **Qwen2.5-3B** 模型（约3GB大小）
- 请确保您的网络连接稳定，能够下载该模型
- 硬件需满足模型运行需求（至少8GB内存）

## � 保持同步

项目处于**活跃开发**状态，建议您：
1. **Watch** 此仓库以获取最新发布通知
2. 定期更新您的fork仓库以享受新功能和bug修复

## 🧠 工作原理

ArXiv Radar的工作流程分为以下几个步骤：
1. **数据收集**：从ArXiv检索最新论文
2. **兴趣匹配**：使用本地LLM分析论文摘要与您定义兴趣的相关性
3. **排序**：根据相关性分数对论文进行排序
4. **摘要生成**：使用轻量级LLM为每篇论文生成TL;DR
5. **邮件发送**：将排序后的论文列表发送到您的邮箱

## ⚠️ 已知限制

1. **推荐算法**：当前的相关性计算基于简单的相似度算法，可能无法完全准确地反映您的兴趣偏好
2. **执行时间**：在GitHub Actions上部署LLM并为每篇论文生成摘要需要一定时间（约70秒/篇）
3. **资源限制**：GitHub Actions有执行时间限制（公共仓库每执行6小时，每月2000分钟）

## 🤝 贡献

欢迎提交Issue和Pull Request！我们鼓励：
- 改进推荐算法
- 添加新功能
- 修复bug
- 优化文档

> 💡 **提示**：所有Pull Request请合并到dev分支

## 📝 许可证

项目采用 **MIT许可证** 分发，详情请参阅[LICENSE](LICENSE)文件。

## 🙏 致谢

感谢以下项目和工具的支持：
- [arxiv](https://github.com/lukasschwab/arxiv.py) - ArXiv API客户端
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) - 本地LLM支持
- [sentence-transformers](https://github.com/UKPLab/sentence-transformers) - 文本嵌入生成
- [GitHub Actions](https://github.com/features/actions) - 自动化工作流支持

--- 

**开始使用ArXiv Radar，让最新的研究成果自动找到您！** 🚀