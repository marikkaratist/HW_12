import json
from exception import DataLayerError


class PostManager:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        """Загружает все посты"""

        with open(self.path, encoding="utf-8") as file:
            posts = json.load(file)

        return posts

    def get_posts_by_text(self, text):
        """Возвращает список постов по ключевому слову"""

        posts = self.load_posts()
        posts_list = []
        for post in posts:
            text_lower = text.lower()
            if text_lower in post["content"].lower():
                posts_list.append(post)

        return posts_list

    def add_post(self, post):
        """Добавляет новый пост в список постов"""
        posts = self.load_posts()
        posts.append(post)
        self.save_post_to_json(posts)

    def save_post_to_json(self, posts):
        """Сохраняет данные нового поста в JSON"""
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(posts, file, ensure_ascii=False)
        except FileNotFoundError:
            raise DataLayerError
