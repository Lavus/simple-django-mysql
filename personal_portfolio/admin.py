from django.contrib.admin.sites import AdminSite

class MyAdminSite(AdminSite):
    pass
    #ou sobrescrever alguns métodos para funcionalidades diferentes

localadmin = MyAdminSite(name="localadmin")
RDSadmin = MyAdminSite(name="RDSadmin")
otherRDSadmin = MyAdminSite(name="otherRDSadmin")