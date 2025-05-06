from google.adk.agents import Agent
from . import prompt

root_agent = Agent(
    name = "basic_agent",
    model = "gemini-2.0-flash",
    description = "Agent to answer questions about user's questions",
    instruction = prompt.INSTRUCTION,
)