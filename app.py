from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Global list to store notes
notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

# The test script specifically calls THIS route
@app.route('/results', methods=["POST"])
def regex_results():
    # Field names 'regex' and 'test_string' MUST match test_app.py
    regex_pattern = request.form.get("regex", "")
    test_string = request.form.get("test_string", "")
    
    matches = []
    error = None
    
    if regex_pattern:
        try:
            # findall returns all matching strings
            matches = re.findall(regex_pattern, test_string)
        except re.error as e:
            error = f"Invalid Regex: {str(e)}"
            
    return render_template("home.html", notes=notes, matches=matches, error=error)

if __name__ == '__main__':
    app.run(debug=True)