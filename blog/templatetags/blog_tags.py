from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-posts.html')
def latestpost():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-categories.html')
def postcategory():
    posts = Post.objects.filter(status=1)
    catgories = Category.objects.all()
    cat_dict = {}
    for name in catgories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'category':cat_dict}
