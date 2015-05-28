import re
from django.conf import settings

class DomainMiddleware(object):
    def process_request(self, request):
        url_config = getattr(settings, 'URL_CONFIG', None)
        if url_config:
            try:
                host = request.get_host()
                for (regex, value) in url_config:
                    if re.search(regex, host):
                        request.urlconf = value
                        break
            except Exception, e:
                print str(e)
                pass