# TwinRAD

This repository implements a multi-agent red teaming framework designed to test the safety and robustness of language models (LMs). The system simulates a controlled adversarial environment where a team of offensive agents actively probes and attacks a target LLM.

---

## Project Structure 📂

Our project is organized to be modular, scalable, and easy to navigate. The core of our system is located in the `twinrad/` directory, while other top-level folders manage the peripheral components, configurations, and documentation.

```text
.
├── LICENSE                     # Project license file
├── README.md                   # You are here! General project information
├── client                      # Simple client for initial requests
│   └── client.py
├── configs                     # Configuration files for LLMs, etc.
├── dashboard                   # Streamlit application for real-time monitoring
│   └── app.py
├── server                      # Central Socket.IO communication server
│   └── server.py
├── tests                       # Unit and integration tests
└── twinrad                     # The core Twinrad multi-agent system
    ├── agents                  # Each folder holds a specialized agent
    │   ├── base_agent.py        # Shared logic for all agents
    │   ├── introspection_agent.py # The AG2-level learning agent
    │   ├── prompt_generator.py  # Agent for creating attack prompts
    │   ├── gourmet_agent.py     # The vulnerable target LLM
    │   └── ...
    ├── main.py                 # Main entry point to start the system
    ├── tools                   # Tools the agents can call (e.g., databases)
    │   └── ...
    └── workflows               # Defines the collaboration logic between agents
        └── red_team_flow.py     # Orchestrates the red-teaming process
```

### Key Components Explained

* **`server/`**: This is the heart of our communication. It's a central **Socket.IO server** that allows all agents, the client, and the dashboard to communicate in real-time.
* **`twinrad/`**: This is where the magic happens. It contains the logic for all our custom-built agents, the tools they use, and the workflows that define their interactions.
  * **`agents/`**: Each Python file here represents a distinct, specialized agent. They are designed to work independently and communicate via the server.
  * **`tools/`**: These are the simulated external resources that our agents can access, such as a mock database or an API. They are crucial for testing tool-use vulnerabilities.
  * **`workflows/`**: This folder contains the high-level orchestration logic. The `red_team_flow.py` script defines the sequence of events, ensuring a smooth and repeatable test cycle.
* **`dashboard/`**: The `app.py` file here runs a **Streamlit** dashboard, providing a visual, real-time overview of the red-teaming process, showing attack progress and vulnerability findings.

---

## 🚀 Getting Started with TwinRAD

This guide will help you set up and run the `twinrad` multi-agent system. This framework is designed to conduct red-teaming exercises by orchestrating a team of specialized AI agents to test the security and safety of a target large language model (LLM).

### 📋 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.13+**
* **Git**

### 💻 Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/ai-twinkle/TwinRAD.git
   cd TwinRAD
   ```

2. **Create a virtual environment** (recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required libraries:**

   ```sh
   pip install -r requirements.txt
   ```

### 🛠️ Configuration

The system requires API keys for the LLMs that will power the agents.

1. **Create a `.env` file:**
   Create a new file named `.env` in the root directory of the project.

2. **Add your API keys:**
   Add your API keys to the `.env` file in the following format:

   ```env
   TWINKLE_BASE_URL=https://litellm-ekkks8gsocw.dgx-coolify.apmic.ai
   TWINKLE_API_KEY=your_api_key_here
   GOOELG_GENAI_API_KEY=your_google_api_key_here
   ```

   *Replace the placeholder values with your actual API keys.*

### ▶️ How to Run the System

The `main.py` script orchestrates the entire red-teaming operation.

**Run the system:**

*Make sure you are in the `TwinRAD/` root directory*

```sh
python twinrad/main.py
```

### 🧠 System in Action

Once the system is running, you will see a series of log messages in your terminal. This shows the agents communicating in a structured conversation, as defined by the `GroupChat` workflow.

* The **PromptGenerator** starts the process with a predefined attack.
* The **GourmetAgent** (the target LLM) responds to the prompt.
* The **EvaluatorAgent** analyzes the response and sends a diagnostic report.
* The **IntrospectionAgent** receives the report, learns from it, and provides a strategic recommendation.
* The **PlannerAgent** uses this recommendation to decide which agent should speak next, potentially giving the floor back to the `PromptGenerator` for a refined attack.

The conversation will continue until a `max_round` limit is reached or the agents decide the task is complete.
