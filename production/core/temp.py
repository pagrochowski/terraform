from .models import Session
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone

class SessionMiddleware(MiddlewareMixin):  # Renamed from PageVisitMiddleware
    def process_request(self, request):
        # Check if a session exists
        if not request.session.session_key:
            request.session.save()  # Start a new session
        session_key = request.session.session_key
        try:
            # Try to get an existing session
            session = Session.objects.get(session_key=session_key)
        except Session.DoesNotExist:
            # Create a new session
            session = Session.objects.create(
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT'),
                session_key=session_key
            )
        request.session_object = session  # Store in request object

    def process_response(self, request, response):
        # Check if session was created in process_request
        if hasattr(request, 'session_object'):
            session = request.session_object
            if not session.end_time:
                session.end_time = timezone.now()
                session.duration = session.end_time - session.start_time
                session.save()

        return response
