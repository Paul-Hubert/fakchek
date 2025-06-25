from text_checker import fact_check_text

def main():
    test("Petrol comes from dinosaurs")
    test("Cheese comes from a cow")

def test(str):
    print("Prompt : ")
    print(str)
    (is_true, answer) = fact_check_text(str)
    print("Is this true ? ")
    print(is_true)
    print("Explanation : ")
    print(answer)

if __name__ == "__main__":
    main()
