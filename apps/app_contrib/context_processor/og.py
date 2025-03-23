#OpenGraph context processor
from urllib.parse import urljoin

from django.contrib.sites.models import Site
from django.http import HttpRequest
from django.conf import settings
from django.templatetags.static import static



def get_domain_url() -> str:
    site_domain = Site.objects.get_current().domain
    return f'https://{site_domain}'


def og_url_context_processor(request: HttpRequest) -> dict[str, str]:
    return {
        'og_url': get_domain_url()
    }

def og_image_context_processor(request: HttpRequest) -> dict[str, str]:
    site_url = get_domain_url()
    image_url = static(settings.OG_IMAGE_PATH)
    if image_url is None:
        raise NameError('OG_IMAGE_PATH is not defined.')
    return {
        "og_image": urljoin(site_url, image_url)
    }