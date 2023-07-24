import requests

def authenticate_wordpress(client_id, client_secret, username, password):
    url = 'https://public-api.wordpress.com/oauth2/token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password,
        'grant_type': 'password'
    }
    response = requests.post(url, data=data)
    response_json = response.json()
    if response.status_code == 200:
        return response_json['access_token']
    else:
        raise Exception('Failed to authenticate: {}'.format(response_json))

def get_posts(access_token, site_id):
    url = f'https://public-api.wordpress.com/rest/v1.1/sites/{site_id}/posts/'
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    if response.status_code == 200:
        return response_json['posts']
    else:
        raise Exception('Failed to get posts: {}'.format(response_json))

def create_post(access_token, site_id, title, content):
    url = f'https://public-api.wordpress.com/rest/v1.1/sites/{site_id}/posts/new'
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    data = {'title': title, 'content': content}
    response = requests.post(url, data=data, headers=headers)
    response_json = response.json()
    if response.status_code == 201:
        return response_json
    else:
        raise Exception('Failed to create post: {}'.format(response_json))
