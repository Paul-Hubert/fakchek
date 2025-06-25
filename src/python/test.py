from text_checker import fact_check_text
from pipeline import video_to_verdict

def main():
    #test("Petrol comes from dinosaurs")
    #test("Cheese comes from a cow")
    test_video("trump_fakcheck.mp4")

def test(str):
    print("Prompt : ")
    print(str)
    (is_true, answer) = fact_check_text(str)
    print("Is this true ? ")
    print(is_true)
    print("Explanation : ")
    print(answer)

def test_video(path):
    print("Prompt : ")
    print(path)
    (is_true, answer) = video_to_verdict(path)
    print("Is this true ? ")
    print(is_true)
    print("Explanation : ")
    print(answer)

if __name__ == "__main__":
    main()
