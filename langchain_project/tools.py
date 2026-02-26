import os
from datetime import datetime
from langchain.tools import Tool

class CustomTools:
    @staticmethod
    def get_weather(city: str) -> str:
        """模拟天气查询"""
        weather_data = {
            "北京": {"temperature": "15°C", "condition": "晴", "humidity": "40%"},
            "上海": {"temperature": "18°C", "condition": "多云", "humidity": "65%"},
            "广州": {"temperature": "25°C", "condition": "阴", "humidity": "80%"}
        }
        if city in weather_data:
            w = weather_data[city]
            return f"{city}的天气：温度{w['temperature']}，{w['condition']}，湿度{w['humidity']}"
        return f"未找到{city}的天气信息"

    @staticmethod
    def read_file(filename: str) -> str:
        """读取文件内容"""
        try:
            if not os.path.exists(filename):
                return f"文件 {filename} 不存在"
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                return f"文件 {filename} 的内容：\n{content[:500]}"
        except Exception as e:
            return f"读取文件时出错：{str(e)}"

    @staticmethod
    def get_current_time() -> str:
        """获取当前时间"""
        now = datetime.now()
        return now.strftime("当前时间：%Y年%m月%d日 %H:%M:%S")

    @staticmethod
    def calculator(expression: str) -> str:
        """简单计算器"""
        try:
            # 安全评估表达式（仅限简单运算）
            result = eval(expression, {"__builtins__": {}}, {})
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算错误：{str(e)}"
        
    @staticmethod
    def create_note(content: str, filename: str = "note.txt") -> str:
        """创建笔记文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"创建时间：{datetime.now()}\n")
                f.write(f"内容：{content}\n")
            return f"笔记已保存到 {filename}"
        except Exception as e:
            return f"创建笔记失败：{str(e)}"

    @staticmethod
    def list_files() -> str:
        """列出当前目录文件"""
        try:
            files = os.listdir('.')
            txt_files = [f for f in files if f.endswith('.txt')]
            py_files = [f for f in files if f.endswith('.py')]
            result = "当前目录文件：\n"
            if txt_files:
                result += f"文本文件：{', '.join(txt_files)}\n"
            if py_files:
                result += f"Python文件：{', '.join(py_files)}\n"
            return result
        except Exception as e:
            return f"列出文件失败：{str(e)}"

def create_langchain_tools() -> list:
    custom = CustomTools()
    tools = [
        Tool(name="天气查询", func=custom.get_weather,
             description="查询城市的天气信息。输入：城市名称"),
        Tool(name="文件读取", func=custom.read_file,
             description="读取文件的内容。输入：文件路径"),
        Tool(name="当前时间", func=custom.get_current_time,
             description="获取当前日期和时间"),
        Tool(name="计算器", func=custom.calculator,
             description="执行数学计算。输入：数学表达式，如 '2 + 3 * 4'"),
        # 下面是新增的两个工具
        Tool(name="创建笔记", func=custom.create_note,
             description="创建笔记文件。输入：笔记内容，可选文件名"),
        Tool(name="列出文件", func=custom.list_files,
             description="列出当前目录下的文件")
    ]
    return tools