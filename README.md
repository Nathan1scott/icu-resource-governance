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
