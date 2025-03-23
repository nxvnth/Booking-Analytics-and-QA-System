# LLM-Powered Booking Analytics & QA System

![Alt text](resources/home.png?raw=true "Landing Page")
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
  - Added new columnS `total_days_stayed` AND `total_revenue`to capture the total number of nights for each booking.
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
- Used **Mistral-Large-Instruct-2407** as the primary LLM for question-answering.
- Created a conversational chain to maintain chat history and provide contextual responses.
- Example supported queries:
  - **"Show me total revenue the hotel has generated."**
  - **"Which locations had the highest booking cancellations?"**
  - **"What is the average price of a hotel booking?"**

---

### 4️⃣ API Development
- Developed a REST API using **Flask** with the following endpoints:
- **`POST /analytics`** → Returns visual analytics in JSON/HTML format.
- **`POST /chat`** → Accepts natural language queries and returns insightful responses.
- **`GET /health`** → Provides a system health check for dependency verification.
- **`GET /get_data`** → Provides both chat history and analytics data as JSON.

---

### 5️⃣ Performance Evaluation
- Evaluated Q&A accuracy by comparing LLM responses against known data points.
- Ensured efficient embedding retrieval by optimizing the batch size for ChromaDB inserts.
- Measured and optimized API response time to ensure faster insights delivery.
- `Main issues that were encountered were expected; the llm cannot handle the retreival and processing of all the 100000+ records. The maximum tested number of records that can be extracted without compramising on response time and tokens per request limit is 10 (controlled by the search_kwargs k parameter in retreiver)`


---

## 🟠 Bonus Features
### ✅ Health Check API
- Developed the **`/health`** endpoint to confirm system functionality by:
  - Checking ChromaDB connectivity.
  - Verifying LLM availability.
  - Ensuring data files are loaded correctly.

---

### ❗ Pending Features
1. **Query History Tracking** – To keep a record of user queries for reference and analysis.
2. **PostgreSQL Live Updates** – To automatically update the analytics data when new records are added to the database.
3. **Enhancing RAG** - To add more fields to the dataset to minimize computations so that llm can just focus on retrieval.
4. **Fixing geo-distribution graph** - To fix the issue where the interactive geo-distribution graph doesn't appear.

---

## 💻 Technology Stack
- **Python** – Data processing, analytics, and API development.
- **Pandas**, **NumPy** – Data cleaning and manipulation.
- **Plotly**, **Matplotlib**,**Seaborn** – Analytics visualizations.
- **ChromaDB** – Vector database for embeddings.
- **Mistral-7B-Instruct** – Open-source LLM for Q&A.
- **Flask** – API development.
- **Basic HTML** - Frontend to visualize API results.
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

3. **API credentials and .env setup**
- Obtain valid api secret key from the official mistral ai website and create a .env file containing the secret key.

4.  **(Optional - Just to check rate limits and if RAG works as expected ) Run the Chatbot API**
   ```bash
   python chatbot.py
   ```

5. **Run the Flask Web Application**
   ```bash
   python app.py
   ```

6. **Access the Web Interface**
   - Visit **`http://localhost:5000`** to use the Chatbot UI.
   - Use the **"Show/Hide Analytics"** button to visualize analytics.

---

## 📈 Sample Queries & Expected Results
Once the Chroma embeddings have been updated it should be able to answer the following queries withing the limits mentioned in performance evaluation.
| **Query** | **Expected Output** |
|:-----------|:--------------------|
| _"Show me total revenue."_ | `$xxx` |
| _"Which country had the highest booking cancellations?"_ | **ABC** |
| _"What is the average length of stay?"_ | **x days** |

---

## 🔍 Future Improvements
- Implement **Query History Tracking** to maintain chat history records.
- Develop **PostgreSQL Live Updates** to dynamically update analytics.
- Enhancing RAG and Dataset manipulation

---

## 🔗 References
- [Hotel Booking Demand Dataset - Kaggle](https://www.kaggle.com/jessemostipak/hotel-booking-demand)
- [Mistral AI Documentation](https://mistralai.com/)
- [ChromaDB Documentation](https://www.trychroma.com/)
