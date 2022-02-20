from django.shortcuts import render
from .models import Post
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline

# Create your views here.


def home(request):
    qs = Post.objects.all()
    query = request.GET.get("query")
    if query:
        # qs = Post.objects.filter(title__icontains=query)
        # qs = Post.objects.annotate(search=SearchVector("title", "content")).filter(
        #     search=SearchQuery(query)
        # )
        qs = Post.objects.annotate(
            headline=SearchHeadline(
                "content",
                SearchQuery(query),
                start_sel="<b><u><i>",
                stop_sel="</i></u></b>",
            )
        )
    return render(request, "index.html", context={"queryset": qs})
