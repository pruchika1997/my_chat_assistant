from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

from src.config.settings import BACKEND, OLLAMA_MODEL


def create_chat_assistant():
    """
    Create a conversational assistant using the modern LangChain Runnable API.
    Compatible with LangChain >= 1.0.0.
    """

    if BACKEND.lower() != "ollama":
        raise ValueError(f"Unsupported backend: {BACKEND}")

    llm = OllamaLLM(model=OLLAMA_MODEL)

    # Create a structured chat prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are Nova — a friendly and intelligent assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    # Combine prompt and LLM into a pipeline
    chain = prompt | llm

    # Add memory via RunnableWithMessageHistory
    def get_session_history(session_id):
        return ChatMessageHistory()

    conversational_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    return conversational_chain


def get_response(conversation, user_input: str, session_id="default") -> str:
    """
    Generate a response from the conversational chain using memory.
    """
    try:
        response = conversation.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        # response is an AIMessage object
        return response.content if hasattr(response, "content") else str(response)
    except Exception as e:
        return f"[Error] {e}"
