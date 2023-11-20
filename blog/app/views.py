from django.shortcuts import render


def test_for_digit(str_):
    for ch in str_:
        if ch.isdigit():
            return False
    return True


def main_page_view(request):
    # context = {}

    return render(request, 'main_index.html')


def page_post_view(request):
    return render(request, 'page_post.html')


def create_post(request):
    return render(request, 'create_post.html')

