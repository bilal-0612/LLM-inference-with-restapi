import pandas as pd

# Load the CSV file
sales_data = pd.read_csv('sales_performance_data.csv')

# Function to load sales data for a specific representative
def get_sales_data_for_rep(rep_id):
    rep_data = sales_data[sales_data['employee_id'] == int(rep_id)]
    if rep_data.empty:
        return f"No data found for rep ID {rep_id}"
    return rep_data.to_dict(orient='records')

# Function to load the entire sales team's data
def get_team_sales_data():
    return sales_data.to_dict(orient='records')

# Function to load sales data for a specific time period
def get_sales_data_for_period(time_period):
    # Convert the 'dated' column to datetime
    sales_data['dated'] = pd.to_datetime(sales_data['dated'], format='%Y-%m-%d')
    
    # Filter based on time period (monthly, quarterly, etc.)
    if time_period == 'monthly':
        monthly_data = sales_data[sales_data['dated'].dt.to_period('M') == pd.to_datetime('today').to_period('M')]
        return monthly_data.to_dict(orient='records')
    elif time_period == 'quarterly':
        quarterly_data = sales_data[sales_data['dated'].dt.to_period('Q') == pd.to_datetime('today').to_period('Q')]
        return quarterly_data.to_dict(orient='records')
    else:
        return f"Unsupported time period: {time_period}"
