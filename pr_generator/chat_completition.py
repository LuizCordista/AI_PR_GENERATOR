from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

def chatCompletion(prompt):
    api_url = os.environ.get("LLM_API_URL")
    api_key = os.environ.get("LLM_API_KEY")
    model_name = os.environ.get("LLM_MODEL", "gpt-3.5-turbo")
    # Optional: custom headers
    custom_headers = {}
    if os.environ.get("LLM_HEADERS"):
        import json
        custom_headers = json.loads(os.environ["LLM_HEADERS"])

    chat = ChatOpenAI(
        model_name=model_name,
        openai_api_base=api_url,
        openai_api_key=api_key,
        default_headers=custom_headers or None,
    )

    messages = [
        HumanMessage(content=prompt),
    ]
    return chat.invoke(messages)