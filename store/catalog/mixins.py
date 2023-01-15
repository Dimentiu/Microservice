from django.views.decorators.cache import cache_page


class CacheMixin(object):
    cache_timeout = 0

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.cache_timeout)(
            super(CacheMixin, self.dispatch)(*args, **kwargs))
