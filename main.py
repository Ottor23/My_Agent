# main.py

from tools import calculator, get_weather
#从tools代码中获取两个工具函数

def main():
    print("=" * 30)
    print("个人助理 Agent v0.1")
    print("支持：")
    print("  计算 1+1")
    print("  天气 北京")
    print("  退出")
    print("=" * 30)
#输入一段前置文字背景信息
    while True:
        user_input = input("你：").strip()
#.strip 去掉输入文字的前后空格
        if user_input == "退出":
            print("Agent：再见！")
            break

        if "计算" in user_input:
            expression = user_input.replace("计算", "", 1).strip()
#.replace("str1","str2",num) 把输入信息中第num次出现的str1替换为str2
            result = calculator(expression)
            print("Agent：", result)

        elif "天气" in user_input:
            city = user_input.replace("天气", "", 1).strip()
            result = get_weather(city)
            print("Agent：", result)

        else:
            print("Agent：我还不会这个。试试：计算 1+1 或 天气 北京")


if __name__ == "__main__":
    main()
#更好的编译main函数的方法