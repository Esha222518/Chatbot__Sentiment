import streamlit as st
from sentiment import analyze_sentiment

# Initialize session state for conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("Chatbot with Sentiment Analysis 💬")
st.markdown("Talk to the bot. Type your messages below:")

# Input box for user
user_input = st.text_input("You:")

def get_bot_reply(sentiment_label):
    """Return bot reply based on sentiment"""
    if sentiment_label == "Negative":
        return "I’ll make sure your concern is addressed."
    elif sentiment_label == "Positive":
        return "I’m glad to hear that!"
    else:
        return "Thanks for sharing. Tell me more."

def update_conversation(user_msg):
    """Analyze sentiment, update conversation state, and return bot reply"""
    sentiment_label, scores = analyze_sentiment(user_msg)
    bot_reply = get_bot_reply(sentiment_label)

    # Save message, sentiment, and bot reply to session_state
    st.session_state.messages.append({
        "user": user_msg,
        "sentiment": sentiment_label,
        "bot": bot_reply
    })

# Button to send message
if st.button("Send") and user_input:
    update_conversation(user_input)

# Display conversation history
for chat in st.session_state.messages:
    st.markdown(f'**User:** "{chat["user"]}" → Sentiment: {chat["sentiment"]}')
    st.markdown(f'**Chatbot:** "{chat["bot"]}"\n')

# Button to end chat and show overall sentiment with description
if st.button("End Chat"):
    if st.session_state.messages:
        # Compute overall sentiment
        total = 0
        for chat in st.session_state.messages:
            _, scores = analyze_sentiment(chat["user"])
            total += scores['compound']
        avg = total / len(st.session_state.messages)
        if avg >= 0.05:
            overall = "Positive"
            description = "general satisfaction"
        elif avg <= -0.05:
            overall = "Negative"
            description = "general dissatisfaction"
        else:
            overall = "Negative"
            description = "general dissatisfaction"

        st.markdown(f"**Final Output: Overall conversation sentiment: {overall} – {description}**")
    else:
        st.markdown("**No messages in conversation.**")
