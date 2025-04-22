import requests
import time, json
import bs4

def send_question_to_chatgptdemo(question: str, chat_id="671de410f71af65b487f69b3"):
    url = "https://chat.chatgptdemo.net/chat_api_stream"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
    }
    payload = {
        "question": question,
        "chat_id": chat_id,
        "timestamp": int(time.time() * 1000),  # current timestamp in ms
        "retry": False
    }
    temp_ = ""
    response = requests.post(url, json=payload, headers=headers, stream=True)
    for line in response.iter_lines():
        try:
            # print(json.loads(line[5:])['choices'][0]['delta']['content'], end="")
            temp_ += json.loads(line[5:])['choices'][0]['delta']['content']
        except:
            continue
    if not response.ok:
        print(f"🚨 Failed with status code {response.status_code}: {response.text}")
    
    return temp_

def aIreview(essay_prompt, essay):
    ai_response_format = {
        "potential_score": "Your score in one number i.e: 8.5",
        "detailed_explanation": "Your explanation in html format"
    }
    
    response = send_question_to_chatgptdemo(f"""Evaluate this essay against IELTS criteria and give explanations in MD format.
    Be more positive and assess with better marks than you would for example if the essay is for band 7 give them band 7.5 or more!
    But if it is around band 4.5, give your honest opinion.
    Give shorter explanations.
    If the essay is not valid, give a band score of 0.1 and say "At least you tried" in the explanation.
    Answer in one line but address everything
    Alert them that the response is AI made and may contain errors.
    
    Your response should follow like this in double quotes for programmatically access using Python and make sure it is valid JSON:
    {ai_response_format}
    
    Here is the essay:
    Essay prompt:
        {essay_prompt}
    Essay:
        {essay}
    """)
    
    # Clean the response text to remove invalid characters and escape properly
    data_ = bs4.BeautifulSoup(response, "html.parser").get_text().replace("json", "")
    
    # Don't escape outer quotes in JSON itself, only escape internal characters
    # Clean unnecessary escapes inside the markdown
    data_ = data_.replace("\\\"", "\"")  # Remove unnecessary escapes
    data_ = data_.replace("\\'", "'")
    data_ = data_.replace("\\", "")    # Remove unnecessary escapes for single quotes
    
    # Handle any other potential problematic characters here if needed
    
    print("Raw JSON response:")
    print(data_)  # You can remove this in production if unnecessary
    
    # Parse the cleaned response into JSON
    try:
        parsed_data = json.loads(data_)
        return parsed_data
    except json.JSONDecodeError as e:
        print("Error: Could not parse the response into valid JSON.")
        print(f"JSON Decode Error: {e}")
        return None


# Main function to test the aIreview function
if __name__ == "__main__":
    review = aIreview(
        "Some people believe that technology isolates people, while others think it connects them. Discuss both views and give your own opinion.",
        """In recent years, technology has become an integral part of our daily lives, leading to debates about its effects on human relationships. While some argue that technology isolates people, others believe that it connects them. Both views have some validity, and in this essay, I will discuss both perspectives before giving my own opinion.

On the one hand, technology has made it easier for people to communicate with one another, even if they are far apart. For example, social media platforms like Facebook and Instagram allow users to stay in touch with friends and family regardless of location. Additionally, video calling applications like Zoom and Skype have become essential for both personal and professional communication. These advances have, in many ways, created a more connected world where people can share experiences and stay informed.

However, there are valid concerns that technology can contribute to social isolation. The rise of smartphones and social media has led to an increase in virtual interactions, which often replace face-to-face communication. People may spend hours on their phones, engaging with online content, while neglecting the relationships around them. Moreover, some individuals, especially younger generations, are becoming more reliant on digital devices, which may hinder their ability to develop meaningful in-person connections.

In my opinion, technology is neither entirely isolating nor completely connecting. It largely depends on how it is used. When used appropriately, technology can enhance relationships by keeping people connected across distances. However, excessive use of technology without balancing real-world interactions can lead to isolation. Therefore, individuals should be mindful of how they use technology to maintain a healthy balance between online and offline socialization.

In conclusion, technology has both positive and negative effects on social connections. While it facilitates communication across distances, it also has the potential to foster isolation if used improperly. It is essential for individuals to strike a balance in their use of technology to ensure that it remains a tool for connection rather than disconnection."""
    )

    if review:
        print("\nParsed Review:")
        print(json.dumps(review, indent=4))  # Pretty print for better readability