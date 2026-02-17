# Student Polling Station Checker

A USSD and Web application to help students find their polling stations.

## Features
- USSD interface for mobile access
- Web interface for browser access
- 100 students with polling station assignments
- Easy deployment to cloud platforms

## Local Testing

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access web interface: http://localhost:8080
4. Test USSD endpoint: http://localhost:8080/endpointURL

## Deployment Options

### Option 1: Render (Free)
1. Push code to GitHub
2. Go to https://render.com
3. Create new Web Service
4. Connect your GitHub repo
5. Render auto-deploys

### Option 2: Railway
1. Go to https://railway.app
2. Connect GitHub repo
3. Deploy automatically

### Option 3: Heroku
```bash
heroku create your-app-name
git push heroku main
```

## USSD Integration

After deployment, configure your USSD gateway:

1. Sign up with provider (Arkesel, Hubtel, etc.)
2. Get USSD short code
3. Set webhook URL: `https://your-app.com/endpointURL`
4. Test by dialing the code

## API Endpoints

### USSD Endpoint
- **URL:** `/endpointURL`
- **Method:** POST
- **Body:**
```json
{
  "sessionID": "session123",
  "userID": "user001",
  "msisdn": "233244123456",
  "newSession": true,
  "userData": "*928*92#"
}
```

### Web Check Endpoint
- **URL:** `/check`
- **Method:** POST
- **Body:**
```json
{
  "student_id": "STU001"
}
```

## Student ID Format
- Format: STU001 to STU100
- Example: STU001, STU050, STU100
