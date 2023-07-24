import schedule
import os
import time
from ai_agent import generate_text
from wordpress_api import create_post, get_comments
from autogptblogDB import update_memory

username = os.getenv('WP_USERNAME')  
password = os.getenv('WP_PASSWORD') 

def format_comments_for_ai(comments):
    # Concatenate the comments into a single string with some separator
    formatted_comments = " ".join(comments)
    return formatted_comments

def update_collective_understanding(summarized_comments):
    # The id of the collective understanding memory in the database
    collective_understanding_id = 1
    
    # Update the memory with the summarized comments
    update_memory(collective_understanding_id, summarized_comments)

def post_job():
    # Generate a new post
    post_content = generate_text("You are an AI philosopher, and you write daily blog posts in the style of famous philosophers such as Aristotle, Lao-Tzu, John Locke, Karl Marx, Confucius, Ralph Waldo Emerson, Immanuel Kant, Epicurus, Socrates, Zeno, and Friedrich Nietzsche. You have the ability to access a secondary prompt which works as a memory when creating a new post. You have the ability to interact with readers via the comments when a comment includes #AutoAgent. Every philosophical post you write must be original and from a unique perspective.")
    
    # Publish the new post
    create_post(f'https://philosophy.autogptblog.dev', username, password, 'Post Title', post_content)

def comment_job():
    # Get the comments
    comments = get_comments('https://philosophy.autogptblog.dev')
    
    # Format the comments for the AI model
    formatted_comments = format_comments_for_ai(comments)
    
    # Summarize the comments
    summarized_comments = generate_text(formatted_comments)
    
    # Update the collective understanding in the database
    update_collective_understanding(summarized_comments)

# Schedule the jobs
schedule.every().day.at("09:00").do(post_job)
schedule.every().day.at("23:59").do(comment_job)

while True:
    # Run pending scheduled jobs
    schedule.run_pending()
    time.sleep(1)