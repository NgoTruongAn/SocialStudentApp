from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    avatar = CloudinaryField(null=True)
    cover_photo = CloudinaryField(null=True)
    role = models.CharField(max_length=20, choices=[('alumni', 'Cựu sinh viên'), ('teacher', 'Giảng viên'), ('admin', 'Quản trị viên')])
    is_active = models.BooleanField(default=True)
    must_change_password = models.BooleanField(default=False)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextField(blank=True)

    def __str__(self):
        return self.user.username


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    media_url = CloudinaryField(null=True, blank=True)
    allow_comments = models.BooleanField(default=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Interaction(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(Interaction):
    content = models.CharField(max_length=255)


class Reaction(Interaction):
    type = models.CharField(max_length=20, choices=[('like', 'Like'), ('haha', 'Haha'), ('love', 'Love')])

    class Meta:
        unique_together = ('post', 'user')


class Survey(BaseModel):
    title = models.CharField(max_length=255)
    description = RichTextField()
    content = RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_surveys')

    def __str__(self):
        return self.title


class SurveyResponse(BaseModel):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = RichTextField()

    def __str__(self):
        return f'{self.user.username} - {self.survey.title}'


class Notification(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_notifications')
    target_group = models.CharField(max_length=20, choices=[('all', 'All'), ('group', 'Group'), ('individual', 'Individual')])
    target_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Group(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name



