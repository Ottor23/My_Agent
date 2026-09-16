import os
#工具函数存放

#计算简单算式
def calculator (expression: str)->str:
    try:
        result=eval(expression,{"__builtins__":{}},{})
        return f"计算结果是：{result}"
    except Exception as e:
        return f"计算错误：{e}"

#获取储存的天气数据
def get_weather (city:str)->str:
    weather_Info={
        "北京":"晴天",
        "上海":"阴天",
        "广州":"多云",
        "深圳":"小雨",
    }
    if city in weather_Info:
        return f"{city}的天气为：{weather_Info}"
    return f"未找到{city}的天气数据"

def add_todo (content:str)->str:
    if not content:
        return f"内容不能能为空"
    with open ("todos.txt", "a", encoding="utf-8") as f:
        f.write(content+"\n")
    return f"已记录待办： {content}"

def list_todos()->str:
    if not os.path.exists("todos.txt"):
        return "暂无待办。"
    with open("todos.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        return "暂无待办。"

    result = "待办列表：\n"
    for i, line in enumerate(lines, 1):
        result += f"{i}. {line}\n"

    return result.strip()

TOOLS = {
    "calculator": {
        "fn": calculator,
        "desc": "计算数学表达式",
        "keywords": ["计算", "算", "等于"],
        "args": ["expression"],
    },
    "get_weather": {
        "fn": get_weather,
        "desc": "查询城市天气",
        "keywords": ["天气", "气温"],
        "args": ["city"],
    },
    "add_todo": {
        "fn": add_todo,
        "desc": "添加待办事项",
        "keywords": ["记一下", "提醒我", "添加待办", "待办"],
        "args": ["content"],
    },
    "list_todos": {
        "fn": list_todos,
        "desc": "查看待办事项",
        "keywords": ["查看待办", "待办列表", "我的待办"],
        "args": [],
    },
}
    


