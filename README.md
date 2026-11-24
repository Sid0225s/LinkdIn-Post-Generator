# LinkedIn Post Generator

This is a small AI project that generates LinkedIn posts based on the user's requirements.

The idea behind this project is to use existing LinkedIn posts as examples and use an LLM to generate a new post with a similar style and structure.

## What does it do?

The user can select things like:

- Language
- Post length
- Topic

Based on these selections, the application finds some relevant posts from the dataset and uses them as examples while generating a new post.

For example, if I select:

- Language: Hinglish
- Length: Medium
- Topic: Job Search

the application searches for posts matching these requirements and then uses them as few-shot examples for the LLM.

## How the project works

The project has two main stages: preprocessing and post generation.

During preprocessing, the raw LinkedIn posts are analyzed and information such as language, tags and line count is extracted. This information is stored in `processed_posts.json`.

When the user generates a post, the application uses the selected language, length and topic to find relevant examples from the processed data. These examples are then included in the prompt sent to the LLM.

### Flow

Raw Posts  
↓  
Preprocessing  
↓  
Processed Posts  
↓  
User selects language, length and topic  
↓  
Find relevant examples  
↓  
Few-shot prompt  
↓  
LLM  
↓  
Generated LinkedIn Post

## Set-up

1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `.env` update the value of `GROQ_API_KEY` with the API_KEY you created.
2. To get started, first install the dependencies using:
   ```commandline
    pip install -r requirement.txt
   ```
3. Run the streamlit app:
   ```commandline
   streamlit run main.py
   ```
