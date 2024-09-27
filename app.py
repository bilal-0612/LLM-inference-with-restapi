from flask import Flask, request, jsonify
from data_funccs import *
from prompts import *

app = Flask(__name__)

@app.route('/api/rep_performance', methods=['GET'])
def rep_performance():
    rep_id = request.args.get('rep_id')  # Get the rep_id from query params
    if not rep_id:
        return jsonify({"error": "rep_id parameter is missing"}), 400

    sales_data = get_sales_data_for_rep(rep_id)
    
    if isinstance(sales_data, str):
        return jsonify({"error": sales_data}), 404

    analysis = analyze_rep_performance(rep_id, sales_data)
    
    return jsonify({
        "rep_id": rep_id,
        "performance_analysis": analysis
    })


@app.route('/api/team_performance', methods=['GET'])
def team_performance():
    sales_data = get_team_sales_data()
    
    analysis = analyze_team_performance(sales_data)
    
    return jsonify({
        "team_performance_summary": analysis
    })

@app.route('/api/performance_trends', methods=['GET'])
def performance_trends():
    time_period = request.args.get('time_period') 
    if not time_period:
        return jsonify({"error": "time_period parameter is missing"}), 400

    sales_data = get_sales_data_for_period(time_period)
    
    if isinstance(sales_data, str):
        return jsonify({"error": sales_data}), 404

    analysis = analyze_performance_trends(time_period, sales_data)
    
    return jsonify({
        "time_period": time_period,
        "trends_analysis": analysis
    })

if __name__ == '__main__':
    app.run(debug=True)
