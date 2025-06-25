import whisper

def video_to_text(path):
    model = whisper.load_model("base")  # ou "small", "medium", "large"
    result = model.transcribe(path)
    print(result["text"])
    return result["text"]
