from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

# Load student database from CSV
def load_students():
    students = {}
    with open('uds_src26.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students[row['Student_ID']] = {
                'name': row['Full_Name'],
                'station': row['Polling_Station']
            }
    return students

STUDENTS = load_students()

class USSDResponse:
    def __init__(self, session_id=None, user_id=None, msisdn=None, message=None, continue_session=False):
        self.sessionID = session_id
        self.userID = user_id
        self.msisdn = msisdn
        self.message = message
        self.continueSession = continue_session

@app.route('/')
def index():
    """Web interface for testing"""
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_student():
    """Web API endpoint for checking student"""
    data = request.json
    student_id = data.get('student_id', '').strip().upper()
    
    if student_id in STUDENTS:
        student = STUDENTS[student_id]
        return jsonify({
            'found': True,
            'name': student['name'],
            'station': student['station']
        })
    else:
        return jsonify({
            'found': False,
            'message': f'Student ID {student_id} not found in the system.'
        })

@app.route('/endpointURL', methods=['POST'])
def ussd_handler():
    ussd_request = request.json
    
    ussd_response = USSDResponse(
        session_id=ussd_request.get('sessionID'),
        user_id=ussd_request.get('userID'),
        msisdn=ussd_request.get('msisdn')
    )
    
    # New session - show welcome message
    if ussd_request.get('newSession') and ussd_request.get('userData') == '*928*92#':
        ussd_response.message = "Welcome to Student Polling Station Checker\n\nPlease enter your Student ID:"
        ussd_response.continueSession = True
    
    # User entered student ID
    elif not ussd_request.get('newSession'):
        student_id = ussd_request.get('userData').strip().upper()
        
        if student_id in STUDENTS:
            student = STUDENTS[student_id]
            ussd_response.message = f"Name: {student['name']}\nPolling Station: {student['station']}"
        else:
            ussd_response.message = f"Student ID {student_id} not found.\nPlease check and try again."
        
        ussd_response.continueSession = False
    
    else:
        ussd_response.message = "Invalid request"
        ussd_response.continueSession = False
    
    return jsonify(vars(ussd_response))

if __name__ == '__main__':
    app.run(port=8080, debug=True)
