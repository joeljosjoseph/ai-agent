from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from google import genai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# llm = ChatOpenAI()
llm = genai.Client()
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder","{chat_history}"),
        ("human","{query}"),
        {"placeholder","{agent_scratchpad}"}
    ]
).partial(format_instructions=parser.get_format_instructions())

interaction = llm.interactions.create(
    model="gemini-flash-latest",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)