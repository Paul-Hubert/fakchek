from text_checker import fact_check_text
from pipeline import video_to_verdict
from source_search import find_source
from source_search import google_search
from read_video import show_video

def main():
    #test("Petrol comes from dinosaurs")
    #test("Cheese comes from a cow")
    
    test_video("trump_fakcheck.mp4", "audio.wav")

def test(str):
    print("Prompt : ")
    print(str)
    (is_true, answer) = fact_check_text(str)
    print("Is this true ? ")
    print(is_true)
    print("Explanation : ")
    print(answer)

def test_video(path, audio_path):
    print("Prompt : ")
    print(path)
    (is_true, answer) = video_to_verdict(path)
    print("Is this true ? ")
    print(is_true)
    print("Explanation : ")
    print(answer)
    

    show_video(is_true, path, audio_path)

if __name__ == "__main__":
    main()
