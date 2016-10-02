# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from filemanager import FileManager
from joshua_blog.settings import MEDIA_ROOT
import math

import urllib2
# Create your views here.

def read_md_from_url(input_url):
    try:
        if "http://joshua881228.webfactional.com" in input_url:
            return ''
        else:
            response = urllib2.urlopen(input_url, timeout=5)
            return response.read()
    except:
        return ''

def profile_view(request):
    if request.user.is_anonymous():
        user_level = 0
    else:
        user_level = request.user.profile.profile_level
    topic_list = Topic.objects.all()
    return render_to_response('about_me.html', locals(), context_instance=RequestContext(request));


def topic_archive_view(request):
    topic_list = Topic.objects.all()
    return render_to_response('topic_archive.html', locals(), context_instance=RequestContext(request))


def blog_archive_view(request, topic_name='ALL', page_idx=1):
    topic_list = Topic.objects.all()
    blog_num_per_page = 15 
    page_num_per_slide = 10
    page_idx = int(page_idx)
    start_page_idx = ((page_idx-1)/page_num_per_slide)*page_num_per_slide+1
    next_page_idx = page_idx
    prev_page_idx = page_idx
    if request.user.is_anonymous():
        user_level = 0
    else:
        user_level = request.user.profile.profile_level
    if page_idx > 1:
        prev_page_idx = page_idx-1
    if 'topic_ALL_archive' in request.path:
        blogs = Blog.objects.filter(blog_level__lte=user_level)
        archive_type = 'topic_ALL_archive'
	topic_name = 'ALL'
    else:
        topic = Topic.objects.get(topic_name=topic_name)
        blogs = topic.blog_set.filter(blog_level__lte=user_level)
        archive_type = 'topic_' + topic_name + '_archive'

    total_blog_num = len(blogs)
    total_page_num = int(math.ceil(total_blog_num/float(blog_num_per_page))) + 1
    end_page_idx = min(total_page_num, start_page_idx+page_num_per_slide)
    blog_list = blogs[(page_idx-1)*blog_num_per_page: min(page_idx*blog_num_per_page, total_blog_num)]

    for a_blog in blog_list:
        a_blog.blog_content = read_md_from_url(a_blog.blog_content_from_url)

    page_list = [x for x in range(start_page_idx, end_page_idx)]
    if page_idx < total_page_num:
        next_page_idx = page_idx+1
    prev_block = start_page_idx - 1
    next_block = end_page_idx
    return render_to_response('blog_archive.html', locals(), context_instance=RequestContext(request))

def blog_list_view(request, topic_name='ALL', page_idx=1):
    topic_list = Topic.objects.all()
    blog_num_per_page = 5
    page_num_per_slide = 10
    page_idx = int(page_idx)
    start_page_idx = ((page_idx-1)/page_num_per_slide)*page_num_per_slide+1
    next_page_idx = page_idx
    prev_page_idx = page_idx
    if request.user.is_anonymous():
        user_level = 0
    else:
        user_level = request.user.profile.profile_level
    if page_idx > 1:
        prev_page_idx = page_idx-1
    if 'topic_ALL_list' in request.path:
        blogs = Blog.objects.filter(blog_level__lte=user_level)
        archive_type = 'topic_ALL_list'
        topic_name = 'ALL'
    else:
        topic = Topic.objects.get(topic_name=topic_name)
        blogs = topic.blog_set.filter(blog_level__lte=user_level)
        archive_type = 'topic_' + topic_name + '_list'

    total_blog_num = len(blogs)
    total_page_num = int(math.ceil(total_blog_num/float(blog_num_per_page))) + 1
    end_page_idx = min(total_page_num, start_page_idx+page_num_per_slide)
    blog_list = blogs[(page_idx-1)*blog_num_per_page: min(page_idx*blog_num_per_page, total_blog_num)]
    for a_blog in blog_list:
        a_blog.blog_content = read_md_from_url(a_blog.blog_content_from_url)
    page_list = [x for x in range(start_page_idx, end_page_idx)]
    if page_idx < total_page_num:
        next_page_idx = page_idx+1
    prev_block = start_page_idx - 1
    next_block = end_page_idx
    return render_to_response('blog_list.html', locals(), context_instance=RequestContext(request))


def blog_view(request, input_url):
    if request.user.is_anonymous():
        user_level = 0
    else:
        user_level = request.user.profile.profile_level
    topic_list = Topic.objects.all()
    blog_id = int(input_url[input_url.rfind('_')+1:])
    post_blog = Blog.objects.get(id=blog_id)
    post_blog.blog_content = read_md_from_url(post_blog.blog_content_from_url)
    add_comment_url = 'add_comment_to_blog_%s' % blog_id
    return render_to_response('blog_view.html', locals(), context_instance=RequestContext(request))


def conversation_archive_view(request):
    conv_flag = 'ALL'
    topic_list = Topic.objects.all()
    conversation_list = Conversation.objects.all()
    return render_to_response('conversation_archive.html', locals(), context_instance=RequestContext(request))


def conversation_view(request, input_idx):
    if request.user.is_anonymous():
        user_level = 0
    else:
        user_level = request.user.profile.profile_level
    topic_list = Topic.objects.all()
    a_conversation = Conversation.objects.get(id=input_idx)
    conv_flag = a_conversation.conversation_title
    comment_list = a_conversation.commenttoconversation_set.all()
    add_comment_url = 'add_comment_to_conversation_%d' % a_conversation.id
    return render_to_response('conversation_view.html', locals(), context_instance=RequestContext(request))


@login_required
def blog_add_view(request):
    level_list = blog_level_list
    topic_list = Topic.objects.all()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            a_blog = Blog(blog_title=request.POST.get('blog_title'),
                          blog_content=request.POST.get('blog_content'),
                          blog_tag=request.POST.get('blog_tag'),
                          blog_level=blog_level_dict[request.POST.get('blog_level')],
                          blog_topic=Topic.objects.get(topic_name=request.POST.get('blog_topic'))
                          )
            a_blog.save()
            return HttpResponseRedirect('/%s' % a_blog.get_url())
    else:
        form = BlogForm()
    flag = 'new blog'
    return render_to_response('edit_blog.html', locals(), context_instance=RequestContext(request))


@login_required
def blog_update_view(request, input_id):
    a_blog = get_object_or_404(Blog, pk=int(input_id))
    level_list = blog_level_list
    topic_list = Topic.objects.all()
    selected_level = level_list[a_blog.blog_level]
    selected_topic = a_blog.blog_topic
    if request.method == "POST":
        form = BlogForm(request.POST, instance=a_blog)
        if form.is_valid():
            a_blog.blog_title = request.POST.get('blog_title')
            a_blog.blog_content = request.POST.get('blog_content')
            a_blog.blog_tag = request.POST.get('blog_tag')
            a_blog.blog_level = blog_level_dict[request.POST.get('blog_level')]
            a_blog.blog_topic = Topic.objects.get(topic_name=request.POST.get('blog_topic'))
            a_blog.save()
            return HttpResponseRedirect('/%s' % a_blog.get_url())
    else:
        form = BlogForm(instance=a_blog)
    flag = 'edit blog'
    return render_to_response('edit_blog.html', locals(), context_instance=RequestContext(request))


@login_required
def blog_delete_view(request, input_id):
    a_blog = get_object_or_404(Blog, pk=int(input_id))
    a_blog.delete()
    return HttpResponseRedirect('/topic_ALL_archive/')


def comment_add_view(request, input_id=-1):
    if request.user.is_anonymous():
        user_level = 0
    else:
        user_level = request.user.profile.profile_level
    topic_list = Topic.objects.all()
    
    if 'add_comment_to_conversation_' in request.path:
        flag = 'new comment'
        comment_content = request.POST.get('comment_content')
        comment_nickname = request.POST.get('comment_nickname')
        a_conversation = Conversation.objects.get(id=input_id)
        if (comment_content is not None) and (comment_nickname is not None):
            a_comment = CommentToConversation(comment_nickname=comment_nickname,
                                              comment_content=comment_content, comment_conversation=a_conversation)
            a_comment.save()
            return HttpResponseRedirect('/%s' % a_conversation.get_url())
    elif 'add_conversation' in request.path:
        flag = 'new conversation'
        add_comment_url = 'add_conversation'
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_content = request.POST.get('comment_content')
                comment_nickname = request.POST.get('comment_nickname')
                if (comment_content is not None) and (comment_nickname is not None):
                    a_conversation = Conversation(creator=comment_nickname)
                    a_conversation.save()
                    a_comment = CommentToConversation(comment_nickname=comment_nickname,
                                                      comment_content=comment_content, comment_conversation=a_conversation)
                    a_comment.save()
                    return HttpResponseRedirect('/%s' % a_conversation.get_url())
        else:
            form = CommentForm()
        return render_to_response('add_comment.html', locals(), context_instance=RequestContext(request))


@login_required
def comment_delete_view(request, input_id):
    if request.method == 'GET':
        request.session['deletion_from'] = request.META.get('HTTP_REFERER', '/')
    a_comment = get_object_or_404(Comment, pk=int(input_id))
    a_comment.delete()
    return HttpResponseRedirect(request.session['deletion_from'])


@login_required
def filemanager_view(request, path):
    fm = FileManager(MEDIA_ROOT+'uploads/')
    return fm.render(request,path)
