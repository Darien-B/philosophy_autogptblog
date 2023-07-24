import os
import requests
import base64

site_url = 'https://philosophy.autogptblog.dev'
username = os.getenv('WP_USERNAME')  
password = os.getenv('WP_PASSWORD')  

def get_posts(site_url):
    url = f'{site_url}/wp-json/wp/v2/posts'
    response = requests.get(url)
    response_json = response.json()
    if response.status_code == 200:
        return response_json
    else:
        raise Exception('Failed to get posts: {}'.format(response_json))

def create_post(site_url, username, password, title, content):
    url = f'{site_url}/wp-json/wp/v2/posts'
    headers = {'Authorization': 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()}
    data = {'title': title, 'content': content, 'status': 'publish'}
    response = requests.post(url, data=data, headers=headers)
    response_json = response.json()
    if response.status_code == 201:
        return response_json
    else:
        raise Exception('Failed to create post: {}'.format(response_json))

def get_comments(site_url):
    url = f'{site_url}/wp-json/wp/v2/comments'
    response = requests.get(url)
    response_json = response.json()
    if response.status_code == 200:
        return response_json
    else:
        raise Exception('Failed to get comments: {}'.format(response_json))

def respond_to_comment(site_url, username, password, comment_id, response_text):
    url = f'{site_url}/wp-json/wp/v2/comments/{comment_id}'
    headers = {'Authorization': 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()}
    data = {'content': response_text}
    response = requests.post(url, data=data, headers=headers)
    response_json = response.json()
    if response.status_code == 201:
        return response_json
    else:
        raise Exception('Failed to respond to comment: {}'.format(response_json))