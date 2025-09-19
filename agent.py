from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

load_dotenv()

agent = Agent(
    'openai:gpt-4o'
)

@agent.tool
def get_weather(_, location: str) -> str:
    """Get the weather for a given location. Ensure location is fully spelled out."""
    print(f"Getting weather for {location}")
    return f"The weather in {location} is sunny."

agent_app = agent.to_ag_ui()

frontend_build_dir = Path(__file__).parent / "frontend" / "out"

app = Starlette()
app.mount("/api", agent_app)

if frontend_build_dir.exists():
    app.mount("/", StaticFiles(directory=frontend_build_dir, html=True), name="frontend")
else:

    async def _frontend_not_built(request):  # type: ignore[unused-arg]
        return JSONResponse(
            {
                "detail": "Frontend build not found. Run `pnpm run build:static` inside the frontend directory.",
            },
            status_code=404,
        )

    app.add_route("/", _frontend_not_built, methods=["GET"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
