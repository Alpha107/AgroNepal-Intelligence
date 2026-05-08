# AgroNepal Intelligence: AI-Powered Agricultural Decision Support System for Nepal

AgroNepal Intelligence is an AI-driven agricultural intelligence platform designed to support data-informed farming decisions across all 77 districts of Nepal. The system combines satellite-based climate data, machine learning, and interactive geographic visualization to analyze regional agricultural conditions and recommend suitable crops based on district-level environmental patterns.

The platform aims to bridge the gap between modern data science technologies and practical agricultural planning by transforming complex climate datasets into understandable and actionable insights.

---

**Project Objectives**
* Analyze long-term climate conditions across Nepal
* Provide district-specific crop recommendations
* Visualize agricultural and environmental data interactively
* Support sustainable and climate-aware farming decisions
* Demonstrate the application of AI and data engineering in agriculture

---

**Key Features**

### Interactive District Intelligence Map
* Interactive map of all 77 districts of Nepal using Leaflet.js
* District highlighting and tooltip-based insights
* Geographic climate and agricultural visualization

### ASA POWER Climate Data Integration
The platform integrates historical weather and environmental data from NASA POWER API including:
* Temperature
* Precipitation
* Humidity
This enables localized climate profiling for agricultural analysis.

### Machine Learning-Based Crop Recommendation
A Random Forest Classifier is used to predict the most suitable crops for each district based on:
* Climate conditions
* Rainfall patterns
* Humidity levels
* Ecological characteristics

The system recommends:
* Top suitable crops
* Companion planting combinations
* Climate-related agricultural risks

### Climate Trend Analysis
The dashboard provides:
* 10-year rainfall trends
* Temperature change visualization
* Historical climate comparisons
Interactive charts are built using **Recharts** for intuitive analysis.

### Agricultural Resource Insights
The platform includes:
* Irrigation coverage tracking
* Agricultural land availability indicators
* Regional agricultural summaries

---

**Why This Project Was Built**

Agriculture remains one of the most important sectors in Nepal, yet many farming decisions are still heavily dependent on traditional methods and inconsistent environmental conditions.

With increasing climate variability and limited access to localized agricultural intelligence, farmers often lack reliable decision-support tools.

This project was built to explore how:
* Artificial Intelligence
* Climate Data
* Geographic Information Systems
* Data Visualization
can be combined to create a practical agricultural intelligence system tailored for Nepal.

---

**System Architecture**
```text
NASA POWER API
        ↓
Climate Data Collection
        ↓
Data Cleaning & Processing
        ↓
Feature Engineering
        ↓
Random Forest ML Model
        ↓
FastAPI Backend
        ↓
Interactive Frontend Dashboard
        ↓
District-Level Agricultural Insights
```

---

**Tech Stack**

**Frontend**
* React (Vite)
* Leaflet.js
* Recharts
* HTML/CSS

**Backend**
* FastAPI
* Python

**Machine Learning & Data Processing**
* Scikit-learn
* Pandas
* NumPy

**Data Sources**
* NASA POWER API
* Nepal District GeoJSON Data

---

**Machine Learning Pipeline**
1. Climate data collection from NASA POWER API
2. Data preprocessing and normalization
3. Feature extraction from environmental variables
4. Model training using Random Forest Classifier
5. District-level crop prediction and recommendation generation

---

**Why Random Forest?**
* Performs well on structured environmental datasets
* Handles nonlinear relationships effectively
* Reduces overfitting risk
* Provides stable predictions across varying climate conditions
* Works efficiently with mixed agricultural variables

---

**Project Structure**
```text
AgroNepal-Intelligence/
│
├── main.py
├── seed_districts.py
├── index.html
├── README.md
│
├── frontend/
│   ├── components/
│   ├── assets/
│   └── charts/
│
├── backend/
│   ├── api/
│   ├── models/
│   └── services/
│
├── datasets/
│
└── screenshots/
```

---

**Installation & Setup**

### Prerequisites
* Python 3.9+
* Node.js 16+
* npm or yarn

### Backend Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alpha107/AgroNepal-Intelligence.git
   ```
2. **Navigate to backend:**
   ```bash
   cd backend
   ```
3. **Create virtual environment:**
   * **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Initialize data:**
   ```bash
   python seed_districts.py
   ```
6. **Run backend server:**
   ```bash
   python main.py
   ```
   *Backend runs at: `http://localhost:8000`*

### Frontend Setup
1. **Navigate to frontend:**
   ```bash
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Run development server:**
   ```bash
   npm run dev
   ```
   *Frontend runs at: `http://localhost:5173`*

---

**Screenshots**

### Dashboard Overview
<img width="1848" height="845" alt="Dashboard Overview" src="https://github.com/user-attachments/assets/62d1240e-126c-488e-b7b6-f59cf2687810" />

### District Intelligence View
<img width="1857" height="817" alt="District Intelligence" src="https://github.com/user-attachments/assets/13af9be1-4bd0-4d69-96fc-725f0f7e9ad5" />

### Climate Trend Analysis
<img width="1267" height="655" alt="Climate Trends" src="https://github.com/user-attachments/assets/4df70a3f-e17a-4f5e-8342-1a16f7001508" />

### Crop Recommendation Panel
<img width="1201" height="793" alt="Crop Recommendation" src="https://github.com/user-attachments/assets/58c7b24c-97d1-4f93-9442-6e0e012f6d4e" />

---

**Potential Real-World Applications**
* Smart agricultural planning
* Climate-aware crop recommendation
* Agricultural research support
* Government-level agricultural analytics
* Rural technology initiatives
* Educational and research demonstrations

---

**Current Limitations**
* Recommendations are currently district-level only
* No real-time IoT sensor integration yet
* Crop prediction depends on available climate datasets
* Soil quality analysis is limited
* Requires internet access for external API data

---

**Future Improvements**
* IoT-based live soil monitoring
* Satellite imagery integration
* Deep learning climate forecasting
* Mobile application support
* Nepali-language farmer interface
* AI chatbot for agricultural guidance
* Cloud deployment and scalability improvements

---

**Contributing**
Contributions, ideas, and improvements are welcome.
If you would like to contribute:
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Submit a pull request

---

**License**
This project is licensed under the MIT License.

---

**Author**
**Abashesh Ranabhat**
Computer Engineer | AI & Robotics Enthusiast | ML Practitioner

[GitHub](https://github.com/Alpha107) | [LinkedIn](https://www.linkedin.com/in/abashesh-ranabhat/)

---

**Final Note**

AgroNepal Intelligence represents the intersection of Artificial Intelligence, Climate Science, Geographic Intelligence, and Agricultural Technology with the goal of building smarter, more accessible, and data-driven agricultural systems for Nepal.
