
import requests
import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

# --- Configuration ---
# Securely load secrets from the .env file
VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_PHONE_NUMBER_ID = os.getenv("VAPI_PHONE_NUMBER_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# --- Vapi API Details ---
VAPI_API_URL = "https://api.vapi.ai/call/phone"

def trigger_call(phone_number_to_call, customer_name="Valued Customer"):
    """
    Triggers a Vapi call to a specific phone number with a dynamic customer name.
    """
    print(f"Initiating call to {customer_name} at {phone_number_to_call}...")

    payload = {
        "phoneNumberId": VAPI_PHONE_NUMBER_ID,
        "customer": {
            "number": phone_number_to_call,
            "name": customer_name
        },
        "assistant": {
            "serverUrl": WEBHOOK_URL,
            "model": {
                "provider": "openai",
                "model": "gpt-4-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a friendly and efficient AI assistant for a personal trainer. Your only goal is to book a free 15-minute consultation. Your conversation flow is: 1. Greet the user by name. 2. State your purpose (booking a consultation). 3. Ask for their primary fitness goal. 4. Based on their answer, propose the single time slot of 3 PM tomorrow. 5. If they agree, use the bookAppointment function to confirm. If they ask for a different time or are unsure, politely state that you can only book 3 PM tomorrow and that a human will follow up to find a better time, then end the call."
                    }
                ],
                "functions": [
                    {
                        "name": "bookAppointment",
                        "description": "Books the 15-minute consultation for the user after they have agreed to the time.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "time": {"type": "string", "description": "The time for the appointment, which must be '3 PM tomorrow'."},
                                "fitnessGoal": {"type": "string", "description": "The user's stated primary fitness goal."}
                            },
                            "required": ["time", "fitnessGoal"]
                        }
                    }
                ]
            },
            "voice": {
                "provider": "playht",
                "voiceId": "jennifer"
            },
            "firstMessage": f"Hi {customer_name}, this is the AI assistant for John's Personal Training. I'm calling because you just filled out a form on our website, and I'd like to get you booked for your free 15-minute consultation."
        }
    }

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(VAPI_API_URL, headers=headers, json=payload)
        if response.status_code == 201:
            print(f"✅ Success! Call initiated to {customer_name}.")
            print("Response Body:", response.text)  # Debug: Print full response
            # Fetch call details to check status
            call_data = response.json()
            call_id = call_data.get("id")
            if call_id:
                status_url = f"https://api.vapi.ai/call/{call_id}"
                status_response = requests.get(status_url, headers=headers)
                if status_response.status_code == 200:
                    print("Call Status Details:", status_response.text)
                else:
                    print(f"Failed to fetch call status: {status_response.status_code}")
            return True
        else:
            print(f"❌ Error: Received status code {response.status_code}")
            print("Response Body:", response.text)
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ A network error occurred: {e}")
        return False
