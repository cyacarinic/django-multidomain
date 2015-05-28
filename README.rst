Django Multi Domain
*******************

Django application, implement multi domain concept. You can choose your url config according to your domain host.

Installation
============

You can install the most recent **Django Theming** version using pip: ::

    pip install django-multidomain

Setup
=====

**NOTE**: The following settings should be added to the project file 'settings.py'.

1. Add 'multidomain' to ''INSTALLED_APPS'': ::

    INSTALLED_APPS += ( 'multidomain', )

2. Add 'multidomain.middleware.DomainMiddleware' to ''MIDDLEWARE_CLASSES'': ::

    MIDDLEWARE_CLASSES += ( 'multidomain.middleware.DomainMiddleware', )

3. Create a file for each domain you have (For example: 'domain-one.dev' and 'domain-two.dev'): ::

    * urls.py   (by default)
        from django.conf.urls import patterns, include, url
        from django.contrib import admin
        urlpatterns = patterns('',
            url(r'^admin/', include(admin.site.urls)),
        )

    * urls-one.py
        from django.conf.urls import patterns, include, url
        import one.urls
        urlpatterns = patterns(
            '',
            url(r'^', include(one.urls, namespace='one')),
        )

    * urls-two.py
        from django.conf.urls import patterns, include, url
        import two.urls
        urlpatterns = patterns(
            '',
            url(r'^', include(two.urls, namespace='one')),
        )

4. Declare host/domain urlconfig tuple ''URL_CONFIG'': ::

    URL_CONFIG = (
        (r'^(.+\.)?domain-one\.dev', 'urls-one'),
        (r'^(.+\.)?domain-two\.dev', 'urls-two'),
    )

    ROOT_URLCONF = 'urls'


Usage
=====

It should create a folder ``themes`` at the project with the following structure: ::

    project_django/
    | -- __init__.py
    | -- settings.py
    | -- wsgi.py
    | -- urls-one.py
    | -- urls-two.py
    | -- urls.py        (default/optional)


**NOTE**: We use ''django-theming'' library to manage multiple teming.


Contributing
============

Development of **django-multidomain** happens at github: https://github.com/cyacarinic/django-multidomain

Credits
=======

* Claudio Yacarini: https://github.com/cyacarinic/