from plonetheme.classic.browser.interfaces import ILegacyThemeSpecific

class IThemeSpecific(ILegacyThemeSpecific):
    """ Plone tableless depends on the classic theme. Use this layer
        to make sure it continues to get the old viewlet order.
    """
    
