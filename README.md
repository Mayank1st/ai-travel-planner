# AI Travel Planner

An AI-powered travel planning API built with FastAPI and OpenAI. It coordinates multiple specialized AI agents and parallel research tasks to prepare a trip plan, then flags higher-budget trips for human review.

## Features

- **Multi-agent planning:** planner, itinerary, and budget-approval agents handle distinct responsibilities.
- **Parallel travel research:** hotel, flight, and weather suggestions are gathered concurrently.
- **Workflow registry:** workflows are selected by name, providing an extensible pattern for registering additional workflows.
- **Human-in-the-loop review:** budgets at or above `30,000` are flagged as requiring manual approval.
- **Structured API response:** trip details, research, itinerary, approval information, and workflow status are returned in separate fields.
- **Interactive API docs:** explore and test endpoints through FastAPI Swagger UI.

## How the workflow works

1. The travel workflow collects hotel, flight, and weather research in parallel.
2. The planner agent combines the research with the destination, duration, and budget.
3. The itinerary agent turns the plan into a day-by-day itinerary.
4. The approval check flags budgets of `30,000` or more for human review.
5. The API returns the trip data with a `completed` or `pending_approval` status.

The workflow registry is designed to make it possible to register additional workflows. At present, the registry has one workflow registered: `travel`. The approval status is flagged in the response; a human approval interface or approval action is not currently included.

## Requirements

- Python
- An OpenAI API key

## Setup

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/Mayank1st/ai-travel-planner.git
   cd ai-travel-planner
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create your local environment file and add your OpenAI API key:

   ```bash
   cp .env.example .env
   ```

   Set `OPENAI_KEY` in `.env` to your own key. `.env.example` contains a placeholder only. Never commit or share your real `.env` file.

## Run the API

```bash
uvicorn app.main:app --reload
```

By default, the API is available at `http://127.0.0.1:8000`. Open `http://127.0.0.1:8000/docs` for interactive Swagger documentation.

## API Endpoints

### `GET /`

Returns basic service information and the current UTC timestamp.

### `POST /travel/travel-plan`

Creates a travel plan. Example request:

```json
{
  "destination": "Tokyo",
  "days": 2,
  "budget": 200000
}
```

The response is grouped into trip details, research, itinerary, approval details, and status. Example shape:

```json
{
  "trip": {
    "destination": "Tokyo",
    "days": 2,
    "budget": 200000
  },
  "research": {
    "hotels": "Hotel suggestions...",
    "flights": "Flight suggestions...",
    "weather": "Weather information..."
  },
  "itinerary": "Day-by-day travel itinerary...",
  "approval": {
    "required": true,
    "threshold": 30000,
    "message": "Manual approval is required..."
  },
  "status": "pending_approval"
}
```

### `POST /test-openai`

Calls OpenAI and returns a short service-status response. An optional `model` query parameter can select a model, for example:

```text
POST /test-openai?model=gpt-4o-mini
```

## Configuration

| Variable | Description |
| --- | --- |
| `OPENAI_KEY` | OpenAI API key used by the application |

Keep secrets in your local `.env` file. The `.env.example` file is a template and should contain placeholders only.
