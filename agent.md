# agent.md

This file provides guidance for AI agents when working with code in this repository.

## Project Overview

TwinRAD is a multi-agent red teaming framework built with AutoGen (AG2) for testing the safety and robustness of language models. The system orchestrates specialized AI agents in a controlled adversarial environment to probe target LLMs for vulnerabilities.

## Core Architecture

The system follows a modular agent-based architecture:

- **Multi-Agent System**: Built on AutoGen's GroupChat framework with specialized agents
- **Communication Layer**: Socket.IO server (`server/server.py`) handles real-time agent communication
- **Workflow Orchestration**: Custom speaker selection logic in `twinrad/workflows/red_team_flow.py`
- **Agent Specialization**: Each agent in `twinrad/agents/` has a specific role in the red team process

### Key Agent Types

1. **PromptGenerator**: Creates adversarial prompts to test target models
2. **GourmetAgent**: The vulnerable target LLM being tested
3. **EvaluatorAgent**: Analyzes responses for safety violations
4. **IntrospectionAgent**: Learns from evaluations and provides strategic recommendations
5. **PlannerAgent**: Orchestrates the conversation flow and determines next speakers

## Development Commands

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the System
```bash
# Install the package in development mode
pip install -e .

# Run the main red team workflow
twinrad

# OR run directly with Python
python -m twinrad.main

# Optional: Start the Socket.IO server (separate terminal)
twinrad-server
# OR python server/server.py

# Optional: Launch monitoring dashboard (separate terminal)
twinrad-dashboard
# OR streamlit run dashboard/app.py
```

### Configuration
Environment variables required in `.env`:
- `GOOELG_GENAI_API_KEY`: Google Gemini API key for red team agents
- `TWINKLE_BASE_URL`: Base URL for target LLM API
- `TWINKLE_API_KEY`: API key for target LLM
- `LOG_LEVEL`: Logging level (default: INFO)

## Agent Development Patterns

### Creating New Agents
1. Inherit from `BaseAgent` in `src/twinrad/agents/base_agent.py`
2. Add agent name to `AgentName` enum in `src/twinrad/schemas/agents.py`
3. Update speaker selection logic in `red_team_flow.py`
4. Register in main GroupChat configuration

### Agent Communication Flow
The system uses a structured conversation flow:
1. UserProxy initiates with a test prompt
2. PromptGenerator creates adversarial prompt
3. GourmetAgent (target) responds
4. EvaluatorAgent assesses the response
5. IntrospectionAgent analyzes and learns
6. PlannerAgent decides next speaker

### Tool Integration
Agents can use tools from `src/twinrad/tools/`:
- `reward_tool.py`: Reward system for agent behavior
- `safety_db_tool.py`: Safety violation database
- `social_media_tool.py`: Social media simulation

## Configuration Management

Settings are centralized in `configs/settings.py` using Pydantic:
- Server configuration (host, port)
- API keys and endpoints
- Logging configuration

Logging is standardized across all components using `configs/logging_config.py`.

## Import Resolution Fix

The main script includes a sys.path fix to resolve module import issues:
```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

This allows the script to find the `configs/` module when run from the project root with `python twinrad/main.py`.

## Docker Configuration

The system is configured to run without Docker by default:
- UserProxyAgent includes `code_execution_config={"use_docker": False}`
- This eliminates Docker dependency for local development

## Testing and Validation

The system is designed for security research and should only be used for:
- Defensive security testing
- LLM safety evaluation
- Academic research on AI alignment

**Important**: This framework tests AI safety mechanisms and should be used responsibly for defensive purposes only.

## Architecture Notes

- **Event-Driven**: Uses Socket.IO for real-time agent communication
- **Stateful Conversations**: GroupChat maintains conversation history
- **Extensible Agents**: Modular agent design allows easy addition of new capabilities
- **Configurable Workflows**: Speaker selection logic can be customized for different test scenarios