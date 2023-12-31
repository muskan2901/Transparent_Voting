from django.http.response import StreamingHttpResponse
from .camera import VideoCamera, gen


def detect_person(request):
    return StreamingHttpResponse (
        gen(VideoCamera()), 
        content_type='multipart/x-mixed-replace; boundary=frame'
    )

