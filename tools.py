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