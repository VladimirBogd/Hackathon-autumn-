def classFactory(iface):
    from .ndvi import NdviPlugin
    return NdviPlugin(iface)