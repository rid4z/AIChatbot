from ollama import chat

MODEL = "llama3.2"
MEMORY_PAIRS = 4

def get_chatbot_response(user_input: str, conversation: list[dict[str, str]]) -> str:
    conversation.append({"role": "user", "content": user_input})
    limited_context = conversation[-2 * MEMORY_PAIRS:]

    assistant_tokens = []
    for part in chat(MODEL, messages=limited_context, stream=True):
        token = part["message"]["content"]
        assistant_tokens.append(token)

    full_response = "".join(assistant_tokens)
    conversation.append({"role": "assistant", "content": full_response})
    return full_response
