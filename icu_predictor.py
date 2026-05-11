# icu_predictor.py
import random
import numpy as np
from datetime import datetime, timedelta

class ICURiskPredictor:
    """Predicts patient deterioration risk and ICU need"""
    
    def __init__(self):
        self.risk_levels = {
            "critical": {"score": 81, "color": "#dc3545", "action": "Immediate ICU transfer required", "priority": 1},
            "high": {"score": 61, "color": "#fd7e14", "action": "ICU review within 2 hours", "priority": 2},
            "medium": {"score": 31, "color": "#ffc107", "action": "Monitor closely, consider HDU", "priority": 3},
            "low": {"score": 0, "color": "#28a745", "action": "Ward-level care appropriate", "priority": 4}
        }
    
    def calculate_risk_score(self, patient_data):
        """Calculate risk score based on multiple clinical factors"""
        score = 0
        
        # Age factor (0-20 points)
        age = patient_data.get('age', 50)
        if age > 80:
            score += 20
        elif age > 70:
            score += 15
        elif age > 60:
            score += 10
        elif age > 50:
            score += 5
        
        # Vital signs factors (0-30 points)
        sbp = patient_data.get('sbp', 120)
        if sbp < 90:
            score += 15
        elif sbp < 100:
            score += 10
        
        hr = patient_data.get('hr', 80)
        if hr > 130:
            score += 10
        elif hr > 110:
            score += 5
        
        rr = patient_data.get('rr', 16)
        if rr > 25:
            score += 10
        elif rr > 20:
            score += 5
        
        o2 = patient_data.get('o2_sats', 98)
        if o2 < 90:
            score += 15
        elif o2 < 94:
            score += 10
        
        # Lab factors (0-25 points)
        lactate = patient_data.get('lactate', 1.0)
        if lactate > 4:
            score += 15
        elif lactate > 2:
            score += 10
        
        wbc = patient_data.get('wbc', 8000)
        if wbc > 15000 or wbc < 4000:
            score += 10
        
        # Comorbidity factors (0-25 points)
        conditions = patient_data.get('num_conditions', 0)
        score += min(conditions * 2, 15)
        
        if patient_data.get('recent_surgery', False):
            score += 10
        
        if patient_data.get('on_ventilator', False):
            score += 20
        
        return min(score, 100)
    
    def get_risk_level(self, score):
        """Get risk level based on score"""
        if score >= 80:
            return "critical"
        elif score >= 60:
            return "high"
        elif score >= 30:
            return "medium"
        else:
            return "low"
    
    def predict_icu_need(self, patient_data):
        """Generate complete ICU prediction"""
        score = self.calculate_risk_score(patient_data)
        risk_level = self.get_risk_level(score)
        risk_info = self.risk_levels[risk_level]
        
        # Estimated ICU stay (days)
        if risk_level == "critical":
            estimated_stay = random.randint(5, 14)
        elif risk_level == "high":
            estimated_stay = random.randint(3, 7)
        elif risk_level == "medium":
            estimated_stay = random.randint(1, 3)
        else:
            estimated_stay = 0
        
        return {
            "risk_score": score,
            "risk_level": risk_level,
            "color": risk_info["color"],
            "recommended_action": risk_info["action"],
            "priority": risk_info["priority"],
            "estimated_icu_stay_days": estimated_stay,
            "requires_icu": risk_level in ["critical", "high"],
            "urgency": "Immediate" if risk_level == "critical" else ("High" if risk_level == "high" else "Routine")
        }

class ICUResourceManager:
    """Manages ICU bed allocation and resource tracking"""
    
    def __init__(self):
        self.total_icu_beds = 20
        self.occupied_beds = random.randint(12, 18)
        self.reserved_beds = 2
        self.pending_admissions = []
    
    def get_availability(self):
        """Get current bed availability"""
        available = self.total_icu_beds - self.occupied_beds - self.reserved_beds
        occupancy_rate = (self.occupied_beds / self.total_icu_beds) * 100
        
        status = "green"
        if occupancy_rate > 85:
            status = "red"
        elif occupancy_rate > 70:
            status = "orange"
        
        return {
            "total_beds": self.total_icu_beds,
            "occupied_beds": self.occupied_beds,
            "available_beds": max(0, available),
            "reserved_beds": self.reserved_beds,
            "occupancy_rate": round(occupancy_rate, 1),
            "status": status
        }
    
    def allocate_bed(self, patient_id, priority):
        """Allocate bed based on priority (1=highest)"""
        availability = self.get_availability()
        
        if availability["available_beds"] <= 0 and priority == 4:
            return {"allocated": False, "reason": "No beds available", "waitlist_position": len(self.pending_admissions) + 1}
        
        if priority <= 2:  # Critical or High priority
            self.occupied_beds += 1
            return {"allocated": True, "bed_number": random.randint(1, self.total_icu_beds), "estimated_wait": 0}
        else:
            self.pending_admissions.append({"patient_id": patient_id, "priority": priority, "timestamp": datetime.now()})
            position = len(self.pending_admissions)
            return {"allocated": False, "reason": "Awaiting bed assignment", "waitlist_position": position, "estimated_wait_hours": position * 2}
    
    def get_waitlist(self):
        """Get current waitlist"""
        return sorted(self.pending_admissions, key=lambda x: (x["priority"], x["timestamp"]))

# Generate mock patient data
def generate_mock_patients():
    patients = []
    first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    
    for i in range(20):
        age = random.randint(18, 92)
        patients.append({
            "id": f"ICU-{1000 + i}",
            "name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "age": age,
            "sbp": random.randint(70, 160),
            "hr": random.randint(60, 150),
            "rr": random.randint(12, 35),
            "o2_sats": random.randint(85, 100),
            "lactate": round(random.uniform(0.5, 8.0), 1),
            "wbc": random.randint(3000, 25000),
            "num_conditions": random.randint(0, 8),
            "recent_surgery": random.choice([True, False]),
            "on_ventilator": random.choice([True, False]),
            "admission_time": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
    
    return patients

predictor = ICURiskPredictor()
resource_manager = ICUResourceManager()
mock_patients = generate_mock_patients()