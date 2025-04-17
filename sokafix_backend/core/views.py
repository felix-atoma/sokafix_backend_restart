from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage, NewsletterSubscriber
from .serializers import ContactMessageSerializer, NewsletterSubscriberSerializer
from django.core.mail import send_mail

@api_view(['POST'])
def submit_contact(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        contact = serializer.save()

        # Send the email to Sokafix admin
        send_mail(
            subject=f"New Contact: {contact.subject}",
            message=f"From {contact.name} ({contact.email})\nPhone: {contact.phone}\n\n{contact.message}",
            from_email=None,  # uses DEFAULT_FROM_EMAIL
            recipient_list=['sokafix056@gmail.com'],
            fail_silently=False,
        )

        return Response({'message': 'Message received!'})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def subscribe_newsletter(request):
    serializer = NewsletterSubscriberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Subscribed successfully!'})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_messages(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    serializer = ContactMessageSerializer(messages, many=True)
    return Response(serializer.data)
