from flask import Flask, jsonify, render_template, request, render_template_string
from plotly.io import from_json
import json
import os
import requests
from chatbot import create_qa_chain, load_and_process_csv, create_or_load_vector_db
import time
from datetime import datetime

app = Flask(__name__)

# Load ChromaDB and chatbot on startup
csv_path = "dataset/cleaned/dataset_cleaned.csv"
docs = load_and_process_csv(csv_path)
vector_db = create_or_load_vector_db(docs)
qa_chain = create_qa_chain(vector_db)

# Chat history storage
chat_history = []

# API stats tracking
api_stats = {
    "status": "Online",
    "total_queries": 0,
    "response_times": [],
    "avg_response_time": 0,
    "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Helper function to get analytics data
def get_analytics_data():
    analytics_data = {
        'analytics_images': [],
        'captions': {},
        'plot_html': None
    }
    
    # Get image files
    try:
        analytics_data['analytics_images'] = [
            f for f in os.listdir("static/analytics") 
            if f.endswith((".png", ".jpg"))
        ]
        print(f"Found {len(analytics_data['analytics_images'])} analytics images")
    except Exception as e:
        print(f"Error loading analytics images: {e}")
    
    # Set captions
    analytics_data['captions'] = {
        "cancellation_rate.png": "Cancellation Rate as Percentage of Total Bookings",
        "revenue_trends.png": "Revenue Trends Over Time",
        "lead_time_distribution.png": "Booking Lead Time Distribution",
        "revenue_by_country.png": "Revenue by Country"
    }
    
    # Load plot
    try:
        with open("static/analytics/geo_distribution.json", "r") as f:
            fig_json = f.read()
        from plotly.io import from_json
        fig = from_json(fig_json)
        analytics_data['plot_html'] = fig.to_html(full_html=False)
    except Exception as e:
        print(f"Error loading plot data: {e}")
    
    return analytics_data

def update_api_stats(response_time_ms):
    api_stats["total_queries"] += 1
    api_stats["response_times"].append(response_time_ms)
    
    # Keep only the last 100 response times to avoid memory issues
    if len(api_stats["response_times"]) > 100:
        api_stats["response_times"] = api_stats["response_times"][-100:]
    
    # Calculate average response time
    api_stats["avg_response_time"] = round(sum(api_stats["response_times"]) / len(api_stats["response_times"]), 2)
    api_stats["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route('/')
def index():
    # Render the template without data initially
    return render_template("index.html")

@app.route('/get_data')
def get_data():
    # Get analytics data
    analytics_data = get_analytics_data()
    
    # Return both chat history and analytics data as JSON
    return jsonify({
        "chat_history": chat_history,
        "api_stats": api_stats,
        **analytics_data
    })

@app.route('/api_stats')
def get_api_stats():
    return jsonify(api_stats)

@app.route('/chat', methods=['POST'])
def chat():
    start_time = time.time()
    user_input = request.form.get("user_input")

    if not user_input:
        bot_response = "Please enter a valid prompt."
    else:
        try:
            response = qa_chain.invoke({"question": user_input})
            bot_response = response['answer']
        except Exception as e:
            bot_response = f"An error occurred: {str(e)}"
            # Update API status to reflect error
            api_stats["status"] = "Degraded"

    # Calculate response time in milliseconds
    response_time_ms = round((time.time() - start_time) * 1000, 2)
    
    # Update API stats
    update_api_stats(response_time_ms)
    
    # Add chat to history with response time
    chat_history.append({
        "user": user_input, 
        "bot": bot_response, 
        "response_time_ms": response_time_ms,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    # Get analytics data for consistent rendering
    analytics_data = get_analytics_data()
    return render_template(
        "index.html", 
        chat_history=chat_history,
        api_stats=api_stats,
        **analytics_data
    )

# Show analytics functionality - no longer needed as a separate route
# but keeping for backward compatibility
@app.route('/show-analytics')
def show_analytics():
    analytics_data = get_analytics_data()
    return render_template(
        "index.html", 
        chat_history=chat_history,
        **analytics_data
    )

@app.route('/health')
def health_check():
    try:
        # Simple test to verify vector database is working
        vector_db.similarity_search("test", k=1)
        api_stats["status"] = "Online"
    except Exception as e:
        api_stats["status"] = "Degraded"
        print(f"Health check failed: {e}")
    
    return jsonify({"status": api_stats["status"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)