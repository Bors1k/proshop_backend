from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from base import serializer

from base.models import OrderItem, Product, Order, ShippingAddress
from base.serializer import UserSerializer, MyTokenObtainPairSerializer, OrderSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItem(request):

    user = request.user
    data = request.data

    orderItems = data['orderItems']

    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice']
        )

    shipping = ShippingAddress.objects.create(
        order=order,
        address=data['shippingAddress']['address'],
        city=data['shippingAddress']['city'],
        postalCode=data['shippingAddress']['postCode'],
        country=data['shippingAddress']['country'],
    )

    order.taxPrice = 0
    order.shippingPrice = 0
    order.totalPrice = 0

    for i in orderItems:
        product = Product.objects.get(id=i['product'])
        qty = 0
        if product.countInStock == 0:
            order.delete()
            shipping.delete()
            return Response({'detail': 'Count some items in order equal 0. Go back to cart, and check count of items.'}, status=status.HTTP_400_BAD_REQUEST)

        if i['qty'] > product.countInStock:
            qty = product.countInStock

        else:
            qty = i['qty']

        order.taxPrice += float((int(qty) * float(i['price'])) * 0.082)
        order.totalPrice += float(int(qty) * float(i['price']))

        item = OrderItem.objects.create(
            product=product,
            order=order,
            name=product.name,
            qty=qty,
            price=i['price'],
            image=product.image.url,

        )

        product.countInStock -= item.qty
        product.save()

    if order.totalPrice < 100:
        order.shippingPrice += 10
        order.totalPrice += order.shippingPrice 

    order.save()

    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)
