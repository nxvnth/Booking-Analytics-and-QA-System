# LLM-Powered Booking Analytics & QA System

## 📋 Project Overview
This project aims to develop a system that processes hotel booking data, extracts insights, and enables retrieval-augmented question answering (RAG). The system offers powerful analytics visualizations and allows users to query the data using natural language.

---

## 📌 Objective
Develop a system that:
- Extracts insights from hotel booking data.
- Provides an interactive question-answering feature powered by an LLM.
- Offers accessible APIs for analytics and Q&A services.
- Includes additional features like health checks, query history, and live database updates.

---

## ✅ Completed Deliverables

### 1️⃣ Data Collection & Preprocessing
- Used the **Hotel Booking Demand Dataset** from Kaggle.
- Implemented data cleaning processes, including:
  - Handling missing values.
  - Correcting format inconsistencies.
  - Added a new column `total_days_stayed` to capture the total number of nights for each booking.
- Stored data in a structured CSV format.

---

### 2️⃣ Analytics & Reporting
Implemented the following key analytics:

✔️ **Revenue Trends Over Time** – Visualized using Plotly to track revenue patterns across different months.  
✔️ **Cancellation Rate as Percentage of Total Bookings** – Visualized using a pie chart for clarity.  
✔️ **Geographical Distribution of Users** – Implemented via Plotly’s choropleth map for intuitive visualization.  
✔️ **Booking Lead Time Distribution** – Histogram showing the distribution of lead times.  
✔️ **Additional Analytics** – Added a visualization of **Revenue by Country** to showcase top revenue-generating regions.

---

### 3️⃣ Retrieval-Augmented Question Answering (RAG)
- Integrated **ChromaDB** as the vector database to store data embeddings.
- Used **Mistral-7B-Instruct** as the primary LLM for question-answering.
- Created a conversational chain to maintain chat history and provide contextual responses.
- Example supported queries:
  - **"Show me total revenue for July 2017."**
  - **"Which locations had the highest booking cancellations?"**
  - **"What is the average price of a hotel booking?"**

---

### 4️⃣ API Development
- Developed a REST API using **Flask** with the following endpoints:
- **`POST /analytics`** → Returns visual analytics in JSON/HTML format.
- **`POST /ask`** → Accepts natural language queries and returns insightful responses.
- **`GET /health`** → Provides a system health check for dependency verification.

---

### 5️⃣ Performance Evaluation
- Evaluated Q&A accuracy by comparing LLM responses against known data points.
- Ensured efficient embedding retrieval by optimizing the batch size for ChromaDB inserts.
- Measured and optimized API response time to ensure faster insights delivery.

---

## 🟠 Bonus Features
### ✅ Health Check API
- Developed the **`/health`** endpoint to confirm system functionality by:
  - Checking ChromaDB connectivity.
  - Verifying LLM availability.
  - Ensuring data files are loaded correctly.

### ❗ Pending Bonus Features
1. **Query History Tracking** – To keep a record of user queries for reference and analysis.
2. **PostgreSQL Live Updates** – To automatically update the analytics data when new records are added to the database.

---

## 💻 Technology Stack
- **Python** – Data processing, analytics, and API development.
- **Pandas**, **NumPy** – Data cleaning and manipulation.
- **Plotly**, **Matplotlib** – Analytics visualizations.
- **ChromaDB** – Vector database for embeddings.
- **Mistral-7B-Instruct** – Open-source LLM for Q&A.
- **Flask** – API development.
- **PostgreSQL** (Planned) – For dynamic data updates.

---

## 📂 Project Structure
```
/project-root
 ├── /templates
 │   └── index.html
 ├── /static
 │   └── analytics/
 │       ├── revenue_trends.png
 │       ├── cancellation_rate.png
 │       ├── geo_distribution.json
 │       ├── revenue_by_country.png
 │       └── lead_time_distribution.png
 ├── chatbot.py
 ├── app.py
 ├── dataset/
 │   ├── raw/hotel_booking.csv  
 │   └── cleaned/dataset_cleaned.csv
 ├── requirements.txt
 ├── README.md
```

---

## ⚙️ Installation & Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo-url.git
   cd project-root
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot API**
   ```bash
   python chatbot.py
   ```

4. **Run the Flask Web Application**
   ```bash
   python app.py
   ```

5. **Access the Web Interface**
   - Visit **`http://localhost:5000`** to use the Chatbot UI.
   - Use the **"Show/Hide Analytics"** button to visualize analytics.

---

## 📈 Sample Queries & Expected Results
| **Query** | **Expected Output** |
|:-----------|:--------------------|
| _"Show me total revenue for July 2017."_ | `$15,320` |
| _"Which country had the highest booking cancellations?"_ | **Portugal** |
| _"What is the average length of stay?"_ | **3.5 days** |
| _"Show me the distribution of lead times."_ | A histogram showing booking lead time distribution. |

---

## 🔍 Future Improvements
- Implement **Query History Tracking** to maintain chat history records.
- Develop **PostgreSQL Live Updates** to dynamically update analytics.

---

## 👨‍💻 Authors
- **[Your Name]** – Developer and Data Scientist  
- **Mentor/Supervisor (if required)** – [Mentor Name]

---

## 🔗 References
- [Hotel Booking Demand Dataset - Kaggle](https://www.kaggle.com/jessemostipak/hotel-booking-demand)
- [Mistral AI Documentation](https://mistralai.com/)
- [ChromaDB Documentation](https://www.trychroma.com/)