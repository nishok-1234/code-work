import random   
from cryptography.fernet import Fernet   
# AI DIAGNOSIS  def 
diagnose(symptoms):     symptom_map 
= {   
        "fever": "Influenza",   
        "cough": "Common Cold",   
        "chest pain": "Heart Disease",   
        "fatigue": "Anemia",   
        "headache": "Migraine"   
    }   
   
    diagnosis = [symptom_map[s] for s in symptoms if s in symptom_map]      return diagnosis if diagnosis else ["Diagnosis not found"]   
   
# TREATMENT RECOMMENDATION    
def recommend_treatment(diagnosis, patient_profile):     treatments = {   
        "Influenza": "Rest, fluids, antiviral medication",   
        "Common Cold": "Rest, hydration, over-the-counter meds",          
"Heart Disease": "Lifestyle changes, statins, beta-blockers",   
        "Anemia": "Iron supplements, diet improvement",   
        "Migraine": "Pain relief meds, lifestyle adjustment"   
    }   
   
    if diagnosis in treatments:         base = treatments[diagnosis]         if patient_profile.get("age") > 60:   
            base += " (adjust for elderly patient)"          if patient_profile.get("allergies"):              base += f" (check for allergy to {patient_profile['allergies']})"          return base       return "No treatment found"   
   
# IOT SIMULATION def 
get_iot_data():      return {   
        "heart_rate": random.randint(60, 110),   
        "temperature": round(random.uniform(36.0, 39.5), 1),   
        "oxygen_level": random.randint(88, 100)   
    }   
   
def check_alerts(data):     alerts = []     if data["heart_rate"] 	> 	100:          
alerts.append("High Heart Rate")     if data["temperature"] 	> 	38:         
alerts.append("High Temperature")     if data["oxygen_level"] 	< 	92:          alerts.append("Low 	Oxygen 	Level")      
return alerts   
   
# DATA SECURITY    
# Generate encryption key (for demo purposes; in production, store safely) key 
= Fernet.generate_key()   cipher = Fernet(key)   
   
def encrypt_data(data: str) -> bytes:     return cipher.encrypt(data.encode())   
   
def decrypt_data(encrypted_data: bytes) -> str:     return cipher.decrypt(encrypted_data).decode()   
   
# MAIN PROGRAM   
if _name_ == "_main_":     # Sample input     symptoms = ["fever", "fatigue"]      profile = 
{"age": 45, "allergies": "penicillin"}   
   
    # Diagnosis     diagnosis_list = diagnose(symptoms)     diagnosis =  diagnosis_list[0]   
    print("Diagnosis:", diagnosis)   
   
    # Treatment Recommendation   
    treatment_plan = recommend_treatment(diagnosis, profile)      print("Treatment Recommendation:", treatment_plan)   
   
    # IoT Monitoring     iot_data = get_iot_data()     alerts = check_alerts(iot_data)     print("\nIoT Real-Time Data:", iot_data)      print("Health 
Alerts:", alerts if alerts else "Vitals are normal")   
   
    # Data Encryption Demo      sensitive_info = f"{diagnosis} - {treatment_plan}"      encrypted = encrypt_data(sensitive_info)     decrypted  
= decrypt_data(encrypted)      print("\nEncrypted Diagnosis & 
Treatment Data:", encrypted)      print("Decrypted Data:", decrypted)   
