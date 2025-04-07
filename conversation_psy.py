import os
from openai import OpenAI

def conversation(input_text):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")
    
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "This is what the patient seeing a psychiatrist verbally says to the doctor, describe and only describe their behavior, no diagnosis, be concise: in less than 50 words"},
                {"role": "user", "content": input_text}
            ],
        )
        
        response = chat_completion.choices[0].message.content.strip()


        return response
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    user_input = "Tell me something about AI."
    reply = conversation(user_input)
    print(f"Model reply: {reply}")
