import openai

"""
Contains the prompts that would be later 
"""



openai.api_key = 'your-api-key'

def analyze_rep_performance(rep_id, sales_data):
    prompt = f"""
    You are an expert sales analyst. Based on the following sales data, provide a comprehensive analysis of the performance of the sales representative with ID {rep_id}. 
    Consider the following in your analysis:
    - Historical sales performance (revenue, number of deals closed, client acquisition rate)
    - Comparisons to team averages and top performers
    - Strengths and areas for improvement in the sales process (e.g., lead conversion, closing skills)
    - Recommendations for improving performance in the next quarter, including training or focus areas.

    Sales Data:
    {sales_data}
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600
    )
    return response.choices[0].text.strip()

def analyze_team_performance(sales_data):
    prompt = f"""
    You are an experienced sales consultant. Based on the following sales team data, provide a detailed analysis of the overall team's performance. 
    Consider these factors:
    - Revenue generation across the team and individual contributions
    - Trends in team-wide metrics (e.g., overall win rate, deal sizes, and lead generation)
    - Comparison with last quarter’s performance and industry benchmarks
    - Identification of any bottlenecks or challenges the team is facing (e.g., long sales cycles, high lead drop-off rates)
    - Specific strategies to improve team collaboration, performance, and morale for the next quarter.

    Sales Team Data:
    {sales_data}
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600
    )
    return response.choices[0].text.strip()

def analyze_performance_trends(time_period, sales_data):
    prompt = f"""
    You are a data-driven sales strategist. Analyze the sales performance trends for the time period '{time_period}' based on the following sales data. 
    Please include in your analysis:
    - Key trends in sales performance (e.g., growth or decline in revenue, customer acquisition, deal sizes)
    - Significant fluctuations during the time period and potential causes (e.g., market changes, sales campaigns)
    - Predictive analysis for future performance, based on the observed trends
    - Risks and opportunities to watch out for in the upcoming period
    - Recommendations for how the sales team should adjust strategy to capitalize on positive trends or mitigate potential risks.

    Sales Data for the period '{time_period}':
    {sales_data}
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600
    )
    return response.choices[0].text.strip()
