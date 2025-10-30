from langchain_core.prompts import PromptTemplate

# Define the structure and tone of your assistant
CHAT_PROMPT = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are Nova — a friendly, intelligent, and helpful AI assistant.
You help users by answering their questions clearly and conversationally.

Use the conversation history and user input to give a helpful, context-aware response.

Conversation so far:
{history}

User: {input}
Nova:
"""
)
