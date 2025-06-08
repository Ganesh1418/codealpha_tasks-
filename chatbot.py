import nltk
from nltk.chat.util import Chat, reflections

# Pairs of pattern and response
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Polisetty Sai Ganesh.", "You can call me ChatBuddy."]
    ],
    [
        r"how are you?",
        ["I'm doing great, thanks for asking!", "I'm a bot, but I'm feeling helpful!"]
    ],
    [
        r"sorry (.*)",
        ["No worries!", "It's okay, how can I assist you?"]
    ],
    [
        r"i need help with (.*)",
        ["Why do you need help with %1?", "Sure, I can help with %1."]
    ],
    [
        r"quit",
        ["Goodbye!", "See you later!", "Have a great day!"]
    ],
    [
        r"(.*)",
        ["I didn't understand that. Could you rephrase?", "Interesting. Tell me more!", "Let's talk about something else."]
    ]
]

# Start chatbot
def chatbot():
    print("🤖 ChatBot: Hi! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
