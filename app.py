import re # Import the regex module
from flask import Flask, render_template, request, jsonify
from vapi_caller import trigger_call # Import from our new file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call', methods=['POST'])
def call():
    phone_number = request.form['phone']
    customer_name = request.form['name']

    if not phone_number or not customer_name:
        error_msg = "Please provide both name and phone number."
        if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": False, "message": error_msg}), 400
        return error_msg, 400

    # Server-side validation for E.164 format
    e164_pattern = re.compile(r"^\+[1-9]\d{1,14}$")
    if not e164_pattern.match(phone_number):
        error_msg = f"The number '{phone_number}' is not in the required E.164 format. Please enter it as '+' followed by the country code and number (e.g., +15551234567)."
        if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({"success": False, "message": error_msg}), 400
        error_message = f"""<h1>Invalid Phone Number</h1>
        <p>The number '<strong>{phone_number}</strong>' is not in the required E.164 format.</p>
        <p>Please go back and enter it as '+' followed by the country code and number (e.g., <strong>+15551234567</strong>).</p>"""
        return error_message, 400

    print(f"Web form submitted. Received Name: {customer_name}, Phone: {phone_number}")
    trigger_call(phone_number, customer_name)

    success_msg = f"Thank you! Our AI assistant will call you at {phone_number} shortly."
    if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({"success": True, "message": success_msg})

    # Display a simple success message to the user
    return f"""<h1>Thank you!</h1>
    <p>Our AI assistant will call you at {phone_number} shortly.</p>"""

if __name__ == '__main__':
    # Running on port 5001 to avoid potential conflicts
    app.run(debug=True, port=5001)
