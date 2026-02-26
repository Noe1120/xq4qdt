import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from tools import create_langchain_tools
from llm_manager import LLMManager

load_dotenv()

class SimpleAgent:
    def __init__(self):
        self.llm_manager = LLMManager()
        self.llm = self.llm_manager.llm
        self.tools = create_langchain_tools()
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.agent = initialize_agent(
    tools=self.tools,
    llm=self.llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=self.memory,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=3,                # 尝试 3 次
    early_stopping_method="generate" # 如果无法解析，直接生成回答
)

    def run(self, query: str) -> str:
        try:
            return self.agent.run(query)
        except Exception as e:
            return f"Agent执行出错：{str(e)}"

    def chat_mode(self):
        print("=== 简单Agent聊天模式 ===")
        print("输入 '退出' 或 'quit' 结束对话")
        print("可用功能：天气查询、文件读取、计算器、时间查询等")
        print("=" * 50)
        while True:
            try:
                user_input = input("\n你: ").strip()
                if user_input.lower() in ['退出', 'quit', 'exit']:
                    print("再见！")
                    break
                if not user_input:
                    continue
                print("Agent思考中...")
                response = self.run(user_input)
                print(f"Agent: {response}")
            except KeyboardInterrupt:
                print("\n程序被中断")
                break

agent = SimpleAgent()