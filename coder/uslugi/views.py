from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import *


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from comments.models import Comment
from comments.forms import CommentForm
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

def landuslugi(request):
	return render(request, 'uslugi/uslugi.html')

