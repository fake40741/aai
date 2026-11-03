#T.C=O(1) S.C=O(L)
# AI Rule-Based Chatbot
def chatbot(message):
    message = message.lower().split()
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "your name" in message:
        return "I am an AI chatbot created using Python."

    elif "artificial intelligence" in message or "what is ai" in message:
        return "AI enables machines to perform tasks that need human intelligence."

    elif "machine learning" in message or "ML" in message:
        return "Machine Learning allows computers to learn from data."

    elif "python" in message:
        return "Python is a popular language used in AI and Machine Learning."

    elif "study" in message or "exam" in message:
        return "Make a study plan and practice programs regularly."

    elif "project" in message:
        return "You can create AI projects like chatbots and smart assistants."

    elif "how are you" in message:
        return "I am fine! Ready to answer your questions."

    elif "thank" in message:
        return "You are welcome! Happy to help."

    elif "help" in message:
        return "You can ask me about AI, Python, ML, exams, or projects."

    elif "bye" in message:
        return "Goodbye! Keep learning AI."

    else:
        return "Sorry, I don't understand. Please ask another question."
print("AI Chatbot: Hello! Type 'bye' to exit.")
while True:
    user = input("You: ")
    reply = chatbot(user)
    print("Chatbot:", reply)

    if "bye" in user.lower():
        break

# Algorithm
# 1. Accept a message from the user.
# 2. Convert it to lowercase.
# 3. Match the message against predefined rules.
# 4. Generate a suitable response for the matching rule.
# 5. Display a default response if no rule matches.
# 6. Repeat until the user types bye.
# Complexity: For \(k\) rules and input length \(m\), approximately \(O(km)\) time and \(O(m)\) auxiliary space.

# Viva point: The chatbot demonstrates natural-language input handling and rule-based response generation. Unlike generative AI, it does not learn or create new knowledge from training data.