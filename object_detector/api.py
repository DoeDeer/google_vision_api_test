# -*- coding: utf-8 -*-

"""Project API views."""

from google.cloud import vision
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def get_image_objects_by_url(image_url):
    """Localize objects in the image on given url.

    Args:
        image_url: image url.

    Returns:
        List of detected on image objects.

    """
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = image_url

    objects = client.object_localization(  # noqa: WPS110
        image=image).localized_object_annotations  # noqa: WPS319
    return [object_.name for object_ in objects]


class DetectObjectsAPIView(APIView):  # as class
    """View class, that detecting objects on passed image."""

    def get(self, request):
        """Handle GET request and give response.

        Args:
            request: django wsgi request.

        Returns:
            JSON response.

        """
        image_url = request.GET.get('image_url')
        on_image_objects = self.get_objects(image_url)
        return Response({'objects': on_image_objects})

    def get_objects(self, image_url):
        """Localize objects in the image on given url.

        Args:
            image_url: image url.

        Returns:
            List of detected on image objects.

        """
        return get_image_objects_by_url(image_url)


@api_view(['get'])
def detect_objects(request):  # as method
    """Localize objects on given image.

    Args:
        request: django wsgi request.

    Returns:
        JSON response with found objects.
    """
    image_url = request.GET.get('image_url')
    on_image_objects = get_image_objects_by_url(image_url)

    return Response({'objects': on_image_objects})
