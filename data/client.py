import requests
import json
from pprint import pprint as print

def update_speaking_sections():
    base_url = "https://dbvirtualeducation.com/ielts/api/section{}"

    for part in range(1, 4):
        try:
            response = requests.get(base_url.format(part))
            response.raise_for_status()  # Raise error if status != 200

            with open(f"speaking_{part}.json", "w", encoding="utf-8") as f:
                json.dump(response.json(), f, indent=4, ensure_ascii=False)

            print(f"[✓] Successfully saved section {part}")
        except requests.RequestException as e:
            print(f"[✗] Failed to fetch section {part}: {e}")
        except json.JSONDecodeError:
            print(f"[✗] Failed to parse JSON for section {part}")

def format_part_1():
    for part in range(1,2):
        actual_data = []
        with open(f"speaking_{part}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for element in data["content"]:
                temp_ = {
                    "name":element.split("-")[1].strip() if "-" in element else element,
                    "new": data["content"][element]["new"],
                    "answers": [question["answer"][0]["text"] for question in data["content"][element]["questions"]],
                    "questions":[question["text"] for question in data["content"][element]["questions"]],
                    "vocabulary": [vocabulary["text"] for vocabulary in data["content"][element]["vocabulary"]],
                    }
                ideas = []
                # Ideas saving
                for question in data["content"][element]["questions"]:
                    for idea in question["ideas"]:
                        ideas.append(idea["text"])
                temp_["ideas"] = ideas
                actual_data.append(temp_)
                # print(temp_)
        print(actual_data)
        with open(f"speaking_{part}_formatted.json", "w", encoding="utf-8") as f:
            json.dump(actual_data, f, indent=4, ensure_ascii=False)
        
def format_part_2():
    with open("speaking_2.json", "r", encoding="utf-8") as f:
        data = json.load(f)   
        actual_data = []
        for element in data["content"]:
            temp_ = {
                "name": element.split("-")[1].strip() if "-" in element else element,
                "new": data["content"][element]["new"],
                "questions": [question["text"] for question in data['content'][element]['questions']],
                "vocabulary": [vocabulary["text"] for vocabulary in data["content"][element]["vocabulary"]],
                "answers": [answer["text"] for answer in data["content"][element]["answer"]]
            }
            ideas = []
            for bullet in data["content"][element]["ideas"]:
                for idea in bullet["body"]:
                    ideas.append(idea["text"])
            temp_["ideas"] = ideas
            actual_data.append(temp_)
        # print(actual_data)
        with open("speaking_2_formatted.json", "w", encoding="utf-8") as f:
            json.dump(actual_data, f, indent=4, ensure_ascii=False)

def format_part_3():
    with open("speaking_3.json", "r", encoding="utf-8") as f:
        data = json.load(f)   
        actual_data = []
        for element in data["content"]:
            temp_ = {
                "name": element.split("-")[1].strip() if "-" in element else element,
                "new": data["content"][element]["new"],
                "questions": [question["text"] for question in data['content'][element]['questions']],
                "vocabulary": [vocabulary["text"] for vocabulary in data["content"][element]["vocabulary"]],
                "answers": [question["answer"][0]["text"] for question in data["content"][element]["questions"]]
            }
            ideas = []
            for bullet in data["content"][element]["questions"]:
                for idea in bullet["ideas"]:
                    ideas.append(idea["text"])
            temp_["ideas"] = ideas
            actual_data.append(temp_)
            # print(actual_data)
        with open("speaking_3_formatted.json", "w", encoding="utf-8") as f:
            json.dump(actual_data, f, indent=4, ensure_ascii=False)




if __name__ == "__main__":
    format_part_2()
