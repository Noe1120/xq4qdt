from llm_manager import llm_manager

print("=== 简单问答 ===")
response = llm_manager.simple_question("什么是Python？")
print(response)

print("\n=== 模板问答 ===")
template = """
请根据以下信息回答问题：
用户信息：
姓名：{name}
年龄：{age}
职业：{job}
问题：{question}
"""
response = llm_manager.formatted_response(
    template,
    name="李华",
    age=28,
    job="数据分析师",
    question="我应该学习哪些技能？"
)
print(response)