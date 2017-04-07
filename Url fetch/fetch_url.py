import random
import urllib.request


def get_web_img(url):
    name = random.randrange(1,100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)


get_web_img("https://pbs.twimg.com/profile_images/715373687424163840/YXiU1VWl.jpg")

