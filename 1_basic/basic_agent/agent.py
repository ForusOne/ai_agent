from google.adk.agents import Agent
from . import prompt

root_agent = Agent(
    name = "basic_agent",
    model = "gemini-2.0-flash",
    description = "사용자의 질문에 대한 질문에 답변하는 에이전트",
    instruction = """    
        당신은 한국의 역사에 대한 전문가입니다. 
        사용자의 질문에 자세하게 답변해야 합니다.
        질문은 한국의 역사와 관련된 어떤 것이든 가능합니다.
        역사적인 사실과 함께 년도, 날짜가 포함된 경우에는 그에 대한 정보도 제공해야 합니다.
    """,
)