from django.shortcuts import render, HttpResponse, redirect


records = [
    {
        "id": 1,
        "name": "Dojo Tshirt",
        "price": 19.99
    }, 
    {
        "id": 2,
        "name": "Dojo Sweater",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Dojo Cup",
        "price": 4.99
    },
    {
        "id": 4,
        "name": "Algorithm Book",
        "price": 49.99
    }
]


# Create your views here.
def index(request):
    context = {
        "data": records
    }
    return render(request, "store/index.html", context)


def checkout(request):
    print("========>>>>>>>> checkout")
    return render(request, "store/checkout.html")


def process(request):
    if request.method == "POST":
        item_id = int(request.POST["id"])
        qty = int(request.POST["qty"])

        price = -1
        for rec in records:
            if rec["id"] == item_id:
                price = rec["price"]
                break

        if price > 0:
            total = price * qty
            #print("Total:", total)
            if not "totalOrders" in request.session:
                request.session["totalOrders"] = 0
                request.session["totalItems"] = 0

            totalOrders = request.session["totalOrders"]
            totalItems = request.session["totalItems"]

            totalOrders += total
            totalItems += qty

            request.session["total"] = total
            request.session["totalOrders"] = totalOrders
            request.session["totalItems"] = totalItems
        else:
            request.session.flash("Something went wrong, id not found in records!", "error")

    return redirect("/store/checkout")
