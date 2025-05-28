import webbrowser
import urllib.parse

phone_number = "+911111111"  # Change this to your recipient's number
message = "Hello! This is a test message from Python 😄"

# Encode the message
encoded_msg = urllib.parse.quote(message)

# WhatsApp URL
url = f"https://wa.me/{phone_number}?text={encoded_msg}"

# Open the URL in browser (this opens WhatsApp app on phone)
webbrowser.open(url)
