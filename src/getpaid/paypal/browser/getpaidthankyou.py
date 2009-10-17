from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class GetpaidPayPalThankyouView(BrowserView):
    """Class for overriding getpaid-thank-you view for paypal purchases
    """
    
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getInvoice(self):
        if self.request.has_key('invoice'):
            return self.request['invoice']
        else:
            return None

    def getURL(self):
        portalurl = getToolByName(self.context, "portal_url").getPortalObject().absolute_url()
        if self.getInvoice() is not None:
            return "%s/@@getpaid-order/%s" % ( portalurl, self.getInvoice())
        else:
            return ''
