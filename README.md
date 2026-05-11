# 🏥 ICU Resource Governance System

AI-powered ICU bed allocation and patient risk prediction system.

## Features

- **Risk Score Calculation** (0-100 points)
  - Age: 0-20 points
  - Vital Signs: 0-30 points
  - Lab Values: 0-25 points
  - Comorbidities: 0-25 points

- **Risk Levels**
  - 🔴 CRITICAL (81-100): Immediate ICU transfer
  - 🟠 HIGH (61-80): ICU review within 2 hours
  - 🟡 MEDIUM (31-60): Monitor closely
  - 🟢 LOW (0-30): Ward-level care

- **ICU Bed Management**
  - Real-time availability tracking
  - Priority-based allocation
  - Waitlist management

## Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn pandas numpy

# Run the API
python icu_api.py

# Open icu_dashboard.html in your browser
