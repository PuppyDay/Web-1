from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    image = models.ImageField(upload_to='static/img/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'


class TagManager(models.Manager):
    def all_tags(self):
        return self.all()


class Tag(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='Тэг')

    objects = TagManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name='Голос', choices=VOTES, default=0)
    user = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор', default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=0)
    object_id = models.PositiveIntegerField(default=0)
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ('user', 'object_id', )


class ArticleManager(models.Manager):
    def sort_new(self):
        return self.order_by('-date_create')

    def sort_hot(self):
        return self.order_by('-number_of_likes')

    def sort_questions_by_tag(self, tag):
        return self.filter(tags__title=tag).order_by('-number_of_likes')


class Article(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    number_of_likes = models.IntegerField(verbose_name='Рейтинг', default=0)
    marks = GenericRelation(LikeDislike)

    objects = ArticleManager()

    def __str__(self):
        return self.title

    def count_answers(self):
        return Answer.objects.question_answers(self.pk).count()

    def author_img(self):
        return self.author.image

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class AnswerManager(models.Manager):
    def question_answers(self, question_number):
        return self.filter(question__id=question_number).order_by('-number_of_likes')


class Answer(models.Model):
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    question = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='Вопрос')
    is_correct = models.BooleanField(default=False, verbose_name='Верно')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    number_of_likes = models.IntegerField(verbose_name='Рейтинг', default=0)
    marks = GenericRelation(LikeDislike)

    objects = AnswerManager()

    def author_img(self):
        return self.author.image

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
