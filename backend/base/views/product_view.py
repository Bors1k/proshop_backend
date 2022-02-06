from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.serializer import ProductSerializer
from base.models import Product
from rest_framework.response import Response


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    data = request.data

    product = Product.objects.create(
        user=user,
        name='Sample name',
        price=0,
        brand='sample brand',
        countInStock=0,
        category='Sample category',
        description='description',
        rating=0,
    )

    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    user = request.user
    data = request.data

    product = Product.objects.get(id=pk)

    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']

    product.save()

    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delProductById(request, pk):
    product = Product.objects.get(id=pk)

    product.delete()

    return Response('Product was deleted')

@api_view(['POST'])
def uploadImage(request):
    data = request.data
    
    product_id = data['product_id']
    
    product = Product.objects.get(id=product_id)

    product.image = request.FILES.get('image')
    product.save()

    return Response('Image was uploaded')