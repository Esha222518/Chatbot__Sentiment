
CHATBOT WITH SENTIMENT ANALYSIS :-

OVERVIEW :-
This project implements a chatbot capable of conducting a conversation with a user and performing sentiment analysis.  

Tier 1 : Conversation-level sentiment analysis.  
Tier 2 : Statement-level sentiment analysis per user message with trend summary.  

The chatbot supports both terminal-based and web UI (Streamlit) modes.

FILES IN REPOSITORY:-
chatbot_sentiment/
│
├── app.py                  # Streamlit UI chatbot
├── chatbot.py              # Terminal chatbot
├── sentiment.py            # Sentiment analysis module
├── emotion_engine.py       # Emotion detection module
├── chathistory.txt         # Optional: chat log file
├── requirements.txt        # Python packages needed
└── README.md               # Documentation


HOW TO RUN :-
(a) In Terminal Mode :-
1. Navigate to the project folder.  
2. Run the chatbot:
```bash
   python chatbot.py
3.Interact with the bot. 
  Type quit to exit.

(b) In Streamlit Web UI :-
Install dependencies
pip install -r requirements.txt
Run the app:
streamlit run app.py
Open the browser link, type your message, click Send, and click End Chat to see overall sentiment.


CHOSEN TECHNOLOGIES :-
1.Python 3.10+
2.NLTK (VADER Sentiment Analyzer)
3.Streamlit (Web UI)
4.Datetime (for logging timestamps)


EXPLANATION OF SENTIMENT ANALYSIS LOGIC:-
 Per message: Uses VADER sentiment analyzer to compute a compound score:
>= 0.05 → Positive
<= -0.05 → Negative
Otherwise → Neutral
Overall conversation sentiment: Average of compound scores across all messages determines the final sentiment.


STATUS OF TIER 2 IMPLEMENTATION :-
Sentiment is evaluated for each user message individually.
Each message is displayed with its sentiment:
User: "Your message" → Sentiment: Positive/Negative/Neutral.

TESTS IF IMPLEMENTED:-
Test 1:
Input: "Your service disappoints me"
Output:
User: "Your service disappoints me" → Sentiment: Negative, Emotion: SAD
Chatbot: "I’ll make sure your concern is addressed."

Test 2:
Input: "Last experience was better"
Output:User: "Last experience was better" → Sentiment: Positive, Emotion: HAPPY
Chatbot: "I’m glad to hear that!"

Test 3:
Input: "I feel neutral today"
Output:User: "I feel neutral today" → Sentiment: Neutral, Emotion: NEUTRAL
Chatbot: "Thanks for sharing. Tell me more."

Final Output:
Overall conversation sentiment: Negative – general dissatisfaction

INNOVATIONS :-
1.Maintains full conversation history with timestamps.
2.Detects user emotion per message (happy, sad, neutral, joy, anger).
3.Logs all conversations to chathistory.txt.
4.Streamlit UI provides an interactive browser-based chat interface.
5.Overall conversation sentiment is displayed with descriptive text, e.g.:
Overall conversation sentiment: Negative – general dissatisfaction

FEATURES:-
1.Statement-level sentiment and emotion detection for every user message.
2.Conversation-level sentiment summarization at the end of the session.
3.Mood trend summary showing counts of Positive / Neutral / Negative messages.
4.Supports multiple messages in a single session while retaining conversation history.
5.Works in both terminal and browser-based UI (Streamlit).
6.Modular and production-ready code with separate modules for sentiment and emotion detection.

ENHANCEMENTS:-
- Streamlit web interface for interactive chatting instead of terminal-only.  
- Each message shows both detected **emotion** and **sentiment**.  
- Allows multiple messages in a session while keeping previous messages visible.  
- Mood trend summary displays counts of Positive / Neutral / Negative messages at the end.  
- Supports both **terminal** and **browser-based UI** modes.  
- Clean, modular, production-friendly code structure with separate modules for sentiment and emotion detection.

SAMPLE TEST CASE TAKEN:-
![image alt](https://github.com/Esha222518/Chatbot__Sentiment/blob/5731ebbdffef922991c70eed4508006473d478f6/Screenshot%202025-11-27%20005443.png)




Example user conversation:-
Test 1:
Input: "Your service disappoints me"
Output:
User: "Your service disappoints me" → Sentiment: Negative, Emotion: SAD
Chatbot: "I’ll make sure your concern is addressed."

Test 2:
Input: "Last experience was better"
Output:User: "Last experience was better" → Sentiment: Positive, Emotion: HAPPY
Chatbot: "I’m glad to hear that!"

Test 3:
Input: "I feel neutral today"
Output:User: "I feel neutral today" → Sentiment: Neutral, Emotion: NEUTRAL
Chatbot: "Thanks for sharing. Tell me more."

Final Output:
Overall conversation sentiment: Negative – general dissatisfaction


=======
# Chatbot_Sentiment
A Python-based chatbot that conducts conversations with users, performs sentiment and emotion analysis for each message, and provides overall conversation sentiment. Includes a Streamlit UI for interactive chatting.
>>>>>>> 493f5ea8f818ff5af73356b7f4d17d5f113f2f32
