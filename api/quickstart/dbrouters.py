class DbRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['quickstart']:
            return 'SCHIPAnnualReports'
        # Returning None is no opinion, defer to other routers or default database
        return None