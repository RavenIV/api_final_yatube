from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return (
            f'{self.pk=}, '
            f'{self.title=:.20}, '
            f'{self.slug=}, '
            f'{self.description=:.20}'
        )


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        default_related_name = 'posts'
        ordering = ('pub_date',)

    def __str__(self):
        return (
            f'{self.text=:.20}, '
            f'{self.pub_date=}, '
            f'{self.author=}, '
            f'{self.image=}, '
            f'{self.group=}'
        )


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = 'comments'
        ordering = ('created',)

    def __str__(self):
        return (
            f'{self.author=}, '
            f'{self.post=}, '
            f'{self.text=:.20}, '
            f'{self.created=}'
        )


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_followers'
            ),
        ]

    def __str__(self):
        return f'{self.user=}, {self.following=}'
