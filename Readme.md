
# Test Project Submission

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bilal-0612/LLM-inference-with-restapi
   cd LLM-inference-with-restapi
   ```

2. Install the dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Running

1. Open the `prompts.py` file and replace `'your-api-key'` in the code with your actual OpenAI API key:
   ```python
   openai.api_key = 'your-api-key'
   ```

2. Run the `app.py` file from your terminal:
   ```bash
   python app.py
   ```

3. The Flask application will start running on `http://localhost:5000`, and you can test the API endpoints using Postman or Insomnia.

## API Endpoints

- `/api/rep_performance`: Provides performance analysis for a specific sales representative.
- `/api/team_performance`: Gives an overview of the entire sales team's performance.
- `/api/performance_trends`: Returns performance trends and forecasting based on the time period.

Make sure your sales data CSV file is located in the project folder for the APIs to function correctly.
