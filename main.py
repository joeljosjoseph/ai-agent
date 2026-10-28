
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.agents import create_agent

load_dotenv()


# 1. Define the expected response structure
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


# 2. Create the agent
agent = create_agent(
    model="google_genai:gemini-flash-latest",
    tools=[],
    system_prompt=(
        "You are a research assistant that helps generate research papers. "
        "Answer the user's query clearly and accurately. "
        "Include sources only when you can identify them reliably. "
        "List tools actually used; do not claim to use tools that were not used."
    ),
    response_format=ResearchResponse,
)


# 3. Run the agent
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the capital of the UAE?",
            }
        ]
    }
)


# 4. Access the validated Pydantic response
research = result["structured_response"]

print(research)
# print(research.topic)
# print(research.summary)
# print(research.sources)
# print(research.tools_used)
