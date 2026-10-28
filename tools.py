
from langchain_community.tools import (
    DuckDuckGoSearchRun,
    WikipediaQueryRun,
)
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool

search = DuckDuckGoSearchRun()

wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper()
)


@tool
def search_tool(query: str) -> str:
    """Search the web for information relevant to a research question."""
    return search.run(query)


tools = [search_tool, wikipedia]
