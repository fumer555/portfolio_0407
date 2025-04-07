# portfolio_0407

## AI-Powered Voice Health Assistant

### Project Overview

This project introduces a health assistant that takes in users' vocal input, analyzes the provided symptoms and
provides possible disease name as a response.

### Repositories Content

- **`audio2word.py`**: Converts speech to text using **OpenAI Whisper**.
- **`conversation.py`**: AI symptom analysis using **GPT-4**.
- **`convert_online_gtts.py`**: Converts text-based diagnosis into speech.
- **`main.py`**: The core script that records, processes, and plays back the diagnosis.
- **`press_recording.py`**: Manages the voice recording process.
- **`set_env.py`**: Loads API keys from the `.env` directory.

### Installation

#### 1. Clone the project

Download the Project as a Zip File or Clone the Repository

#### 2. Install dependencies

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

#### 3.Run the assistant

```bash
python main.py
```

#### 4.Demonstration

<iframe width="560" height="900" src="https://youtube.com/shorts/QII601ZcQsI?si=EKy2OmWqfJtR0BHy" frameborder="0" allowfullscreen></iframe>
