Make sure you have Python 3 installed.
Make sure you have ngrok installed and set your authtoken.
Open your terminal and go to the project folder (roadapp).
Install Flask: pip install flask
Run the app:python app.py
Start ngrok to make it online: ngrok http 5000
Copy the https URL from ngrok to open the app in any browser.
Click “+ Report Issue” to add a new road issue.
Click on the map to select the location for your report.
Write a short description of the issue.
Click Submit to save your report.
All reports will appear as markers on the map.
Click a marker and press “Mark Resolved” to remove the issue.
Your reports are saved in reports.json.
You can read them anytime in terminal or Python.
