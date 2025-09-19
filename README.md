# VNext with Pydantic

A simple demo showing how Pydantic AI agents work with CopilotKit's new frontend.

## What's This?

This is an example of Pydantic AI and CopilotKit vNext working together.

CopilotKit connects directly to the endpoint created by the Pydantic AI agent. The React frontend then displays the chat and
shows streaming updates of what the agent is doing in real-time.

## How It Works

1. **Backend (Python)**: Creates a Pydantic AI agent and sets up an endpoint using `agent.to_ag_ui()`.

2. **Frontend (React)**: Uses CopilotKit's chat component to communicate directly with the Pydantic AI agent.

## What You Need

- [uv](https://docs.astral.sh/uv/) for Python package management
- [pnpm](https://pnpm.io/) for Node.js package management
- An OpenAI API key in your `.env` file or elsewhere in your environment

## Running It

### Terminal 1: Start the Python Backend

```bash
cd agent

cat > .env << EOF
OPENAI_API_KEY=your-openai-api-key
EOF

# Create a virtual environment
uv venv

# Install stuff
uv pip install -r requirements.txt

# Run the server (will be on port 8000)
uv run python agent.py
```

### Terminal 2: Start the React Frontend

```bash
cd frontend

# Install stuff
pnpm install

# Run the dev server (will be on port 3000)
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) and start chatting.

- **Tool Calls**: The agent has a `get_weather` tool. When you ask about weather, you'll see the tool being called in the UI.
- **Real-time Streaming**: Responses stream in as they're generated.
- **Tool Visualization**: The `WildCardRender` component shows you exactly what tools are being called with what arguments and results.

## How the frontend is set up

1. Import `PydanticAIAgent` from `@ag-ui/pydantic-ai`
2. Creates the outer `CopilotKitProvider` component and configures the `default` agent to use the Pydantic AI agent.
3. Adds the `WildCardRender` component to the `renderToolCalls` to surface tool calls in the UI.
4. Adds the `CopilotChat` component inside a full-screen div.

## Files That Matter

- `agent/agent.py` - The Pydantic AI agent.
- `frontend/app/page.tsx` - Sets up CopilotKit and connects to the backend.
- `frontend/app/WildCardRender.tsx` - Shows tool calls in a nice UI.

## Want to Modify?

- Add more tools: Just add more `@agent.tool` decorated functions in `agent.py`
- Add custom tool renderers: Define them with `defineToolCallRender` and add to the `renderToolCalls` prop in `app/page.tsx`
- Customize the UI ...
