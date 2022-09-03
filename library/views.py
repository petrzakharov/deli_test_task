from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView

from library.forms import BookForm
from library.models import Book


class Index(ListView):
    model = Book
    template_name = 'library/index_new.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'library/book_detail_new.html'


class AddBook(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = BookForm()
        context = {'form': form}
        return render(request, 'library/book_add.html', context)

    def post(self, request):
        if request.user.is_anonymous:
            return HttpResponse(status=403)
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(
                reverse_lazy(
                    "book_detail", kwargs={"pk": instance.id}
                )
            )
        return render(request, "library/book_add.html", {"form": form})
