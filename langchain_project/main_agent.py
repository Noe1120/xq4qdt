from agent import agent

def main():
    # # 测试单个查询
    # print("=== 测试单个查询 ===")
    # test_queries = [
    #     "北京现在的天气怎么样？",
    #     "计算 15 * 3 + 8 等于多少？",
    #     "现在是什么时间？",
    #     "读取当前目录下的 test.txt 文件",
    #     "你好，请介绍一下你自己"
    # ]
    # for query in test_queries:
    #     print(f"\n你: {query}")
    #     response = agent.run(query)
    #     print(f"Agent: {response}")

    # 启动聊天模式
    print("\n" + "="*50)
    agent.chat_mode()

if __name__ == "__main__":
    main()