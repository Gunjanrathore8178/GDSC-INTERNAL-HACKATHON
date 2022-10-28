from django.shortcuts import render
import razorpay

# Create your views here.


def index(request):
    return render(request, 'index.html')


def widget(request):
    return render(request, 'widget.html')

def newsletter(request):
    return render(request, 'newsletter.html')

def globe(request):
    return render(request,'globe.html')


def map(request):
    return render(request, 'map.html')


def pay(request):
    if request.method == 'POST':
        ammount = 500
        currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_DW2N1phxMP2TCQ', 'JuMjNSLvhEXAcP8S0fsfe5J3'))

        payment = client.order.create(
            {'ammount': ammount, 'currency': currency, 'payment_capture': '1'})
        iid = payment['id']
        data = {'ammount': ammount, 'iid': iid}
        return render(request, 'pay.html', data)

    else:
        return render(request, 'pay.html')
