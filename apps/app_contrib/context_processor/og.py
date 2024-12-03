#OpenGraph context processor
from urllib.parse import urljoin

from django.http import HttpRequest
from django.conf import settings
from django.templatetags.static import static


def og_image_context_processor(request: HttpRequest):
    site_url = request.build_absolute_uri()
    image_url = static(settings.OG_IMAGE_PATH)
    if image_url is None:
        raise NameError('OG_IMAGE_PATH is not defined.')
    return {
        "og_image": urljoin(site_url, image_url)
    }