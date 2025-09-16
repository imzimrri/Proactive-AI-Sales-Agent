# Proactive AI Sales Agent

An AI-powered phone calling system that automates outbound sales calls using VAPI.ai, OpenAI's GPT models, and Twilio for voice communication. This project enables businesses to proactively reach out to potential customers with personalized AI-driven conversations.

## Features

- **Web Form Integration**: Simple HTML form for collecting customer information (name and phone number)
- **E.164 Validation**: Server-side validation ensures phone numbers are in the correct international format
- **AI-Powered Calls**: Uses VAPI.ai to initiate calls with GPT-4 powered conversations
- **Customizable Assistant**: Configurable AI assistant with specific conversation flows and functions
- **Voice Integration**: PlayHT voice synthesis for natural-sounding AI speech
- **Webhook Support**: Integrates with webhooks for real-time call event handling
- **Debug Logging**: Comprehensive logging for troubleshooting call initiation and status

## Prerequisites

- Python 3.7+
- Flask
- VAPI.ai account with API key
- Twilio account (integrated via VAPI)
- OpenAI API key (configured in VAPI dashboard)
- PlayHT account (if using PlayHT voice)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/imzimrri/Proactive-AI-Sales-Agent.git
   cd Proactive-AI-Sales-Agent
   ```

2. Install dependencies:

   ```bash
   pip install flask python-dotenv requests
   ```

3. Create a `.env` file in the root directory with your API keys:

   ```
   VAPI_API_KEY=your_vapi_api_key_here
   VAPI_PHONE_NUMBER_ID=your_vapi_phone_number_id_here
   WEBHOOK_URL=your_webhook_url_here
   ```

4. Ensure your VAPI account is configured with:
   - OpenAI API key
   - PlayHT credentials (if applicable)
   - Verified phone number for outbound calls

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5001`

3. Fill out the web form with a customer's name and phone number

4. Submit the form to initiate an AI-powered call

## Configuration

### Environment Variables

- `VAPI_API_KEY`: Your VAPI.ai API key
- `VAPI_PHONE_NUMBER_ID`: The ID of your verified VAPI phone number
- `WEBHOOK_URL`: URL for handling call webhooks (e.g., webhook.site for testing)

### AI Assistant Configuration

The AI assistant is configured in `vapi_caller.py` with:

- GPT-4 model for conversation
- Custom system prompt for sales flow
- Function calling for appointment booking
- PlayHT voice for speech synthesis

## Project Structure

```
.
├── app.py                 # Main Flask application
├── vapi_caller.py         # VAPI API integration
├── templates/
│   └── index.html         # Web form template
├── docs/
│   ├── prd.md            # Product requirements
│   └── screen.png        # Screenshots
├── .env                   # Environment variables (not committed)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## API Endpoints

- `GET /`: Serves the main web form
- `POST /call`: Initiates a call with form data

## Troubleshooting

- **Calls not connecting**: Check VAPI dashboard for call status and ensure API keys are properly configured
- **Environment variables not loading**: Verify `.env` file is in the correct location and dotenv is installed
- **Phone number validation errors**: Ensure phone numbers are in E.164 format (+country code)
- **Permission issues**: If running on macOS, you may need to configure Git safe directories

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [VAPI.ai](https://vapi.ai) for AI phone call infrastructure
- [OpenAI](https://openai.com) for GPT models
- [Twilio](https://twilio.com) for telephony services
- [PlayHT](https://play.ht) for voice synthesis
