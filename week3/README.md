# Week 3 — Custom MCP Server (Weather & Stats)

**Author:** Noor Khalisa (NIM: 2410817220012)

This project implements a local Model Context Protocol (MCP) server using the STDIO transport. It wraps the free [Open-Meteo API](https://open-meteo.com/) to provide real-time weather data and temperature statistical trends to an AI agent.

## External API Used
* **Name:** Open-Meteo API
* **Endpoint Used:** `https://api.open-meteo.com/v1/forecast`
* **Note:** This is a free, open-source weather API that does not require an API key or authentication, making it highly reliable for basic weather and statistical data retrieval.

## Prerequisites & Setup
1. Ensure Python 3.10+ is installed.
2. Open your terminal and navigate to the `week3/server` directory:
   ```bash
   cd server
3. Set up the virtual environment and install dependencies:
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

(Note: Because the API is public, there are no Environment Variables or .env files required for this project).

Deployment Mode: Local (STDIO) via Cursor IDE
This server was deployed locally using STDIO transport and tested with Cursor IDE.

To configure the MCP client in Cursor:

Open Cursor Settings -> Tools & MCP.

Click Add Custom MCP (or edit the .cursor/mcp.json file directly).

Add the following JSON configuration (paths are specifically set for the local development environment):

JSON
{
  "mcpServers": {
    "Weather-Stats": {
      "command": "<ABSOLUTE_PATH_TO_YOUR_VENV>/Scripts/python",
      "args": [
        "<ABSOLUTE_PATH_TO_YOUR_PROJECT>/week3/server/main.py"
      ]
    }
  }
}

Tool Reference
This server exposes 2 tools with built-in resilience (timeout handling and input validation):

1. get_current_weather
Description: Retrieves the exact current temperature and windspeed for a specific location based on its coordinates.

Parameters:
- latitude (float): The latitude of the location.
- longitude (float): The longitude of the location.

Resilience: Includes graceful error handling for httpx.TimeoutException and httpx.HTTPStatusError if the Open-Meteo server goes down.

Expected Output: A formatted string, e.g., "Cuaca saat ini: Suhu 32.0°C, Kecepatan angin 15.2 km/h."

2. get_temperature_stats
Description: Retrieves maximum and minimum daily temperature forecasts for a specified number of days, useful for analyzing short-term weather trends.

Parameters:
- latitude (float): The latitude of the location.
- longitude (float): The longitude of the location.
- days (integer, default=3): The number of forecast days to retrieve.

Resilience: Validates the days input (must be between 1 and 14) to prevent exceeding the API's standard limits and returns a user-facing warning if violated.

Expected Output: A bulleted list of daily max/min temperatures.

Example Invocation Flow
To trigger the tools, open the AI Chat in Cursor (Ctrl+L) and use the following prompt:

User Prompt:
"Gunakan tools MCP Weather-Stats untuk mengecek cuaca saat ini di Banjarmasin, dan tolong berikan juga statistik suhu di sana untuk 3 hari ke depan."

Agent Behavior:
1. The AI infers the coordinates for Banjarmasin (Latitude: -3.3194, Longitude: 114.5908).
2. It calls get_current_weather with those coordinates via the MCP server.
3. It immediately follows up by calling get_temperature_stats with days=3.
4. The AI synthesizes the JSON responses from the server and outputs a neat, readable summary table.