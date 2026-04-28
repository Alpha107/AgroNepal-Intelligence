# 🌱 AgroNepal AI: Advanced Agricultural Intelligence Dashboard

AgroNepal AI is a high-precision, data-driven agricultural intelligence platform designed to empower farmers, policy-makers, and agricultural researchers in Nepal. By integrating real-time weather data from the **NASA POWER API** with **Machine Learning (Random Forest)**, the platform provides tailored crop suitability insights for all 77 districts of Nepal.

![Dashboard Preview](https://via.placeholder.com/1200x600/0f172a/10b981?text=AgroNepal+AI+Strategic+Intelligence)

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

## 🤝 Contributing
Contributions are welcome! If you'd like to improve the AI model or add new features, please fork the repository and submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
*Built for a more prosperous agricultural future in Nepal.*