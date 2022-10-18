from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # cвязь «один к одному» c User
    rating = models.FloatField(default=0.0)


class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE, )  # связь «один ко многим» с моделью Author;
    ARTICLE_NEWS = (
        ('A', 'article'),
        ('N', 'news'),)
    article_news = models.CharField(max_length=2,
                                    choices=ARTICLE_NEWS)

    data_create = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания;
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
    category = models.ManyToManyField(Categories)
    heading = models.CharField(max_length=255, unique=True)  # заголовок статьи/новости;
    text = models.TextField(blank=True)  # текст статьи/новости;
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.heading}: {self.text}'


    # def preview(self):
    #     start_text = (self.text[0:124])
    #     return f'{start_text} ...'
    #
    # def like_post(self):
    #     self.rating += self.rating
    #     self.save()
    #     return self.rating
    #
    # def dislike_post(self):
    #     self.rating -= self.rating
    #     self.save()
    #     return self.rating



    # def update_rating(self):
    #
    #     list_rating_post = Post.objects.filter(user=self.user).values("rating")
    #     sum_list = 0
    #     for i in list_rating_post:
    #         sum_list += i*3
    #
    #     sum_rating_author = Comment.objects.filter(user=self.user).values("rating")
    #     sum_com_list = 0
    #     for i in sum_rating_author:
    #         sum_com_list += i
    #
    #     all_post_author = Post.objects.filter(user=self.user)
    #     all_comment_post_author = Comment.objects.filter(post=all_post_author).values("rating")
    #
    #     all_sum_comment_post_author = 0
    #     for x in all_comment_post_author:
    #         all_sum_comment_post_author += all_sum_comment_post_author





# class PostCategory(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # связь «один ко многим» со встроенной моделью User
    # (комментарии может оставить любой пользователь, необязательно автор);
    text = models.TextField(blank=True)  # текст комментария;
    data_create = models.DateTimeField(auto_now_add=True)  # дата и время создания комментария;
    rating = models.FloatField(default=0.0)  # рейтинг комментария.
    #
    # def like_comment(self):
    #     self.rating += self.rating
    #     self.save()
    #     return self.rating
    #
    # def dislike_comment(self):
    #     self.rating -= self.rating
    #     self.save()
    #     return self.rating