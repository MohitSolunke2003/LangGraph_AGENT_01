import os
from dotenv import load_dotenv
from typing import Annotated, Optional
from langchain_core import messages
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from pydantic import Field, SecretStr
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage # <<< Add these imports


load_dotenv()


# Create a custom ChatOpenAI class to integrate with OpenRouter for opensource and free of cost 
class ChatOpenRouter(ChatOpenAI):
    openai_api_key: Optional[SecretStr] = Field(
        alias="api_key",
        default_factory=SecretStr,
    )

    def __init__(self, openai_api_key: Optional[str] = None, **kwargs):
        super().__init__(
            base_url="https://openrouter.ai/api/v1",  # OpenRouter API endpoint
            openai_api_key=openai_api_key or os.environ.get("OPENROUTER_API_KEY"),
            **kwargs,
        )

llm = ChatOpenRouter(
    model_name="qwen/qwen3-coder:free",  # The model to use from OpenRouter
    max_tokens=500
)


class State(TypedDict):
    messages: Annotated[list[messages.BaseMessage], add_messages] # <<< Change 'List' to 'list[messages.BaseMessage]'


graph_builder = StateGraph(State)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]} 


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

user_input = input("Enter a message: ")
state = graph.invoke({"messages": [HumanMessage(content=user_input)]})  

print(state["messages"][-1].content)
