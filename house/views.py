from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Bid, Comment, Listing, User


def index(request):
    listings = Listing.objects.filter(is_closed=False)
    context = {
        "listings": listings,
    }
    return render(request, "house/index.html", context)


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "house/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "house/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "house/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "house/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "house/register.html")

# ------------------------------------------------------------------------------------------------------------------


def close_auction(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.is_closed = True
    listing.save()
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))


def closed_listings(request):
    closed_listing = Listing.objects.filter(is_closed=True)
    context = {
        "listings": closed_listing,
    }
    return render(request, "house/closed_listing.html", context)

def update_listing(request, listing_id):
    # go to create listing page and update values
    listing = Listing.objects.get(pk=listing_id)
    print(listing.description)
    context = {
        "listing": listing,
        "is_update": True
    }
    return render(request, "house/update_listing.html", context)

def update_listing_item(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    # update listing item
    listing.title = request.POST["title"]
    listing.description = request.POST["description"]
    listing.url = request.POST["image_url"]
    listing.category = request.POST['category']
    listing.save()
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))


def delete_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.delete()
    return HttpResponseRedirect(reverse("index"))

def display_category(request):
    category = request.POST["category"]
    # listings = Listing.objects.filter(category=category)
    listings = Listing.objects.filter(category=category, is_closed=False)
    context = {
        "listings": listings,
        "is_category_page": True,
        "category": category
    }
    return render(request, "house/index.html", context)


def category_page(request):
    category = Listing.objects.all()
    category = category.values_list('category', flat=True).distinct()
    return render(request, "house/category.html", {"category": category, })


def comment(request, listing_id):
    user = request.user
    text = request.POST["comment"]
    listing = listing = Listing.objects.get(pk=listing_id)
    new_comment = Comment(text=text, writer=user, listing=listing)
    new_comment.save()
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))

def create_listing(request):
    # if user is logged in 
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            title = request.POST["title"]
            description = request.POST["description"]
            image_url = request.POST["image_url"]
            category = request.POST['category']

            # Create new bid
            bid = Bid(bid=int(request.POST["bid"]), user=user)
            bid.save()
            # Create new listing
            listing = Listing(title=title, category=category, owner=user,
                            is_closed=False, description=description, bid=bid, url=image_url)
            listing.save()

            return HttpResponseRedirect(reverse("index"))
        return render(request, "house/create_listing.html")
    else:
        return render(request, "house/login.html")


def display_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    is_listing_in_watchlist = request.user in listing.watchlist.all()
    comments = listing.comments.all()
    is_owner = request.user.username == listing.owner.username
    context = {
        "listing": listing,
        "is_listing_in_watchlist": is_listing_in_watchlist,
        "is_owner": is_owner,
        "comments": comments
    }
    return render(request, "house/listing_page.html", context)


def display_watchlist(request):
    user = request.user
    listings = user.watch_listings.all()
    context = {
        "listings": listings,
    }

    return render(request, "house/watchlist_page.html", context)


def new_bid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    current_bid = listing.bid.bid
    new_bid = bid = int(request.POST["bid"])
    if new_bid > current_bid:
        updated_bid = Bid(bid=new_bid, user=request.user)
        updated_bid.save()
        listing.bid = updated_bid
        listing.save()
        return render(request, "house/listing_page.html", {
            "listing": listing,
            "message": "Bid was updated successfully",
            "updated": True,
        })
    else:
        return render(request, "house/listing_page.html", {
            "listing": listing,
            "message": "Bid not high enough",
            "updated": False,
        })


def add_watchlist(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.add(user)
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))


def remove_watchlist(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.remove(user)
    return HttpResponseRedirect(reverse("display_listing", args=(listing_id, )))
