from django.contrib import admin

# Register your models here.
from models import Topic, Blog, Comment, Conversation, CommentToConversation


class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_name',)
    ordering = ('-topic_name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_pub_date', 'blog_tag', 'blog_level',)
    ordering = ('-blog_pub_date',)


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('creator', 'conversation_pub_date', 'conversation_title')
    ordering = ('-conversation_pub_date',)


class CommentToConversationAdmin(admin.ModelAdmin):
    list_display = ('comment_nickname', 'comment_conversation', 'comment_pub_date',)
    ordering = ('-comment_pub_date',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(CommentToConversation, CommentToConversationAdmin)