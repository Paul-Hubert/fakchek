import whisper

model = whisper.load_model("base")  # ou "small", "medium", "large"
result = model.transcribe("trump_fakcheck.mp4")

print(result["text"])
