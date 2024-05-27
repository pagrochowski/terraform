from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from .models import SessionVisit

class SessionVisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Exclude admin routes
        if request.path.startswith(settings.ADMIN_URL):
            return

        now = timezone.now()

        # Get or create the session visit record
        session_key = request.session.session_key
        visit, _ = SessionVisit.objects.get_or_create(session_key=session_key)

        # Check for inactivity
        last_activity = visit.last_activity if visit.last_activity else now
        if now - last_activity > timedelta(minutes=5):
            visit.visit_count += 1

        # Update last activity timestamp
        visit.last_activity = now
        visit.save()
