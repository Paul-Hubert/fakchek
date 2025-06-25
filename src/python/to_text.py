import whisper

def video_to_text(path):
    model = whisper.load_model("base")  # ou "small", "medium", "large"
    result = model.transcribe(path)
    print(result["text"])
    return result["text"]

def video_to_text_with_segments(path):
    model = whisper.load_model("base")  # ou "small", "medium", "large"
    result = model.transcribe(path)
    segments = result["segments"]

    interval = 15  # secondes
    grouped_transcription = {}

    for segment in segments:
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text']

        # On détermine dans quel intervalle commence le segment
        interval_start = int(start_time // interval) * interval

        if interval_start not in grouped_transcription:
            grouped_transcription[interval_start] = ""

        grouped_transcription[interval_start] += " " + text

    # Affichage
    for start in sorted(grouped_transcription):
        end = start + interval
        print(f"[{start:.0f} - {end:.0f}s] {grouped_transcription[start].strip()}")

