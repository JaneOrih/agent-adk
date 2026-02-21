from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def get_forecast(url: str)->dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    
