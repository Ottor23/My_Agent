---
title: Day 01 - 环境搭建与第一个提交
date: 2026-09-14
tags:
  - agent学习
  - day01
  - 项目搭建
status: 进行中
---

# Day 01 - 环境搭建与第一个提交

> [!info] 今日目标
> 能写代码 → 能运行 → 能提交到 GitHub。

## 总进度

- [ ] 完成全部任务
- [ ] 已推送到 GitHub
- [ ] 已写开发日志

---

## 1. 给 VS Code 安装扩展

- [ ] Python（Microsoft）
- [ ] Pylance（通常随 Python 自动安装）
- [ ] Chinese (Simplified) Language Pack
- [ ] GitLens
- [ ] DotENV
- [ ] Markdown All in One
- [ ] 可选：Error Lens
- [ ] 可选：Code Runner
- [ ] 可选：indent-rainbow

> [!tip] 提示
> 不要装一堆 AI 编程插件。今天只装必要的。

---

## 2. 检查 Python 和 Git

- [ ] 打开 VS Code 终端：`终端` → `新建终端`
- [ ] Windows 执行：`py --version`
- [ ] 如果上面不行，再执行：`python --version`
- [ ] Mac 执行：`python3 --version`
- [ ] 执行：`git --version`
- [ ] 确认 Python 3.10+，Git 能显示版本号

---

## 3. 创建项目文件夹

- [ ] 创建文件夹：`my-agent`
- [ ] 在 VS Code 中打开这个文件夹
- [ ] 如果提示“是否信任此文件夹作者”，点击信任

---

## 4. 写第一行代码

- [ ] 新建文件：`main.py`
- [ ] 写入：

```python
print("Hello Agent")
```

- [ ] 点击右上角运行按钮，或在终端运行
- [ ] Windows 运行：`py main.py`
- [ ] Mac 运行：`python3 main.py`
- [ ] 看到输出：`Hello Agent`

---

## 5. 创建项目基础文件

- [ ] 创建 `README.md`
- [ ] 创建 `PRD.md`
- [ ] 创建 `.gitignore`
- [ ] 创建 `logs/day01.md`
- [ ] 按附录模板填入内容

---

## 6. 用 Git 提交代码

- [ ] 设置用户名：

```bash
git config --global user.name "你的名字"
```

- [ ] 设置邮箱：

```bash
git config --global user.email "你的邮箱"
```

- [ ] 初始化仓库：

```bash
git init
```

- [ ] 加入暂存区：

```bash
git add .
```

- [ ] 提交：

```bash
git commit -m "chore: 初始化项目"
```

---

## 7. 上传到 GitHub

- [ ] 注册或登录 GitHub：https://github.com
- [ ] 点右上角 `+` → `New repository`
- [ ] 仓库名写：`my-agent`
- [ ] 不要勾选 `Add a README file`
- [ ] 不要勾选 `.gitignore`
- [ ] 不要选 license
- [ ] 创建仓库后，在终端执行：

```bash
git branch -M main
git remote add origin https://github.com/你的用户名/my-agent.git
git push -u origin main
```

- [ ] 刷新 GitHub 页面
- [ ] 确认能看到：`main.py`、`README.md`、`PRD.md`、`.gitignore`、`logs/day01.md`

---

## 今日验收标准

- [ ] VS Code 装好了 Python、GitLens、Markdown 等扩展
- [ ] 终端能查到 Python 和 Git 版本
- [ ] `main.py` 能运行并输出 `Hello Agent`
- [ ] 创建了 README、PRD、.gitignore、logs/day01.md
- [ ] 代码成功推送到 GitHub

---

## 今天不要做

- [ ] 确认：不接大模型 API
- [ ] 确认：不学 LangChain
- [ ] 确认：不做多 Agent
- [ ] 确认：不追求网页界面
- [ ] 确认：不装几十个插件

---

## 开发日志

- [ ] 今天安装了什么：
- [ ] 遇到什么问题：
- [ ] 怎么解决的：
- [ ] 明天做什么：

---

## 附录：文件内容模板

### README.md

```markdown
# My Agent

这是我的第一个 Agent 项目。

## 目标

- 学习 Python
- 学习项目框架
- 学习 Agent 工作流程
- 学习产品经理的项目管理方式

## 当前进度

- [x] 安装 VS Code 扩展
- [x] 运行 Hello Agent
- [ ] 接入大模型
- [ ] 实现第一个工具
```

### PRD.md

```markdown
# 个人助理 Agent PRD

## 1. 背景

我想通过从 0 做一个 Agent，学习编程、项目开发和产品管理。

## 2. 用户

第一版用户是我自己。

## 3. 使用场景

- 查询天气
- 做数学计算
- 记录待办

## 4. MVP 功能

- 命令行交互
- 支持 3 个工具
- 最多执行 5 步
- 有日志
- 有错误提示

## 5. 非目标

- 不做多 Agent
- 不做网页版
- 不做复杂记忆
- 不接支付

## 6. 成功指标

- 10 个测试任务完成 8 个
- 平均步数少于 3 步
- 工具调用失败时有友好提示
```

### .gitignore

```text
__pycache__/
*.pyc
.env
.venv/
venv/
.vscode/
.DS_Store
```

### logs/day01.md

```markdown
# Day 1 开发日志

## 今天做了什么

- 安装 VS Code 扩展
- 检查 Python 和 Git
- 创建 my-agent 项目
- 运行 Hello Agent
- 创建 README、PRD、.gitignore

## 遇到什么问题

- 

## 怎么解决的

- 

## 明天做什么

- 学习 Python 变量和函数
- 写第一个工具函数
```