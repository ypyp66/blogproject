from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost
# Create your views here.
def home(request):
    blog = Blog.objects #쿼리셋
    blog_list = Blog.objects.all() #블로그의 모든 글들을 대상으로
    paginator = Paginator(blog_list, 3) #블로그 객체 3개를 한페이지로 자르기
    page = request.GET.get('page') #request됨 페이지가 뭔지 알아내고 (key가 page인 변수)
    posts = paginator.get_page(page) #request된 페이지를 얻어온 뒤 return해준다
    return render(request, 'home.html', {'blogs':blog, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    #get_..._404(어떤class에서 object를 가져올건지, 검색조건(pk값))
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title'] #new.html에서 name에 해당하는것을 가져옮
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리셋 메소드 // blog객체에 저장한 내용들은 저장
    return redirect('/blog/'+str(blog.id)) #url은 문자형이므로 형변환

def blogpost(request):
    # 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid(): # form의 return값이 true이면 실행
            post = form.save(commit=False) # 모델 객체를 반환하되, 저장하지는 말라
                #post는 blog형 객체이다
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    # 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost() # 빈 객체 form이 생성됨
        return render(request, 'new.html', {'form':form}) #new.html에 입력공간을 만들것이기 때문이다.
