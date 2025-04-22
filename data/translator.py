import requests

def translate_text(text, source_lang='uz_UZ', target_lang='en_US'):
    url = "https://api-b2b.backenster.com/b1/api/v3/translate/?client=site&feature=seo_text&lang_pair=en_te"

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer a_25rccaCYcBC9ARqMODx2BV2M0wNZgDCEl3jryYSgYZtF1a702PVi4sxqi2AmZWyCcw4x209VXnCYwesx",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }

    data = {
        "from": source_lang,
        "to": target_lang,
        "text": text,
        "platform": "dp"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        return result.get("result", "No translation found.")
    else:
        raise Exception(f"Translation failed: {response.status_code} - {response.text}")

if __name__=="__main__":
    son = 0
    # Example usage:
    while 1:
        son+=1
        translated = translate_text("Salom ishlaring qalay")
        print(son, ". Translated text:", translated)
