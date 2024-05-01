#pip install nltk
import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! How can I assist you?"]
    ],
    [
        r"what is your name ?",
        ["I am a simple chatbot created using NLTK.", "I'm an NLTK-based bot."]
    ],
    [
        r"how are you ?",
        ["I'm doing fine! How about you?", "Good, thank you! How are you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "It's OK, never mind."]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I assist you today?", "Happy to hear you're fine! What can I do for you today?"]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon.", "Goodbye!"]
    ]
]

# Create a chatbot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()

if __name__ == "__main__":
    print("Hi, I'm the chatbot. Type 'quit' to exit.")
    chat.converse()
