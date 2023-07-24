import openai
import os
# Import the function to get memories from autogptblogDB.py
from autogptblogDB import get_memories

openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to summarize memories
def summarize_memories(memories):
    # For now, just join the memories with a delimiter
    return ' | '.join(memories)

def generate_text(prompt):
    # Get the memories from the database
    memories = get_memories()
    # Summarize the memories
    summarized_memories = summarize_memories(memories)
    # Include the summarized memories in the prompt
    full_prompt = f"{summarized_memories} {prompt}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt}
        ]
    )
    return response.choices[0].message['content']