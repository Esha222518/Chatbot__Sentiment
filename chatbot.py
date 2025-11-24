from sentiment import analyze_sentiment
from datetime import datetime

# Lists to store all messages and sentiments
conversation_messages = []
conversation_sentiments = []

def save_to_log(user, bot, sentiment=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("chat_history.txt", "a", encoding="utf-8-sig") as f:
        if sentiment is not None:
            f.write(f"{timestamp} - USER: {user} → Sentiment: {sentiment}\n")
        else:
            f.write(f"{timestamp} - USER: {user}\n")
        f.write(f"{timestamp} - BOT: {bot}\n\n")

print("Chatbot started (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        # Overall conversation sentiment
        overall_score = sum(analyze_sentiment(msg)[1]['compound'] for msg in conversation_messages)
        avg_score = overall_score / len(conversation_messages) if conversation_messages else 0

        if avg_score >= 0.05:
            overall_sentiment = "Positive"
            description = "general satisfaction"
        elif avg_score <= -0.05:
            overall_sentiment = "Negative"
            description = "general dissatisfaction"
        else:
            overall_sentiment = "Negative"
            description = "general dissatisfaction"

        print(f"\nFinal Output: Overall conversation sentiment: {overall_sentiment} – {description}")
        save_to_log("quit", "Goodbye!")
        print("Bot: Goodbye! 👋")
        break

    # Get sentiment
    sentiment_label, scores = analyze_sentiment(user_input)

    # Decide bot reply based on sentiment
    if sentiment_label == "Negative":
        bot_reply = "I’ll make sure your concern is addressed."
    elif sentiment_label == "Positive":
        bot_reply = "I’m glad to hear that!"
    else:
        bot_reply = "Thanks for sharing. Tell me more."

    # Save conversation
    conversation_messages.append(user_input)
    conversation_sentiments.append(sentiment_label)

    # Display in example format
    print(f'User: "{user_input}" → Sentiment: {sentiment_label}')
    print(f'Chatbot: "{bot_reply}"\n')

    # Save to log
    save_to_log(user_input, bot_reply, sentiment_label)
