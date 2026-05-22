# 🛏️ ICU Resource Governance System

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-red)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI-brightgreen)](https://github.com/Nathan1scott)

> An AI-powered ICU bed allocation and patient risk prediction system. Helps hospitals prioritize critical patients and optimize intensive care resources.

---

## 📋 Problem Statement

ICU beds are a scarce and expensive resource. During crises (pandemics, flu seasons, natural disasters), demand often exceeds supply. Without standardized prioritization:

- 🔴 **Critical patients may wait too long** for admission
- 🟡 **Low-risk patients may occupy beds** needed for emergencies
- 📊 **Decisions are subjective** without objective risk scores
- ⏰ **Waitlists are managed manually** leading to delays

**The Solution:** An AI system that objectively scores patient risk, prioritizes ICU admission, and provides transparent resource allocation.

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Patient Risk Scoring** | Calculates risk score (0-100) based on clinical factors |
| **Risk Level Classification** | Categorizes as Critical/High/Medium/Low |
| **ICU Bed Availability** | Real-time tracking of total, occupied, and available beds |
| **Priority-Based Allocation** | Critical patients get immediate admission |
| **Waitlist Management** | Transparent queue with estimated wait times |
| **Resource Dashboard** | Visualize occupancy rates and patient distribution |
| **Mobile Responsive** | Works on phones, tablets, and desktops |
| **Auto-Refresh** | Real-time updates every 30 seconds |

---

## 📊 Risk Score Calculation

The risk score (0-100) is calculated using a weighted algorithm based on established clinical criteria (NEWS2, MEWS, qSOFA):


### Risk Level Classification

| Risk Level | Score Range | Action Required | Color |
|------------|-------------|-----------------|-------|
| 🔴 **CRITICAL** | 81-100 | Immediate ICU transfer | Red |
| 🟠 **HIGH** | 61-80 | ICU review within 2 hours | Orange |
| 🟡 **MEDIUM** | 31-60 | Monitor closely, consider HDU | Yellow |
| 🟢 **LOW** | 0-30 | Ward-level care appropriate | Green |

### Scoring Factors

| Factor | Weight | Clinical Rationale |
|--------|--------|---------------------|
| **Age** | 0-20 points | Older age increases mortality risk |
| **Systolic BP** | 0-15 points | Hypotension indicates shock |
| **Heart Rate** | 0-10 points | Tachycardia suggests distress |
| **Respiratory Rate** | 0-10 points | Tachypnea indicates respiratory failure |
| **O2 Saturation** | 0-15 points | Hypoxia requires respiratory support |
| **Lactate** | 0-15 points | Elevated lactate indicates tissue hypoperfusion |
| **WBC Count** | 0-10 points | Abnormal WBC suggests infection |
| **Comorbidities** | 0-15 points | Multiple conditions increase complexity |

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Backend** | FastAPI, Python |
| **Frontend** | HTML, CSS, JavaScript |
| **Risk Algorithm** | Weighted clinical scoring (NEWS2-based) |
| **Data Generation** | Python random with realistic clinical ranges |
| **Containerization** | Docker-ready |

---

## 📊 Data Source

### Synthetic Patient Generation

All patient data is **synthetically generated** for demonstration:

| Attribute | Clinical Range | Source |
|-----------|----------------|--------|
| Age | 18-92 years | Realistic population distribution |
| Blood Pressure | 70-160 mmHg | Normal to critical range |
| Heart Rate | 60-150 bpm | Bradycardia to tachycardia |
| Respiratory Rate | 12-35/min | Normal to severe distress |
| O2 Saturation | 85-100% | Hypoxia to normal |
| Lactate | 0.5-8.0 mmol/L | Normal to severe shock |
| WBC Count | 3,000-25,000 cells/μL | Leukopenia to leukocytosis |

> *This is synthetic data. In production, connect to real EHR systems.*

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Nathan1scott/icu-resource-governance.git
cd icu-resource-governance

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
python icu_api.py
