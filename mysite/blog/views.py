from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    new = ''
    qul = request.GET.get('m')
    if qul is not None:
        for q in qul:
            if 'А' == q:
                new += 'A'
            elif 'Б' == q:
                new += 'B'
            elif 'Д' == q:
                new += 'D'
            elif 'Э' == q:
                new += 'E'
            elif 'Е' == q:
                new += 'E'
            elif 'Ф' == q:
                new += 'F'
            elif 'Г' == q:
                new += 'G'
            elif 'Ҳ' == q:
                new += 'H'
            elif 'И' == q:
                new += 'I'
            elif 'Ж' == q:
                new += 'J'
            elif 'К' == q:
                new += 'K'
            elif 'Л' == q:
                new += 'L'
            elif 'М' == q:
                new += 'M'
            elif 'Н' == q:
                new += 'N'
            elif 'О' == q:
                new += 'O'
            elif 'П' == q:
                new += 'P'
            elif 'Қ' == q:
                new += 'Q'
            elif 'Р' == q:
                new += 'R'
            elif 'С' == q:
                new += 'S'
            elif 'Т' == q:
                new += 'T'
            elif 'У' == q:
                new += 'U'
            elif 'В' == q:
                new += 'V'
            elif 'Х' == q:
                new += 'X'
            elif 'Й' == q:
                new += 'Y'
            elif 'Ё' == q:
                new += 'YO'
            elif 'З' == q:
                new += 'Z'
            elif 'Ў' == q:
                new += "O'"
            elif 'Ғ' == q:
                new += "G'"
            elif 'Ш' == q:
                new += 'SH'
            elif 'Ч' == q:
                new += 'CH'
            elif 'Нг' == q:
                new += "Ng'"
            elif ' ' == q:
                new += " "
            elif 'Ю' == q:
                new += 'Yu'
            if 'а' == q:
                new += 'a'
            elif 'б' == q:
                new += 'b'
            elif 'д' == q:
                new += 'd'
            elif 'э' == q:
                new += 'e'
            elif 'е' == q:
                new += 'e'
            elif 'ф' == q:
                new += 'f'
            elif 'г' == q:
                new += 'g'
            elif 'ҳ' == q:
                new += 'h'
            elif 'и' == q:
                new += 'i'
            elif 'ж' == q:
                new += 'j'
            elif 'к' == q:
                new += 'k'
            elif 'л' == q:
                new += 'l'
            elif 'м' == q:
                new += 'm'
            elif 'н' == q:
                new += 'n'
            elif 'о' == q:
                new += 'o'
            elif 'п' == q:
                new += 'p'
            elif 'қ' == q:
                new += 'q'
            elif 'р' == q:
                new += 'r'
            elif 'с' == q:
                new += 's'
            elif 'т' == q:
                new += 't'
            elif 'у' == q:
                new += 'u'
            elif 'в' == q:
                new += 'v'
            elif 'х' == q:
                new += 'x'
            elif 'й' == q:
                new += 'y'
            elif 'з' == q:
                new += 'z'
            elif 'ў' == q:
                new += "o'"
            elif 'ғ' == q:
                new += "g'"
            elif 'ш' == q:
                new += 'sh'
            elif 'ч' == q:
                new += 'ch'
            elif 'нг' == q:
                new += "ng'"
            elif ' ' == q:
                new += " "
            elif 'ю' == q:
                new += 'yu'
            elif 'ё' == q:
                new += 'yo'
            elif '.' == q:
                new += '.'
            elif ',' == q:
                new += ','
            elif '"' == q:
                new += '"'

    return render(request, 'blog/post_list.html', {'posts': posts, 'new': new})
# Create your views here.
