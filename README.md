# 🕷️ Spidy AI — Stateful Conversational AI Chatbot

> 🤖 A stateful conversational AI chatbot built with **LangGraph, LangChain, Groq, Llama 3.3 70B, and Streamlit**.

## 🚀 Project Overview

**Spidy AI** is a conversational AI chatbot designed to demonstrate how an LLM application can be built using a **state-based workflow with LangGraph**.

The project demonstrates:

- 🧠 Message state management
- 🔄 Graph-based execution
- 💾 Checkpointing
- 🧵 Thread-based conversation handling
- 💬 Conversational message history
- 🎨 Interactive Streamlit UI
- ⚡ Groq-powered Llama 3.3 70B responses

The main idea is to understand how **state, nodes, edges, messages, reducers, checkpoints, and threads** work together to build a stateful AI application.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| 🦜 **LangChain** | LLM and message integration |
| 🕸️ **LangGraph** | State-based AI workflow |
| ⚡ **Groq** | Fast LLM inference |
| 🦙 **Llama 3.3 70B** | Language model |
| 🎨 **Streamlit** | Interactive web interface |
| 🔐 **python-dotenv** | Environment variable management |
| 💾 **InMemorySaver** | LangGraph checkpointing |

---

# 🔄 Simple Workflow

```text
👤 User
   ↓
🎨 Streamlit
   ↓
💬 Human Message
   ↓
🕸️ LangGraph
   ↓
⚙️ Chat Node
   ↓
⚡ Groq LLM
   ↓
🦙 Llama 3.3 70B
   ↓
🤖 AI Response
   ↓
💾 Checkpoint
   ↓
🎨 Streamlit
```

### 🕸️ LangGraph Workflow

```text
🚀 START
   ↓
⚙️ Chat Node
   ↓
🏁 END
```

---

# 🧠 Backend Workflow

## 1️⃣ State

The chatbot maintains a state called **ChatState**.

The state contains the conversation's message history.

The message history can contain:

- 👤 Human Messages
- 🤖 AI Messages

Conceptually:

```text
🧠 ChatState
      ↓
💬 Message History
      ↓
👤 Human Message
      +
🤖 AI Message
```

## 2️⃣ 💬 Message Management

LangGraph uses the **`add_messages` reducer** to manage the message list.

Conceptually:

```text
📚 Existing Messages
        +
🆕 New Messages
        ↓
📚 Updated Message History
```

This allows the chatbot to maintain a conversational flow.

## 3️⃣ ⚙️ Chat Node

The **Chat Node** is the main processing component.

Its responsibility is to:

1. 📥 Receive the current state
2. 📖 Read the conversation messages
3. 📤 Send the messages to the LLM
4. 🤖 Receive the AI response
5. 📦 Return the response to the graph state

Conceptually:

```text
🧠 State
   ↓
💬 Messages
   ↓
⚙️ Chat Node
   ↓
⚡ LLM
   ↓
🤖 AI Response
```

## 4️⃣ ⚡ Groq LLM

The project uses **ChatGroq** to communicate with the Groq-hosted **Llama 3.3 70B Versatile** model.

```text
💬 Messages
     ↓
⚡ ChatGroq
     ↓
🦙 Llama 3.3 70B
     ↓
🤖 AI Response
```

## 5️⃣ 🕸️ Graph Execution

The graph starts at **START**, executes the **Chat Node**, and then reaches **END**.

```text
🚀 START
   ↓
⚙️ Chat Node
   ↓
🏁 END
```

## 6️⃣ 💾 Checkpointing

The project uses **InMemorySaver** as the LangGraph checkpointer.

A checkpointer saves graph state during execution so that LangGraph can associate state with a conversation thread.

```text
🕸️ Graph Execution
        ↓
📸 Checkpoint
        ↓
💾 InMemorySaver
        ↓
🧠 Saved Graph State
```

`InMemorySaver` stores this information in memory, making it useful for learning, development, and testing.

## 7️⃣ 🧵 Thread ID

A **Thread ID** identifies a particular conversation.

```text
🧵 Thread ID
     ↓
💬 Conversation
     ↓
🧠 Graph State
```

The thread ID is supplied through the configurable runtime configuration so that the checkpointer knows which conversation the state belongs to.

---

# 🎨 Streamlit Frontend Workflow

The Streamlit application provides the user interface.

Its responsibilities include:

- ✍️ Accepting user input
- 👤 Displaying user messages
- 🕸️ Calling the LangGraph chatbot
- 🤖 Receiving the AI response
- 💬 Displaying the AI response
- 🧠 Maintaining frontend conversation history
- 🎨 Providing an interactive chatbot experience

---

# 🧠 Streamlit Session State

**Streamlit Session State** maintains the conversation history displayed by the UI.

It stores information such as:

- 👤 Message role
- 💬 Message content

Conceptually:

```text
👤 User Message
      ↓
🧠 Session History
      ↓
🤖 AI Response
      ↓
🧠 Session History
```

### ⚠️ Important

Streamlit Session State should not be confused with the LangGraph checkpointer.

---

# 💾 Checkpointer vs 🧠 Session State

| Feature | Streamlit Session State | LangGraph Checkpointer |
|---|---|---|
| 🎯 Purpose | UI conversation history | Graph execution state |
| 🧠 Manages | Frontend messages | LangGraph state |
| 🧵 Thread-aware | Not primarily | Yes |
| 💾 Used by | Streamlit | LangGraph |
| 📦 Current implementation | Session State | InMemorySaver |

### In short

```text
🎨 Session State
      ↓
💬 UI History

        VS

🕸️ Checkpointer
      ↓
🧠 Graph State
```

---

# 🔄 Complete End-to-End Workflow

1. 👤 The user enters a message in Streamlit.
2. 🎨 Streamlit captures the user input.
3. 💬 The input is represented as a Human Message.
4. 🕸️ The message is sent to the compiled LangGraph chatbot.
5. 🧵 A thread ID identifies the conversation.
6. 🚀 LangGraph starts execution from START.
7. ⚙️ The Chat Node receives the current state.
8. 📤 The Chat Node sends the conversation messages to ChatGroq.
9. 🦙 The Groq-hosted Llama model generates an AI response.
10. 🤖 The response is returned to the LangGraph state.
11. 💾 The checkpointer maintains the checkpoint associated with the thread.
12. 🏁 The graph reaches END.
13. 🎨 Streamlit receives the updated response.
14. 💬 The latest AI message is extracted and displayed.
15. 🧠 The response is added to the Streamlit session history.

---

# 🏗️ Architecture

```text
                    👤 USER
                       │
                       ▼
              🎨 STREAMLIT FRONTEND
                       │
                       ▼
                💬 HUMAN MESSAGE
                       │
                       ▼
                 🧠 LANGGRAPH
                       │
                       ▼
                    🚀 START
                       │
                       ▼
                  ⚙️ CHAT NODE
                       │
                       ▼
                   ⚡ CHATGROQ
                       │
                       ▼
                 🦙 LLAMA 3.3 70B
                       │
                       ▼
                  🤖 AI RESPONSE
                       │
                       ▼
               🧠 UPDATED STATE
                       │
                       ▼
                💾 INMEMORYSAVER
                       │
                       ▼
                    🏁 END
                       │
                       ▼
              🎨 STREAMLIT FRONTEND
                       │
                       ▼
                 👤 USER SEES
                   RESPONSE
```

---

# 🔑 Key Concepts

### 🧠 State
The information that flows through the LangGraph workflow.

### 💬 Message
A structured representation of human, AI, system, or tool communication.

### ⚙️ Node
A processing step in the graph. In this project, the Chat Node communicates with the LLM.

### 🔗 Edge
Defines how execution moves between graph components.

### 🚀 START
The entry point of the graph.

### 🏁 END
The exit point of the graph.

### 🔄 Reducer
Defines how state updates are combined. The project uses **`add_messages`** for message state.

### 💾 Checkpointer
Stores graph execution checkpoints.

### 🧵 Thread ID
Identifies a particular conversation or execution context.

### 🎨 Session State
Stores frontend conversation information in Streamlit.

---

# 🤔 Why LangGraph?

A direct LLM call is sufficient for a simple question-and-answer application.

However, real AI applications often require:

- 🧠 State management
- 🔄 Multiple processing steps
- 🔀 Conditional routing
- 🛠️ Tool calling
- 👤 Human approval
- 💾 Persistence
- 🛡️ Error handling

**LangGraph** provides a structured way to build these workflows.

This project represents a foundation for building more advanced **Agentic AI applications**.

---

# 🚀 Possible Future Extensions

The current workflow can be extended with:

- 📚 **RAG**
- 🛠️ **Tool Calling**
- 🌐 **Web Search**
- 🗄️ **Database Tools**
- 👤 **Human-in-the-Loop**
- 🛡️ **Guardrails**
- ✅ **Input & Output Validation**
- 🤖 **Multiple Agents**
- 🔀 **Conditional Routing**
- 💾 **Long-Term Persistence**
- 🗃️ **Production Database Checkpointers**

---

# 📌 Final Summary

**Spidy AI** demonstrates how to build a basic **stateful conversational chatbot** using LangGraph, Groq, and Streamlit.

The frontend collects the user's message and sends it to the LangGraph backend.

LangGraph manages the state and routes execution to the Chat Node.

The Chat Node sends the conversation to the Groq-hosted Llama model and receives the AI response.

The response becomes part of the updated graph state and is then displayed by Streamlit.

The project also demonstrates **checkpointing and thread IDs**, which are important concepts for building stateful LangGraph applications.

---

## 🕷️ Core Workflow

```text
👤 User
  ↓
🎨 Streamlit
  ↓
💬 Human Message
  ↓
🕸️ LangGraph
  ↓
⚙️ Chat Node
  ↓
⚡ Groq / 🦙 Llama 3.3 70B
  ↓
🤖 AI Response
  ↓
💾 Checkpointer
  ↓
🎨 Streamlit
```

---

## 🌟 Project Highlights

🧠 **Stateful Conversation**  
🕸️ **LangGraph Workflow**  
⚡ **Fast Groq Inference**  
🦙 **Llama 3.3 70B**  
💾 **Checkpointing**  
🧵 **Thread-Based State**  
🎨 **Streamlit UI**  
🚀 **Foundation for Agentic AI**

---

## 👨‍💻 Developed By

### **Siddhant Uke**

🕷️ **Spidy AI** — Built with **LangGraph + Groq + Streamlit**
