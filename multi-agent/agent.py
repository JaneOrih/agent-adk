import os, asyncio
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import logging

logging.basicConfig(level=logging.ERROR)


OPENAI_API_KEY = os.getenv['OPENAI_API_KEY']
GOOGLE_API_KEY = os.getenv["GOOGLE_API_KEY"]
GROQ_API_KEY = os.getenv["GROQ_API_KEY"]
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"


# @title Define the get_weather Tool
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city (e.g., "New York", "London", "Tokyo").

    Returns:
        dict: A dictionary containing the weather information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'report' key with weather details.
              If 'error', includes an 'error_message' key.
    """
    print(f"--- Tool: get_weather called for city: {city} ---") # Log tool execution
    city_normalized = city.lower().replace(" ", "") # Basic normalization

    # Mock weather data
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}



weather_agent = Agent(
    name = "weather_agent",
    description="gets weather info for city",
    model="gemini_2.5_flash",
    instruction= "you are a weather assistent, use the get_weather tool to answer user question o weather. If the tool returns an error, inform the user politely. If the tool is successful, present the weather report clearly",
    tools=[get_weather],
)


session_service = InMemorySessionService()

# Define constants for identifying the interaction context
APP_NAME = "weather_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001" # Using a fixed ID for simplicity
 
# Create the specific session where the conversation will happen
session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)
print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")


runner = Runner(
    agent= weather_agent,
    app_name= APP_NAME,
    session_service= session_service
)


async def call_agent_async(query: str, runner, user_id, session_id):
    """Sends a query to the agent and prints the final response."""

    content = types.Content(role="user", parts=[types.Part(text=query)])

    final_response_text = "Agent did not produce a final response." # Default
    
    async for event in runner.run_async(user_id=user_id, session_id= session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text= event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text=f"Agent escalated: {event.error_message or 'no specific message.'}"
            break


async def run_conversation():
    await call_agent_async(query= "What is the weather in London?",
                           runner=runner,
                           user_id= USER_ID,
                           session_id=SESSION_ID
                        )
    


if __name__=="__main__":
    try:
        asyncio.run(run_conversation())
    except Exception as e:
        print(f"An error occured: {e}")