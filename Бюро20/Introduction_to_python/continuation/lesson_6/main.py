import os
import requests


def download_picture(folder, filename, picture_link):
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)
    with open(file_path, "wb") as f:
        f.write(requests.get(picture_link).content)


def main():
    url = 'https://random.dog/woof.json'
    folder = "dogs"
    payload = {"filter": "mp4,webm"}
    for num in range(5):
        response = requests.get(url, params=payload)
        picture_link = response.json()["url"]
        picture_extension = os.path.splitext(picture_link)[1]
        filename = f"dog_{num}.{picture_extension}"
        download_picture(folder, filename, picture_link)


if __name__ == "__main__":
    main()