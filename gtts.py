from google.cloud import texttospeech

# Initialize the client
client = texttospeech.TextToSpeechClient()

# Construct the request
input_text = texttospeech.SynthesisInput(text="Hello, how are you?")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Wavenet-F",  # Female voice
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the request
response = client.synthesize_speech(
    input=input_text, voice=voice, audio_config=audio_config
)

# Save the response to a file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
