python
import json

# 1. Load the mock data (The Pac-Man Dots)
with open('mock_data.json', 'r') as file:
    transactions = json.load(file)

print("--- STARTING AIGP & CIPP/E COMPLIANCE SCAN ---\n")

# 2. The Logic Loop (Pac-Man eating the dots)
for txn in transactions:
    risk_score = 0
    flags = []

    # CHECK 1: GDPR Cross-Border (CIPP/E)
    # If user is in Europe (DE/FR) and data moves to US server logic
    if txn['user_location'] in ['Berlin, DE', 'Paris, FR']:
        print(f"Checking EU Data Subject: {txn['transaction_id']}")
    
    # CHECK 2: Security Failure (CIPT)
    # If data is unencrypted, it violates privacy-by-design
    if txn['encryption_level'] == "None":
        risk_score += 50
        flags.append("CRITICAL: Unencrypted Data Storage (Violates NIST-SP-800)")

    # CHECK 3: Illegal AI Consent (AIGP)
    # If AI made a decision but no consent was signed
    if txn['ai_decision_made'] == True and txn['consent_obtained'] == False:
        risk_score += 50
        flags.append("VIOLATION: Automated Decision without Consent (Art. 22 GDPR)")

    # 3. Report Results
    if risk_score > 0:
        print(f"❌ RISK DETECTED in {txn['transaction_id']}: {flags}")
    else:
        print(f"✅ {txn['transaction_id']} is COMPLIANT.")

print("\n--- SCAN COMPLETE ---")
