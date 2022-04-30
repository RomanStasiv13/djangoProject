from news.models import Author


def add_news_statistics(request):
    return {
        "total": Author.objects.all().count()+100,
    }