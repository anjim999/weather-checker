import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

# Load API key from securely stored .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

async def fetch_weather(session, order):
    """Fetch weather data for a single city asynchronously."""
    city = order["city"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        # Make the API request
        async with session.get(url) as response:
            data = await response.json()
            if data.get("cod") != 200:
                raise Exception(f"City not found: {city}")
            weather_main = data["weather"][0]["main"]
            
            # DEMO OVERRIDE: Force 'Rain' for London so you can record the delayed apology message!
            if city == "London":
                weather_main = "Rain"
            
            print(f"✅ {city}: {weather_main}")
            return {"order": order, "weather": weather_main, "error": None}
    except Exception as e:
        # Catch errors gracefully (e.g., InvalidCity123) without crashing
        print(f"❌ ERROR for {city}: {e}")
        return {"order": order, "weather": None, "error": str(e)}

def generate_apology(customer, city, weather):
    """AI Challenge: Generate a personalized apology message based on weather."""
    messages = {
        "Rain": f"Hi {customer}, your order to {city} is delayed due to heavy rain. We appreciate your patience!",
        "Snow": f"Hi {customer}, your order to {city} is delayed due to heavy snowfall. We appreciate your patience!",
        "Extreme": f"Hi {customer}, your order to {city} is delayed due to extreme weather conditions. We appreciate your patience!"
    }
    return messages.get(weather, "")

async def main():
    # 1. Load the database (orders.json)
    with open("orders.json", "r") as f:
        orders = json.load(f)

    # 2. Fetch all city weather data concurrently using asyncio
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, order) for order in orders]
        results = await asyncio.gather(*tasks)

    delay_conditions = ["Rain", "Snow", "Extreme"]

    # 3. Process the results and update statuses
    for result in results:
        order = result["order"]
        if result["error"]:
            print(f"\n⚠️ Skipping {order['city']} due to error: {result['error']}")
            continue
        weather = result["weather"]
        
        # Golden Flow Logic: Update status if delayed
        if weather in delay_conditions:
            order["status"] = "Delayed"
            # Generate the personalized apology
            message = generate_apology(order["customer"], order["city"], weather)
            print(f"\n💬 Apology for {order['customer']}: {message}")
        else:
            print(f"\n✅ {order['city']} is clear - no delay")

    # 4. Save the updated statuses back to orders.json
    with open("orders.json", "w") as f:
        json.dump(orders, f, indent=2)

    print("\n✅ orders.json updated successfully!")

asyncio.run(main())