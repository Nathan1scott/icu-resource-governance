# icu_api.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from icu_predictor import predictor, resource_manager, mock_patients, generate_mock_patients
import random

app = FastAPI(title="ICU Resource Governance API", description="AI-powered ICU bed allocation and patient risk prediction")

# Enable CORS for web dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "project": "ICU Resource Governance System",
        "status": "active",
        "features": ["Risk Prediction", "Bed Allocation", "Resource Monitoring", "Waitlist Management"]
    }

@app.get("/patients")
def get_all_patients():
    """Get all patients with their risk scores"""
    results = []
    for patient in mock_patients:
        risk = predictor.predict_icu_need(patient)
        results.append({
            "patient_id": patient["id"],
            "name": patient["name"],
            "age": patient["age"],
            "risk_score": risk["risk_score"],
            "risk_level": risk["risk_level"],
            "color": risk["color"],
            "requires_icu": risk["requires_icu"]
        })
    # Sort by risk score (highest first)
    results.sort(key=lambda x: x["risk_score"], reverse=True)
    return {"patients": results, "total": len(results)}

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    """Get detailed patient information with ICU prediction"""
    patient = next((p for p in mock_patients if p["id"] == patient_id), None)
    if not patient:
        return JSONResponse(status_code=404, content={"error": "Patient not found"})
    
    risk = predictor.predict_icu_need(patient)
    
    return {
        "patient": patient,
        "icu_prediction": risk,
        "recommendation": risk["recommended_action"]
    }

@app.get("/icu/availability")
def get_icu_availability():
    """Get current ICU bed availability"""
    return resource_manager.get_availability()

@app.get("/icu/allocate/{patient_id}")
def allocate_icu_bed(patient_id: str):
    """Allocate ICU bed to a patient"""
    patient = next((p for p in mock_patients if p["id"] == patient_id), None)
    if not patient:
        return JSONResponse(status_code=404, content={"error": "Patient not found"})
    
    risk = predictor.predict_icu_need(patient)
    allocation = resource_manager.allocate_bed(patient_id, risk["priority"])
    
    return {
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "risk_level": risk["risk_level"],
        "risk_score": risk["risk_score"],
        "priority": risk["priority"],
        "allocation": allocation
    }

@app.get("/icu/waitlist")
def get_icu_waitlist():
    """Get current ICU waitlist"""
    return {"waitlist": resource_manager.get_waitlist(), "count": len(resource_manager.pending_admissions)}

@app.get("/dashboard/summary")
def get_dashboard_summary():
    """Get complete dashboard summary"""
    patients = get_all_patients()
    availability = get_icu_availability()
    waitlist = get_icu_waitlist()
    
    # Calculate priority distribution
    risk_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for p in patients["patients"]:
        risk_counts[p["risk_level"]] += 1
    
    return {
        "icu_status": availability,
        "patient_summary": {
            "total": patients["total"],
            "requires_icu": sum(1 for p in patients["patients"] if p["requires_icu"]),
            "critical": risk_counts["critical"],
            "high": risk_counts["high"],
            "medium": risk_counts["medium"],
            "low": risk_counts["low"]
        },
        "waitlist_count": waitlist["count"],
        "alert_level": "red" if availability["occupancy_rate"] > 85 else ("orange" if availability["occupancy_rate"] > 70 else "green")
    }

@app.post("/refresh")
def refresh_data():
    """Refresh patient data with new random values"""
    global mock_patients
    mock_patients = generate_mock_patients()
    return {"message": "Data refreshed", "patient_count": len(mock_patients)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)