from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task()
def order_created(order_id):
    """Задача отправки email-уведомлений при успешком оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\nYou have successfully placed an order. You order id is {order.id}.'

    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
