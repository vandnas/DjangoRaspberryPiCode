from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.http import HttpResponse

from .models import books

def print1(request):
	return HttpResponse("You're looking at book.")

def print2(request,book_id):
	return HttpResponse("You're looking at book %s." % book_id)

#POST REQUEST
def register(request):
	print "INSIDE REGISTER FUNCTION"
    	if request.method == "POST":
		print "INSIDE POST"
		print "request.POST['book_id']",request.POST['book_id']
		print "request.POST['book_name']",request.POST['book_name']
		b = books(book_id=request.POST['book_id'],book_name=request.POST['book_name'], book_author=request.POST['book_author'])
		print "SAVING"
		b.save()
		print "RETURNING"
		#return render(request, "books/index.html", b)
		return HttpResponse("OK")
	else:
		print "Its a GET request"
		return render(request, "books/gets.html")

#GET REQUEST (specific)
def selectspecificbook(request, book_id):
	b = get_object_or_404(books, pk=book_id)
	print "books",b
	return HttpResponse(b)


#GET REQUEST (all)
def selectallbooks(request):
	print "INSIDE selectallbooks FUNCTION"
        #b = get_object_or_404(books)
	book_list=[]
        b = books.objects.all()
	for book in b:
		print "book:",book
		book_list.append(book)
		book_list.append(", ")
        return HttpResponse(book_list)


#DELETE REQUEST (specific) ...GET request
def deletespecificbook(request, book_id):
	b = get_object_or_404(books, pk=book_id)
	print "books",b
	b.delete()
	return HttpResponse("DELETED")


#DELETE REQUEST (all) ...GET request
def deleteallbooks(request):
	b = books.objects.all()
	print "books",b
	b.delete()
	return HttpResponse("DELETED ALL BOOKS")

