<h1 align="center">🌾 AgroNepal Intelligence</h1>

<p align="center">Climate data + machine learning → crop recommendations for all 77 districts of Nepal, on an interactive map.</p>

<p align="center">
  <img src="https://img.shields.io/badge/backend-FastAPI-009688" alt="FastAPI">
  <img src="https://img.shields.io/badge/frontend-React%20%2B%20Leaflet-61dafb" alt="React Leaflet">
  <img src="https://img.shields.io/badge/ML-Random%20Forest-orange" alt="Random Forest">
  <img src="https://img.shields.io/badge/repo-partial%20upload-yellow" alt="Partial">
</p>

<p align="center"><img src="https://github.com/user-attachments/assets/62d1240e-126c-488e-b7b6-f59cf2687810" width="860" alt="Dashboard"></p>

> **Partial upload.** The screenshots show the working app, but this repo only has the API entry point
> and the HTML shell. The ML pipeline, React source and datasets aren't committed yet.
> [Details →](#status--known-issues)

## Features

| | |
|---|---|
| 🗺️ **District map** | All 77 districts (Leaflet), hover insights |
| 🌦️ **Climate profile** | Temperature, rainfall and humidity history from the **NASA POWER** API |
| 🌱 **Crop recommendation** | Random Forest on climate and ecology features → top crops, companion planting, climate risks |
| 📈 **Trends** | 10-year rainfall and temperature charts (Recharts) |
| 💧 **Resources** | Irrigation coverage and farmland indicators |

<table>
  <tr>
    <td width="33%"><img src="https://github.com/user-attachments/assets/13af9be1-4bd0-4d69-96fc-725f0f7e9ad5" alt="District"><br><sub>District intelligence</sub></td>
    <td width="33%"><img src="https://github.com/user-attachments/assets/4df70a3f-e17a-4f5e-8342-1a16f7001508" alt="Trends"><br><sub>Climate trends</sub></td>
    <td width="33%"><img src="https://github.com/user-attachments/assets/58c7b24c-97d1-4f93-9442-6e0e012f6d4e" alt="Crops"><br><sub>Crop recommendation</sub></td>
  </tr>
</table>

## How it works

```mermaid
flowchart LR
    N["NASA POWER API"] --> C["Clean + feature<br/>engineering"]
    C --> M["Random Forest"]
    G["District GeoJSON"] --> A
    M --> A["FastAPI<br/>/api/districts · /api/insights/{d}"]
    A --> U["React dashboard<br/>Leaflet + Recharts"]
```

## In this repo

| File | What it does |
|---|---|
| `main.py` | FastAPI app: `/api/health`, `/api/districts` (GeoJSON), `/api/insights/{district}` |
| `seed_districts.py` | Downloads Nepal's district GeoJSON into `data/` |
| `index.html` | Vite entry page for the React app |

```bash
pip install fastapi uvicorn
python seed_districts.py           # fetches data/nepal_districts.geojson
python main.py                     # needs ml_pipeline/ (not yet committed)
```

## Status & known issues

| Issue | Effect |
|---|---|
| `ml_pipeline` (the recommender) isn't in the repo | `main.py` fails at import |
| React `src/`, datasets and trained model are missing | The frontend can't be built from this repo |
| Old docs listed `frontend/`, `backend/`, `datasets/` folders | They don't exist here yet |
| CORS allows `*` | Fine for local use; restrict before deploying |
| Recommendations come from climate only | No soil, market-price or irrigation-access data |

## Roadmap

- [ ] Commit `ml_pipeline/`, React source, a `requirements.txt` and a sample dataset
- [ ] Soil (SoilGrids) and market-price features
- [ ] Nepali-language UI; mobile view for field use
