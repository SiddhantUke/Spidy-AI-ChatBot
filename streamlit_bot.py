import streamlit as st
from Backend import chatbot
from langchain_core.messages import HumanMessage
import uuid


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Spidy AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

    /* Main App */
    .stApp {
        background: #0f1117;
        color: #ffffff;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #151821;
        border-right: 1px solid #292d3a;
    }

    /* Logo */
    .logo {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #8b93a7;
        font-size: 14px;
        margin-bottom: 30px;
    }

    /* Main Header */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 5px;
        background: linear-gradient(
            90deg,
            #7c3aed,
            #06b6d4
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .main-subtitle {
        text-align: center;
        color: #8b93a7;
        font-size: 15px;
        margin-bottom: 35px;
    }

    /* Welcome Card */
    .welcome-card {
        background: linear-gradient(
            135deg,
            #171a24,
            #11141c
        );
        border: 1px solid #292d3a;
        border-radius: 18px;
        padding: 30px;
        margin: 20px auto;
        max-width: 800px;
        text-align: center;
    }

    .welcome-icon {
        font-size: 45px;
        margin-bottom: 10px;
    }

    .welcome-title {
        font-size: 25px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .welcome-text {
        color: #9ca3b4;
        font-size: 15px;
    }

    /* Feature Cards */
    .feature-card {
        background: #171a24;
        border: 1px solid #292d3a;
        border-radius: 14px;
        padding: 18px;
        min-height: 120px;
    }

    .feature-icon {
        font-size: 25px;
    }

    .feature-title {
        font-weight: 600;
        margin-top: 8px;
    }

    .feature-description {
        color: #8b93a7;
        font-size: 13px;
        margin-top: 5px;
    }

    /* Chat Messages */
    [data-testid="stChatMessage"] {
        background: transparent;
        border: none;
    }

    /* Chat Input */
    [data-testid="stChatInput"] {
        border: 1px solid #343949;
        border-radius: 18px;
    }

    /* Sidebar Button */
    .sidebar-info {
        background: #1b1f2a;
        border: 1px solid #292d3a;
        border-radius: 12px;
        padding: 15px;
        margin-top: 20px;
    }

    .sidebar-title {
        font-weight: 600;
        margin-bottom: 8px;
    }

    .sidebar-text {
        color: #8b93a7;
        font-size: 13px;
        line-height: 1.6;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #666d7e;
        font-size: 12px;
        margin-top: 30px;
        margin-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())


# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------

CONFIG = {
    "configurable": {
        "thread_id": st.session_state["thread_id"]
    }
}


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="logo">🤖 Spidy AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your intelligent AI assistant</div>',
        unsafe_allow_html=True
    )

    if st.button("🗑️  Clear Conversation", use_container_width=True):

        st.session_state["message_history"] = []
        st.session_state["thread_id"] = str(uuid.uuid4())

        st.rerun()

    st.markdown(
        """
        <div class="sidebar-info">
            <div class="sidebar-title">⚡ Powered By</div>

            
                • LangGraph<br>
                • LangChain<br>
                • Groq<br>
                • Llama 3.3 70B
            
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-info">
            <div class="sidebar-title">🧠 Architecture</div>

            
                Streamlit → LangGraph → Chat Node
                → Groq LLM → AI Response
            
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-info">
            <div class="sidebar-title">💾 Memory</div>

            
                Conversation state is managed using
                LangGraph checkpointing.
            
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🕷️ Spidy AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'A conversational AI powered by LangGraph & Groq'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# WELCOME SCREEN
# ---------------------------------------------------------

if not st.session_state["message_history"]:

    st.markdown(
        """
        <div class="welcome-card">

        ✨ Welcome to Spidy AI 🕷️💬 Ask anything. 💡 Explore ideas. 🚀 Learn something new.

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">💡</div>
                <div class="feature-title">Learn</div>
                <div class="feature-description">
                    Get explanations for technical and general topics.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🚀</div>
                <div class="feature-title">Build</div>
                <div class="feature-description">
                    Discuss AI, Python, LangGraph and application ideas.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🧠</div>
                <div class="feature-title">Explore</div>
                <div class="feature-description">
                    Ask questions and continue a contextual conversation.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------------------------------

for message in st.session_state["message_history"]:

    with st.chat_message(
        message["role"],
        avatar="👤" if message["role"] == "user" else "🤖"
    ):
        st.markdown(message["content"])


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

user_input = st.chat_input(
    "Message Spidy AI..."
)


# ---------------------------------------------------------
# PROCESS USER INPUT
# ---------------------------------------------------------

if user_input:

    # Add user message
    st.session_state["message_history"].append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("ai", avatar="🤖"):

        with st.spinner("Spidy is thinking..."):

            response = chatbot.invoke(
                {
                    "message": [
                        HumanMessage(content=user_input)
                    ]
                },
                config=CONFIG
            )

            ai_message = response["message"][-1].content

            st.markdown(ai_message)

    # Save AI response
    st.session_state["message_history"].append(
        {
            "role": "ai",
            "content": ai_message
        }
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Spidy AI • Built with LangGraph + Groq + Streamlit<br>Developed by <strong>Siddhant Uke</strong>
    </div>
    """,
    unsafe_allow_html=True
)