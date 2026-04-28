# 🌱 AgroNepal AI: Advanced Agricultural Intelligence Dashboard

AgroNepal AI is a high-precision, data-driven agricultural intelligence platform designed to empower farmers, policy-makers, and agricultural researchers in Nepal. By integrating real-time weather data from the **NASA POWER API** with **Machine Learning (Random Forest)**, the platform provides tailored crop suitability insights for all 77 districts of Nepal.

---

<img width="1848" height="845" alt="Screenshot 2026-04-28 110607" src="https://github.com/user-attachments/assets/62d1240e-126c-488e-b7b6-f59cf2687810" />

---

<img width="1857" height="817" alt="Screenshot 2026-04-28 110618" src="https://github.com/user-attachments/assets/13af9be1-4bd0-4d69-96fc-725f0f7e9ad5" />

---

## 💡 The Inspiration Behind AgroNepal AI

Nepal is fundamentally an agricultural nation, with a large majority of our population depending on farming for their livelihood. Despite this deep agricultural heritage, our farmers frequently struggle with unpredictable weather patterns, the undeniable impacts of climate change, and a lack of localized, data-driven insights. Traditional farming knowledge is invaluable, but it is increasingly being challenged by rapidly shifting ecological conditions.

**The Driving Idea:** 
I noticed a massive gap between the advanced technologies available today (like Machine Learning and satellite data) and the tools actually accessible to Nepali agriculture. The driving force behind AgroNepal AI was a simple question: *How can we democratize high-level environmental data and make it actionable for Nepal?* 

I wanted to build a bridge, a tool that doesn't just display weather numbers, but actively translates that data into practical, strategic advice. By leveraging NASA's POWER API and training a Random Forest model on ecological zones, the goal was to create an intuitive dashboard that tells you exactly what crops will thrive in your specific district, what companion plants to use, and what climate risks to anticipate.

## 🚀 Key Features

- **📍 Interactive District Intelligence**: A professional Leaflet-based map of Nepal's 77 districts with high-fidelity glassmorphism tooltips and district spotlighting.
- **🛰️ NASA POWER API Integration**: Real-time historical weather data ingestion (Temperature, Precipitation, Humidity) for precise local climate profiling.
- **📈 10-Year Climate Trends**: Visual 10-year historical analysis (2014-2024) featuring Line and Area charts for long-term rainfall and temperature shifts.
- **🤖 AI-Driven Crop Suitability**: A Random Forest ML model trained on ecological zone data to recommend the Top 5 most viable crops per district.
- **💧 Irrigation & Resource Tracking**: Dynamic tracking of irrigation coverage percentage and available agricultural land reserves.
- **📋 "Pro-Tier" Bento Reports**: Comprehensive, modular intelligence briefings featuring AI reasoning, companion planting synergy, and risk mitigation strategies.

## 🛠️ Tech Stack

### Frontend
- **React (Vite)**: Ultra-fast component-based architecture.
- **Leaflet.js**: High-performance interactive map rendering.
- **Recharts**: Professional-grade data visualization for climate trends.
- **Vanilla CSS**: Custom glassmorphism design system with the **Outfit** and **Inter** font families.

### Backend
- **FastAPI**: Modern, high-performance Python web framework.
- **Scikit-learn**: Random Forest Classifier for agricultural intelligence.
- **Pandas/NumPy**: Large-scale data processing and cleaning.
- **NASA POWER API**: Real-world satellite-based weather data.

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9+
- Node.js 16+
- NPM or Yarn

### 1. Backend Setup
1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```
2. **Create and activate a virtual environment:**
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Initialize data (GeoJSON & ML Model):**
   ```bash
   python seed_districts.py
   ```
5. **Start the API Server:**
   ```bash
   python main.py
   ```
   *The backend will be running at `http://localhost:8000`. You can verify it by visiting `http://localhost:8000/api/health`.*

### 2. Frontend Setup
1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Start the development server:**
   ```bash
   npm run dev
   ```
   *The frontend will be available at `http://localhost:5173`.*

---

## 🚦 Quick Verification
- **Backend Health Check**: Open [http://localhost:8000/api/health](http://localhost:8000/api/health) (Should show `{"status": "ok"}`)
- **Frontend Dashboard**: Open [http://localhost:5173](http://localhost:5173)

## 🧠 The AI Model

The **AgroNepal Intelligence Engine** uses a Random Forest Classifier trained on multidimensional climate vectors:
- **Temperature Profile**: Multi-year seasonal averages.
- **Annual Precipitation**: Normalized rainfall patterns.
- **Soil pH Correlation**: District-specific acidity/alkalinity profiles.
- **Humidity & Moisture**: Atmospheric moisture tracking.

The model doesn't just predict crops; it analyzes **Ecological Synergies** to suggest companion planting (e.g., *Maize + Beans*) and identifies **Risk Hazards** like frost or drought trends.

## 🗺️ Data Sources
- **Map Boundaries**: High-resolution GeoJSON for Nepal's 77 districts.
- **Climate Data**: NASA Prediction Of Worldwide Energy Resources (POWER).
- **Agricultural Logic**: Expert-vetted ecological zone crop mapping.

## Images

<img width="1318" height="802" alt="Screenshot 2026-04-28 110627" src="https://github.com/user-attachments/assets/79a420c7-397e-4502-b679-fc9a84ed1206" />

---

<img width="1251" height="566" alt="Screenshot 2026-04-28 110649" src="https://github.com/user-attachments/assets/fc6e679c-a19a-4a1a-a084-84483b44b13c" />

---

<img width="1267" height="655" alt="Screenshot 2026-04-28 110656" src="https://github.com/user-attachments/assets/4df70a3f-e17a-4f5e-8342-1a16f7001508" />

---

<img width="1249" height="552" alt="Screenshot 2026-04-28 110704" src="https://github.com/user-attachments/assets/77204b35-dc4c-435f-9b5b-443eac926890" />

---

<img width="1201" height="793" alt="Screenshot 2026-04-28 110714" src="https://github.com/user-attachments/assets/58c7b24c-97d1-4f93-9442-6e0e012f6d4e" />

---

<img width="1084" height="672" alt="Screenshot 2026-04-28 110722" src="https://github.com/user-attachments/assets/f9693444-8a75-4c69-b167-cb164a2066c3" />

---

## 🤝 Contributing
Contributions are welcome! If you'd like to improve the AI model or add new features, please fork the repository and submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
*Built for a more prosperous agricultural future of Nepal by Abashesh Ranabhat.*
