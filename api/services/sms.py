import africastalking
from django.conf import settings

def initialize_africastalking():
    africastalking.initialize(
        username=settings.AT_USERNAME,
        api_key=settings.AT_API_KEY
    )
    return africastalking.SMS

def send_order_notification(order):
    sms = initialize_africastalking()
    
    message = f"Dear {order.customer.name}, your order for {order.item} "
    message += f"worth ${order.amount} has been received. Thank you for shopping with us!"
    
    try:
        response = sms.send(
            message=[message],
            recipients=[order.customer.phone],
            sender_id=settings.AT_SENDER_ID
        )
        return response
    except Exception as e:
        # Log the error
        print(f"Error sending SMS: {str(e)}")
        return None