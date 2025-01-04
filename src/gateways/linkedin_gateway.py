import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lib'))

import requests
from bs4 import BeautifulSoup
from entities.comment import Comment

class LinkedInGateway:
    def __init__(self, headers):
        self.headers = headers

    def fetch_comments(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        sections = soup.find_all("section", class_="comment flex grow-1 items-stretch leading-[16px] comment-with-action my-1.5")

        comments = []
        for section in sections:
            author = section.find("a", class_="text-sm link-styled no-underline leading-open comment__author truncate pr-6")
            avatar = section.find("img")
            date = section.find("span", class_="text-xs text-color-text-low-emphasis comment__duration-since absolute right-6 top-1 inline-block")
            content = section.find("p", class_="attributed-text-segment-list__content text-color-text !text-sm whitespace-pre-wrap break-words comment__text babybear:mt-0.5")

            comment = Comment(
                author=author.text.strip(),
                avatar=avatar["data-delayed-url"],
                date=date.text.strip(),
                content=content.text.strip()
            )
            comments.append(comment)

        return comments