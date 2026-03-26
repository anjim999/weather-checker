# AI Log

This document lists the prompts used to guide an AI assistant in building the parallel fetching, error handling, and personalization logic for the Weather Checker script.

### 1. Parallel Fetching Prompt
**Prompt Used:**
> "I have a list of orders in a JSON file, and I need to check the weather for each order's city using the OpenWeatherMap API in Python. I must do this concurrently, not one by one. Can you show me how to use `asyncio.gather` and `aiohttp` to fetch the weather for all cities in parallel, so the script runs as fast as possible?"

### 2. Error Handling & Resilience Prompts
**Prompt Used:**
> "One of my test cities is 'InvalidCity123', which will return an error from the API. How do I build resilience into my async python fetching function so that if a city doesn't exist, it logs a specific error without crashing the script? The rest of the valid cities must continue to resolve."

### 3. Golden Flow & AI Challenge Prompts
**Prompt Used:**
> "Use your AI capabilities to write a 'Weather-Aware Apology' Python function called `generate_apology`. It needs to take a customer's name, their city, and the weather condition (like Rain, Snow, or Extreme). If the weather is one of those conditions, generate a personalized message like: 'Hi Alice, your order to New York is delayed due to heavy rain. We appreciate your patience!'. Otherwise, it shouldn't produce a delay message."

### 4. Integration Prompt
**Prompt Used:**
> "Combine the `asyncio` fetching flow, the resilient error handling, and the `generate_apology` function. Loop through all the responses from `asyncio.gather`, print the apology if delayed, update the status field to 'Delayed' for those orders, and write the final updated records back into `orders.json`."
