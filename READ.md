# 🚚 Supply Chain Optimization and Forecasting Module

This project implements a Python-based module to solve supply chain optimization problems and generate demand forecasts. It focuses on:
- Optimizing transportation costs using **Linear Programming (PuLP)**
- Forecasting demand using **Exponential Smoothing** techniques

---

## 📁 Project Structure
- `main.py` — Integrates forecasting and optimization
- `forecasting.py` — Exponential smoothing for time-series demand
- `optimization.py` — Solves the Transportation Problem using PuLP

---

## 💡 Features
- Flexible input for supply, demand, and cost matrices
- Demand forecasting based on historical data
- Optimized transport routes with minimized cost
- Modular code for easy integration into larger systems

---

## 📦 Dependencies
- `pulp`
- `pandas`
- `numpy`
- `matplotlib`

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
python main.py
