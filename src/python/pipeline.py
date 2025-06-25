from text_checker import fact_check_text
from to_text import video_to_text

def video_to_verdict(path):
    text = video_to_text(path)
    (is_true, answer) = fact_check_text(text)
    return (is_true, answer)
