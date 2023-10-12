import os
import praw
import random


def is_image(entry):
    return entry.name.endswith(".jpg")


def cats_dir():
    return os.scandir("cats")


def cat_images():
    with cats_dir() as it:
        return list(filter(is_image, it))


def post_image(reddit: praw.Reddit, path):
    reddit.subreddit("test").submit_image("Cat :3", path)


if __name__ == '__main__':
    images = cat_images()
    image = random.choice(images).path
    print(image)

    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        password=os.environ["REDDIT_PASSWORD"],
        user_agent="script:catsimages:v0.1.0 (by u/Boothwhack)",
        username=os.environ["REDDIT_USERNAME"],
    )

    post_image(reddit, image)
