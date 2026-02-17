import requests
import json

# Test the USSD application
BASE_URL = "http://localhost:8080/endpointURL"

def test_new_session():
    """Test initial session"""
    payload = {
        "sessionID": "session123",
        "userID": "user001",
        "msisdn": "233244123456",
        "newSession": True,
        "userData": "*928*92#"
    }
    
    response = requests.post(BASE_URL, json=payload)
    print("=== New Session Test ===")
    print(json.dumps(response.json(), indent=2))
    print()

def test_student_lookup(student_id):
    """Test student ID lookup"""
    payload = {
        "sessionID": "session123",
        "userID": "user001",
        "msisdn": "233244123456",
        "newSession": False,
        "userData": student_id
    }
    
    response = requests.post(BASE_URL, json=payload)
    print(f"=== Student Lookup Test ({student_id}) ===")
    print(json.dumps(response.json(), indent=2))
    print()

if __name__ == "__main__":
    print("Testing USSD Application...\n")
    
    # Test new session
    test_new_session()
    
    # Test valid student IDs
    test_student_lookup("STU001")
    test_student_lookup("STU050")
    
    # Test invalid student ID
    test_student_lookup("STU999")
