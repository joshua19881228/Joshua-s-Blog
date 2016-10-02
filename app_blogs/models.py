# -*- coding:utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from unidecode import unidecode
# Create your models here.
blog_level_dict = {'visitor': 0, 'friend': 1, 'close friend': 2}
blog_level_list = ['visitor', 'friend', 'close friend']


class Topic(models.Model):
    topic_name = models.CharField('Topic Name', max_length=64)
    topic_description = models.TextField('Description')
    topic_image = models.ImageField('Description Image', blank=True)

    def get_url(self):
        return 'topic_%s_archive' % self.topic_name

    def __unicode__(self):
        return self.topic_name

    class Meta:
        ordering = ('topic_name',)
        verbose_name = 'Topic'


class Blog(models.Model):
    # The attributes of Blog app 
    blog_title = models.CharField('Title', max_length=1024)
    blog_pub_date = models.DateTimeField('Publish Date', auto_now_add=True)
    blog_content = models.TextField('Content')
    blog_content_from_url = models.CharField(verbose_name='Content from URL', max_length=1024)
    blog_topic = models.ForeignKey(Topic, verbose_name='Topic')
    blog_tag = models.CharField('Tag', max_length=200, default='default')
    blog_level = models.IntegerField('Level', default=0)

    # return dynamic url for each blog
    def get_url(self):
        return 'blog_%s_%d' % (slugify(unidecode(self.blog_title)), self.id)

    def update_url(self):
        return 'update_blog_%d' % self.id

    def delete_url(self):
        return 'delete_blog_%d' % self.id

    def __unicode__(self):
        return self.blog_title

    #the Meta class is used to order blogs by post date
    class Meta:
        ordering = ('-blog_pub_date', )
        verbose_name = 'Blog'


class Conversation(models.Model):
    conversation_pub_date = models.DateTimeField('Conversation Date', auto_now_add=True)
    creator = models.CharField('Creator', max_length=32)
    conversation_title = models.CharField('Title', max_length=32, blank=True, null=True)

    def get_url(self):
        return 'conversation_%d' % self.id
        
    def __unicode__(self):
        return self.creator

    class Meta:
        ordering = ('-conversation_pub_date', )
        verbose_name = 'Conversation'


class Comment(models.Model):
    comment_nickname = models.CharField('Nickname', max_length=32)
    comment_reply_target = models.CharField('Target', max_length=32, blank=True, null=True)
    comment_pub_date = models.DateTimeField('Comment Date', auto_now_add=True)
    comment_content = models.TextField('Content')
    
    def delete_url(self):
        return 'delete_comment_%d' % self.id
    
    def __unicode__(self):
        return self.comment_nickname

    class Meta:
        ordering = ('-comment_pub_date', )
        verbose_name = 'Comment'


class CommentToConversation(Comment):
    comment_conversation = models.ForeignKey(Conversation, verbose_name='Comment to Conversation')

    class Meta:
        ordering = ('-comment_pub_date', )
        verbose_name = 'Comment to Conversation'


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name', 'topic_description', 'topic_image']


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_tag', 'blog_content', 'blog_content_from_url']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_nickname', 'comment_reply_target', 'comment_content']
