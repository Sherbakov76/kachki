from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from sportsmens.models import Sportsmens, Categories, SportsmensSportsmensCategory, Rating
from django.contrib.auth import logout


@login_required
def categories_list(request):
    categories = Categories.objects.all()
    return render(request, "categories_list.html", {"categories": categories})


#def category(request, pk):
 #   category = get_object_or_404(Categories, id=pk)
 #   return render(request, "category.html", {"category": category})

@login_required
def category(request, a):
    #category = Sportsmens.objects.raw('SELECT sportsmens_sportsmens_category.id, sportsmens_sportsmens_category.sportsmens_id '
     #                                 'FROM sportsmens_sportsmens_category '
     #                                 'WHERE categories_id = %s', [a])
    athletes = SportsmensSportsmensCategory.objects.filter(categories=a)

    return render(request, "category.html", {"athletes": athletes})

