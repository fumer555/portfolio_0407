import os

def set_env():
    try:
        with open('./.env/openai_api_key.txt', 'r') as file:
            api_key = file.read().strip()  #
        os.environ["OPENAI_API_KEY"] = api_key
        print("OPENAI_API_KEY has been set successfully.")
    except FileNotFoundError:
        print("Error: File './.env/openai_api_key.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
