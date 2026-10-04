python
import json
import datetime

# 1. Load the Data (The "Proposed Project")
with open('mock_data.json', 'r') as file:
    project_data = json.load(file)

print(f"--- GENERATING AUTOMATED PRIVACY IMPACT ASSESSMENT (PIA) ---")
print(f"Date: {datetime.date.today()}")
print(f"Frameworks Applied: GDPR Art. 35, NIST AI RMF, CIPP/US\n")

for item in project_data:
    # START THE ASSESSMENT FOR EACH DATA FLOW
    print(f"Subject: Transaction ID {item['transaction_id']}")
    print("-" * 40)
    
    # SECTION 1: NATURE OF PROCESSING
    print(f"1. DATA TYPE DETECTED: [{item['data_type']}]")
    
    # SECTION 2: NECESSITY & PROPORTIONALITY (The PIA Core)
    risk_level = "LOW"
    mitigation_required = "None"
    
    # Trigger 1: Biometric Data (High Risk per GDPR Art 9)
    if "biometric" in item['data_type']:
        risk_level = "HIGH (Sensitive Category)"
        mitigation_required = "Must implement explicit consent & encryption at rest."
        
    # Trigger 2: Automated Decision Making (High Risk per GDPR Art 22)
    if item['ai_decision_made'] and not item['consent_obtained']:
        risk_level = "CRITICAL (Illegal Processing)"
        mitigation_required = "STOP PROCESSING. Human-in-the-loop required immediately."

    print(f"2. RISK RATING: {risk_level}")
    
    # SECTION 3: REMEDIATION PLAN
    if risk_level != "LOW":
        print(f"3. REQUIRED MITIGATION: {mitigation_required}")
        print("   STATUS: ❌ PIA FAILED - DO NOT DEPLOY")
    else:
        print("   STATUS: ✅ PIA APPROVED")
    
    print("\n")

print("--- END OF ASSESSMENT REPORT ---")

