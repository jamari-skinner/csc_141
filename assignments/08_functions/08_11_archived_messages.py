def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = ["Hey there!", "What’s up?", "See you later!", "Let’s code!"]
sent_messages = []

send_messages(text_messages[:], sent_messages)

print("\nOriginal messages:", text_messages)
print("Sent messages:", sent_messages)