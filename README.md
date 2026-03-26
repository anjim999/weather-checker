# Weather Checker 🌦️

A high-performance Python application that monitors weather conditions for customer orders and automatically generates personalized apology messages for delays.

## 🚀 Features
- **Parallel Fetching**: Uses `asyncio` and `aiohttp` to fetch weather data for multiple cities concurrently.
- **Weather-Aware Logic**: Automatically detects conditions like Rain, Snow, and Extreme weather.
- **Personalized Apologies**: Dynamically generates customer-specific apology messages using an AI-inspired "Weather-Aware Apology" function.
- **Resilient Error Handling**: Gracefully handles invalid city names or API errors without interrupting the entire flow.
- **Persistent Data**: Updates order statuses and messages directly in `orders.json`.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anjim999/weather-checker.git
   cd weather-checker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory and add your OpenWeatherMap API key:
```env
OPENWEATHER_API_KEY=your_api_key_here
```

## 📂 Project Structure
- `weather.py`: Main application logic.
- `orders.json`: The database containing customer orders and status information.
- `requirements.txt`: Python package requirements.
- `ai_log.md`: History of prompts used to build this application.

## 🚦 Usage

Run the weather checker:
```bash
python weather.py
```

Check `orders.json` to see updated statuses and personalized messages!
