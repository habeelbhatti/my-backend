# myorders/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem

@api_view(['POST'])
def create_order(request):
    data = request.data

    try:
        # 1. Create the Order
        order = Order.objects.create(
            full_name=data['full_name'],
            phone=data['phone'],
            email=data['email'],
            address=data['address'],
            city=data['city'],
            area=data['area'],
            postal_code=data['postal_code'],
            payment_method=data['payment_method'],
            total_amount=data['total_amount'],
            discount=data.get('discount', 0)
        )

        # 2. Create the Order Items
        for item in data.get('items', []):
            OrderItem.objects.create(
                order=order,
                product_name=item['product_name'],
                quantity=item['quantity'],
                price=item['price'],
                image=item['image']
            )

        return Response({'message': 'Order saved successfully!'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)