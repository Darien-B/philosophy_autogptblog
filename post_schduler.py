import schedule
import os
import time
from ai_agent import generate_text
from wordpress_api import create_post

username = os.getenv('WP_USERNAME')  
password = os.getenv('WP_PASSWORD') 

def job():
    # Generate a new post
    post_content = generate_text("You are an AI philosopher, and you write daily blog posts in the style of famous philosophers such as Aristotle, Lao-Tzu, John Locke, Karl Marx, Confucius, Ralph Waldo Emerson, Immanuel Kant, Epicurus, Socrates, Zeno, and Friedrich Nietzsche. You have the ability to access a secondary prompt which works as a memory when creating a new post. You have the ability to interact with readers via the comments when a comment includes #AutoAgent. Every philosophical post you write must be original and from a unique perspective.")
    
    # Publish the new post
    create_post(f'https://philosophy.autogptblog.dev', username, password, 'Post Title', post_content)

# Schedule the job every day at 9am. 
# Note: this assumes that the system time is set to MST. 
# If not, you'll need to adjust the time or use a library that can handle timezones.
schedule.every().day.at("09:00").do(job)

while True:
    # Run pending scheduled jobs
    schedule.run_pending()
    time.sleep(1)