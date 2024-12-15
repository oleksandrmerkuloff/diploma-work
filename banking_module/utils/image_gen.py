import requests


API_URL = 'https://picsum.photos/600'
IMAGE_PATH = 'diploma_platform/banking_module/static/banking_module/images/'


def new_image():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.content


if __name__ == '__main__':
    new_image(45)
