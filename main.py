# main.py

from agent import run_agent


def main():
    print("=" * 40)
    print("个人助理 Agent v0.2（规则式）")
    print("支持：")
    print("  计算 1+1")
    print("  天气 北京")
    print("  记一下 明天买牛奶")
    print("  查看待办")
    print("  退出")
    print("=" * 40)

    while True:
        user_input = input("你：").strip()

        if user_input == "退出":
            print("Agent：再见！")
            break

        if not user_input:
            continue

        result = run_agent(user_input)
        print("Agent：", result)


if __name__ == "__main__":
    main()