from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment


def todo():
    johny_user = User.objects.create_user(username='johny', email='johny@mail.ru', password='johny_password')
    tommy_user = User.objects.create_user(username='tommy', email='tommy@mail.ru', password='tommy_password')

    johny = Author.objects.create(user=johny_user)
    tommy = Author.objects.create(user=tommy_user)

    # создание категорий
    cat_sport = Category.objects.create(name="Спорт")
    cat_music = Category.objects.create(name="Музыка")
    cat_cinema = Category.objects.create(name="Кино")
    cat_IT = Category.objects.create(name="IT")

    # создание текстов статей/новостей
    text_article_sport_cinema = """статья_спорт_кино_Джонни__статья_спорт_кино_Джонни__статья_спорт_кино_Джонни_
                                   _статья_спорт_кино_Джонни__статья_спорт_кино_Джонни__"""

    text_article_music = """статья_музыка_Томми__статья_музыка_Томми__статья_музыка_Томми_
                            _статья_музыка_Томми__статья_музыка_Томми__"""

    text_news_IT = """новость_IT_Томми__новость_IT_Томми__новость_IT_Томми__новость_IT_Томми__
                    новость_IT_Томми__новость_IT_Томми__новость_IT_Томми__новость_IT_Томми__"""

    # создание двух статей и новости
    article_johny = Post.objects.create(author=johny, post_type=Post.article, title="статья_спорт_кино_Джонни",
                                        text=text_article_sport_cinema)
    article_tommy = Post.objects.create(author=tommy, post_type=Post.article, title="статья_музыка_Томми",
                                        text=text_article_music)
    news_tommy = Post.objects.create(author=tommy, post_type=Post.news, title="новость_IT_Томми", text=text_news_IT)

    # присваивание категорий этим объектам
    PostCategory.objects.create(post=article_johny, category=cat_sport)
    PostCategory.objects.create(post=article_johny, category=cat_cinema)
    PostCategory.objects.create(post=article_tommy, category=cat_music)
    PostCategory.objects.create(post=news_tommy, category=cat_IT)

    # создание комментариев
    comment1 = Comment.objects.create(post=article_johny, user=tommy.user, text="коммент Томми №1 к статье Джонни")
    comment2 = Comment.objects.create(post=article_tommy, user=johny.user, text="коммент johny №2 к статье Томми")
    comment3 = Comment.objects.create(post=news_tommy, user=tommy.user, text="коммент Томми №3 к новости Томми")
    comment4 = Comment.objects.create(post=news_tommy, user=johny.user, text="коммент johny №4 к новости Томми")
