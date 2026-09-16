# agent.py
# 规则式 Agent：决定用哪个工具，执行工具，写日志

import os
from datetime import datetime
from tools import TOOLS


def log_interaction(user_input, tool_name, result):
    """
    把每次交互写入 logs/agent.log
    """
    os.makedirs("logs", exist_ok=True)

    with open("logs/agent.log", "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] 输入：{user_input} | 工具：{tool_name} | 输出：{result}\n")


def select_tool(user_input: str):
    """
    根据关键词选择工具。
    优先匹配更长的关键词，避免“待办”抢走“查看待办”。
    """
    candidates = []

    for name, info in TOOLS.items():
        for kw in info["keywords"]:
            if kw in user_input:
                candidates.append((len(kw), name, kw))

    if not candidates:
        return None

    candidates.sort(reverse=True)
    return candidates[0][1]


def extract_args(user_input: str, tool_name: str):
    """
    从用户输入里提取工具需要的参数。
    规则式做法：去掉关键词，剩下的就是参数。
    """
    if tool_name == "calculator":
        for kw in TOOLS["calculator"]["keywords"]:
            if kw in user_input:
                return {"expression": user_input.replace(kw, "", 1).strip()}
        return {"expression": user_input.strip()}

    if tool_name == "get_weather":
        for kw in TOOLS["get_weather"]["keywords"]:
            if kw in user_input:
                return {"city": user_input.replace(kw, "", 1).strip()}
        return {"city": user_input.strip()}

    if tool_name == "add_todo":
        for kw in TOOLS["add_todo"]["keywords"]:
            if kw in user_input:
                return {"content": user_input.replace(kw, "", 1).strip()}
        return {"content": user_input.strip()}

    if tool_name == "list_todos":
        return {}

    return {}


def run_agent(user_input: str):
    """
    Agent 主入口：选择工具 → 提取参数 → 执行工具 → 记录日志 → 返回结果
    """
    tool_name = select_tool(user_input)

    if tool_name is None:
        result = "我还不会这个。试试：计算 1+1、天气 北京、记一下 明天买牛奶、查看待办"
        log_interaction(user_input, "none", result)
        return result

    args = extract_args(user_input, tool_name)

    try:
        result = TOOLS[tool_name]["fn"](**args)
    except Exception as e:
        result = f"工具执行出错：{e}"

    log_interaction(user_input, tool_name, result)
    return result