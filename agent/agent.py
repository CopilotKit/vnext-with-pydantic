from pydantic_ai import Agent
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

agent = Agent(
    'openai:gpt-4o'
)

@agent.tool
def get_weather(_, location: str) -> str:
    """Get the weather for a given location. Ensure location is fully spelled out."""
    print(f"Getting weather for {location}")
    return f"The weather in {location} is sunny."

app = agent.to_ag_ui()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
