import requests
import json
import logging

API_ENDPOINT = "https://chatgptss.org/wp-admin/admin-ajax.php"

def create_data(message: str, bot_id: int = 0) -> dict:
    return {
        '_wpnonce': 'c7cea073e4',
        'post_id': 19,
        'url': 'https://chatgptss.org',
        'action': 'wpaicg_chat_shortcode_message',
        'message': message,
        'bot_id': bot_id,
    }

def freegpt(user_message: str, bot_id: int = 0) -> None:
    if not isinstance(user_message, str):
        raise TypeError("User message must be a string.")

    data = create_data(user_message, bot_id)

    try:
        response = requests.post(API_ENDPOINT, data=data)
        response.raise_for_status()

        if response.content:
            try:
                response_json = response.json()
                response_text = response_json['data']
                response_text = response_text.replace("- AI ChatBot Unlimited?", "")
                print(response_text)
            except json.JSONDecodeError:
                logging.warning("Request successful, but response is not valid JSON.")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logging.error("Request failed with status code 404: %s", e.response.url)
        elif e.response.status_code == 500:
            logging.error("Request failed with status code 500: %s", e.response.url)
        else:
            logging.error("Request failed with status code: %s", e.response.status_code)
    except requests.exceptions.RequestException as e:
        logging.error("Error: %s", e)

    return ""
    print(response)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
