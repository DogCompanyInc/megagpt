import requests
import json

API_ENDPOINT = "https://blackbox.ai/api/inference"

def create_headers(token):
    return {
        "Content-Type": "application/json",
        "key": str(token)
    }

def create_data(prompt):
    return {
        "messages": [{
            "role": "user",
            "content": str(prompt)
        }]
    }

def blackbox(api_token, user_message):
    if not isinstance(api_token, str) or not isinstance(user_message, str):
        print("Error: prompt and api_token must be strings.")
        return
    
    if api_token == '':
        print('OOPS! your api_token is invalid!')
        return

    headers = create_headers(api_token)
    data = create_data(user_message)

    banner = '''
  ╔╗                     ╔═╗ ╔╗ 
  ║║                     ║╔╝╔╝╚╗
╔═╝║╔══╗╔══╗    ╔══╗╔══╗╔╝╚╗╚╗╔╝
║╔╗║║╔╗║║╔╗║    ║══╣║╔╗║╚╗╔╝ ║║ 
║╚╝║║╚╝║║╚╝║    ╠══║║╚╝║ ║║  ║╚╗
╚══╝╚══╝╚═╗║    ╚══╝╚══╝ ╚╝  ╚═╝
        ╔═╝║                    
        ╚══╝                    
NOT OFFICIAL LIBRARY FOR BLACKBOX
    '''
    print(banner)

    try:
        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print("Request successful. Response: ", response.json())
    except requests.exceptions.HTTPError as e:
        print("Request failed with status code: ", e.response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
