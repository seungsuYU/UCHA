from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post


# Create your views here.

def index(request):
    return render(request, 'post/index.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'post/post_detail.html', context)

@require_POST
def post_create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 여기서 게시글을 생성하고 저장하는 로직을 추가하세요
    if title and content:
        new_post = Post(title=title, content=content)
        new_post.save()
        return JsonResponse({'message': '게시글이 성공적으로 등록되었습니다.'}, status=200)
    else:
        return JsonResponse({'message': '게시글 등록에 실패했습니다.'}, status=400)