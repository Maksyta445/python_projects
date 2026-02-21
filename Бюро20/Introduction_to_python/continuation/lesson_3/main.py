from PIL import Image
import os


for x in range(5):
    file_path = f"photo_end_{x}"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    image = Image.open(f"photo_{x}.jpg")

    vk = image.resize((1400, 1000))
    vk.save(f"{file_path}/photo_vk.png", "png")

    inst = image.resize((1080, 1080))
    inst.save(f"{file_path}/photo_inst.png", "png")
    
    fb = image.resize((1200, 628))
    fb.save(f"{file_path}/photo_fb.png", "png")