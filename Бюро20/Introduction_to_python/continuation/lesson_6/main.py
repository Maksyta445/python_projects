import os
import requests


def download_picture():
    url = 'https://random.dog/woof.json'
    payload = {
        "filter": "mp4,webm",
    }
    folder = "C:\python_projects\Бюро20\Introduction_to_python\continuation\lesson_6\dogs"
    for x in range(50):
        response = requests.get(url, params=payload)
        picture_link = response.json()["url"]
        link = os.path.splitext(picture_link)[0]
        picture_extension = os.path.splitext(picture_link)[1]
        filename = f"dog_{x}.{picture_extension}"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, filename)
        with open(file_path, "wb") as f:
            f.write(requests.get(picture_link).content)
        print(picture_extension)

def main():
    print(download_picture())

if __name__ == "__main__":
    main()