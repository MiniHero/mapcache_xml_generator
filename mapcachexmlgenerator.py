from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *
from lxml import etree

from .ui.interface import Ui_MapcacheXmlGenerator

_toUtf8 = lambda s: unicode(s).encode('utf8')


class MapcacheXmlGenerator(QDialog, Ui_MapcacheXmlGenerator):

    def __init__(self, iface, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.legend = self.iface.legendInterface()
        
#         layers = self.legend.layers()
#         firstLayer = layers[0]
        
#         uri = QgsDataSourceURI( firstLayer.source() )
#         self.txtPostgresHost.setText(uri.host())
#         self.txtPostgresUser.setText(uri.username())
#         self.txtPostgresPassword.setText(uri.password())
#         self.txtPostgresDbname.setText(uri.database())
#         self.txtPostgresPort.setText(uri.port())

        QObject.connect( self.btnChooseFile, SIGNAL("clicked()"), self.selectXmlConfigFile )

    def selectXmlConfigFile(self):
        # retrieve the last used map file path
        settings = QSettings()
        lastUsedFile = settings.value("/mapcache_xml_generator/lastUsedFile", "", type=str)

        # ask for choosing where to store the map file
        filename = QFileDialog.getSaveFileName(self, "Select where to save the xml config file", lastUsedFile, "XmlFile (*.xml)")
        if filename == "":
            return

        # store the last used map file path
        settings.setValue("/mapcache_xml_generator/lastUsedFile", filename)
        # update the displayd path
        self.txtXmlConfigFilePath.setText( filename )

    def accept(self):
        # check user inputs
        if self.txtXmlConfigFilePath.text() == "":
            QMessageBox.warning(self, "Mapcache xml generator", "xml output path is required")
            return
        
        mapcache = etree.Element("mapcache")

        if(self.txtCacheName_1.text() != ""):
            cache1 = etree.Element("cache")
            cache1.set("name", self.txtCacheName_1.text())
            if(self.txtCacheType_1.text() != ""):
                cache1.set("type", self.txtCacheType_1.text())
            if(self.txtCacheLayout_1.text() != ""):
                cache1.set("layout", self.txtCacheLayout_1.text())
            if(self.txtCacheTemplate_1.text() != ""):
                cacheTemplate1 = etree.Element("template")
                cacheTemplate1.text = self.txtCacheTemplate_1.text()
                cache1.append(cacheTemplate1)
            if(self.txtCacheBase_1.text() != ""):
                cacheBase1 = etree.Element("base")
                cacheBase1.text = self.txtCacheTemplate_1.text()
                cache1.append(cacheBase1)
            if(self.txtCacheHost_1.text() != ""):
                cacheServer1 = etree.Element("server")
                cacheServerHost1 = etree.Element("host")
                cacheServerHost1.text = self.txtCacheHost_1.text()
                cacheServer1.append(cacheServerHost1)
                if(self.txtCachePort_1.text() != ""):
                    cacheServerPort1 = etree.Element("port")
                    cacheServerPort1.text = self.txtCachePort_1.text()
                    cacheServer1.append(cacheServerPort1)
                cache1.append(cacheServer1)
            if(self.txtCacheDbfile_1.text() != ""):
                cacheDbfile1 = etree.Element("dbfile")
                cacheDbfile1.text = self.txtCacheDbfile_1.text()
                cache1.append(cacheDbfile1)
            if(self.txtCacheXcount_1.text() != ""):
                cacheXcount1 = etree.Element("xcount")
                cacheXcount1.text = self.txtCacheXcount_1.text()
                cache1.append(cacheXcount1)
            if(self.txtCacheYcount_1.text() != ""):
                cacheYcount1 = etree.Element("ycount")
                cacheYcount1.text = self.txtCacheYcount_1.text()
                cache1.append(cacheYcount1)
            mapcache.append(cache1)
            
        if(self.txtCacheName_2.text() != ""):
            cache2 = etree.Element("cache")
            cache2.set("name", self.txtCacheName_2.text())
            if(self.txtCacheType_2.text() != ""):
                cache2.set("type", self.txtCacheType_2.text())
            if(self.txtCacheLayout_2.text() != ""):
                cache2.set("layout", self.txtCacheLayout_2.text())
            if(self.txtCacheTemplate_2.text() != ""):
                cacheTemplate2 = etree.Element("template")
                cacheTemplate2.text = self.txtCacheTemplate_2.text()
                cache1.append(cacheTemplate2)
            if(self.txtCacheBase_2.text() != ""):
                cacheBase2 = etree.Element("base")
                cacheBase2.text = self.txtCacheTemplate_2.text()
                cache2.append(cacheBase2)
            if(self.txtCacheHost_2.text() != ""):
                cacheServer2 = etree.Element("server")
                cacheServerHost2 = etree.Element("host")
                cacheServerHost2.text = self.txtCacheHost_2.text()
                cacheServer2.append(cacheServerHost2)
                if(self.txtCachePort_2.text() != ""):
                    cacheServerPort2 = etree.Element("port")
                    cacheServerPort2.text = self.txtCachePort_2.text()
                    cacheServer2.append(cacheServerPort2)
                cache2.append(cacheServer2)
            if(self.txtCacheDbfile_2.text() != ""):
                cacheDbfile2 = etree.Element("dbfile")
                cacheDbfile2.text = self.txtCacheDbfile_2.text()
                cache2.append(cacheDbfile2)
            if(self.txtCacheXcount_2.text() != ""):
                cacheXcount2 = etree.Element("xcount")
                cacheXcount2.text = self.txtCacheXcount_2.text()
                cache2.append(cacheXcount2)
            if(self.txtCacheYcount_2.text() != ""):
                cacheYcount2 = etree.Element("ycount")
                cacheYcount2.text = self.txtCacheYcount_2.text()
                cache2.append(cacheYcount2)
            mapcache.append(cache2)
            
        if(self.txtCacheName_3.text() != ""):
            cache3 = etree.Element("cache")
            cache3.set("name", self.txtCacheName_3.text())
            if(self.txtCacheType_1.text() != ""):
                cache3.set("type", self.txtCacheType_3.text())
            if(self.txtCacheLayout_1.text() != ""):
                cache3.set("layout", self.txtCacheLayout_3.text())
            if(self.txtCacheTemplate_3.text() != ""):
                cacheTemplate3 = etree.Element("template")
                cacheTemplate3.text = self.txtCacheTemplate_3.text()
                cache3.append(cacheTemplate3)
            if(self.txtCacheBase_3.text() != ""):
                cacheBase3 = etree.Element("base")
                cacheBase3.text = self.txtCacheTemplate_3.text()
                cache3.append(cacheBase3)
            if(self.txtCacheHost_3.text() != ""):
                cacheServer3 = etree.Element("server")
                cacheServerHost3 = etree.Element("host")
                cacheServerHost3.text = self.txtCacheHost_3.text()
                cacheServer3.append(cacheServerHost3)
                if(self.txtCachePort_3.text() != ""):
                    cacheServerPort3 = etree.Element("port")
                    cacheServerPort3.text = self.txtCachePort_3.text()
                    cacheServer3.append(cacheServerPort3)
                cache3.append(cacheServer3)
            if(self.txtCacheDbfile_3.text() != ""):
                cacheDbfile3 = etree.Element("dbfile")
                cacheDbfile3.text = self.txtCacheDbfile_3.text()
                cache3.append(cacheDbfile3)
            if(self.txtCacheXcount_3.text() != ""):
                cacheXcount3 = etree.Element("xcount")
                cacheXcount3.text = self.txtCacheXcount_3.text()
                cache3.append(cacheXcount3)
            if(self.txtCacheYcount_3.text() != ""):
                cacheYcount3 = etree.Element("ycount")
                cacheYcount3.text = self.txtCacheYcount_3.text()
                cache3.append(cacheYcount3)
            mapcache.append(cache3)
            
        if(self.txtCacheName_4.text() != ""):
            cache4 = etree.Element("cache")
            cache4.set("name", self.txtCacheName_4.text())
            if(self.txtCacheType_4.text() != ""):
                cache4.set("type", self.txtCacheType_4.text())
            if(self.txtCacheLayout_4.text() != ""):
                cache4.set("layout", self.txtCacheLayout_4.text())
            if(self.txtCacheTemplate_4.text() != ""):
                cacheTemplate4 = etree.Element("template")
                cacheTemplate4.text = self.txtCacheTemplate_4.text()
                cache4.append(cacheTemplate4)
            if(self.txtCacheBase_4.text() != ""):
                cacheBase4 = etree.Element("base")
                cacheBase4.text = self.txtCacheTemplate_4.text()
                cache4.append(cacheBase4)
            if(self.txtCacheHost_4.text() != ""):
                cacheServer4 = etree.Element("server")
                cacheServerHost4 = etree.Element("host")
                cacheServerHost4.text = self.txtCacheHost_4.text()
                cacheServer4.append(cacheServerHost4)
                if(self.txtCachePort_4.text() != ""):
                    cacheServerPort4 = etree.Element("port")
                    cacheServerPort4.text = self.txtCachePort_4.text()
                    cacheServer4.append(cacheServerPort4)
                cache4.append(cacheServer4)
            if(self.txtCacheDbfile_4.text() != ""):
                cacheDbfile4 = etree.Element("dbfile")
                cacheDbfile4.text = self.txtCacheDbfile_4.text()
                cache4.append(cacheDbfile4)
            if(self.txtCacheXcount_4.text() != ""):
                cacheXcount4 = etree.Element("xcount")
                cacheXcount4.text = self.txtCacheXcount_4.text()
                cache4.append(cacheXcount4)
            if(self.txtCacheYcount_1.text() != ""):
                cacheYcount4 = etree.Element("ycount")
                cacheYcount4.text = self.txtCacheYcount_4.text()
                cache4.append(cacheYcount4)
            mapcache.append(cache4)
        
        if(self.txtSourceName_1.text() !=""):
            source1 = etree.Element("source")
            source1.set("name", self.txtSourceName_1.text())
            if(self.txtSourceType_1.text() != ""):
                source1.set("type", self.txtSourceType_1.text())
            if(self.txtSourceFormat_1.text() != ""):
                sourceGetmap1 = etree.Element("getmap")
                sourceGetmapParams1 = etree.Element("params")
                sourceGetmapParamsFormat1 = etree.Element("FORMAT")
                sourceGetmapParamsFormat1.text = self.txtSourceFormat_1.text()
                sourceGetmapParams1.append(sourceGetmapParamsFormat1)
                if(self.txtSourceLayer_1.text() != ""):
                    sourceGetmapParamsLayer1 = etree.Element("LAYERS")
                    sourceGetmapParamsLayer1.text = self.txtSourceLayer_1.text()
                    sourceGetmapParams1.append(sourceGetmapParamsLayer1)
                sourceGetmap1.append(sourceGetmapParams1)
                source1.append(sourceGetmap1)
            if(self.txtSourceUrl_1.text() != ""):
                sourceHttp1 = etree.Element("http")
                sourceHttpUrl1 = etree.Element("url")
                sourceHttpUrl1.text = self.txtSourceUrl_1.text()
                sourceHttp1.append(sourceHttpUrl1)
                if(self.txtSourceUserAgent_1.text() != ""):
                    sourceHttpHeaders1 = etree.Element("headers")
                    sourceHttpHeadersUserAgent1 = etree.Element("User-Agent")
                    sourceHttpHeadersUserAgent1.text = self.txtSourceUserAgent_1.text()
                    sourceHttpHeaders1.append(sourceHttpHeadersUserAgent1)
                    if(self.txtSourceReferer_1.text() != ""):
                        sourceHttpHeadersReferer1 = etree.Element("Referer")
                        sourceHttpHeadersReferer1.text = self.txtSourceReferer_1.text()
                        sourceHttpHeaders1.append(sourceHttpHeadersReferer1)
                    sourceHttp1.append(sourceHttpHeaders1)
                if(self.txtSourceConnectionTimeout_1.text() != ""):
                    sourceHttpConnectionTimeout1 = etree.Element("connection_timeout")
                    sourceHttpConnectionTimeout1.text = self.txtSourceConnectionTimeout_1.text()
                    sourceHttp1.append(sourceHttpConnectionTimeout1)
                source1.append(sourceHttp1)
            mapcache.append(source1)
            
        if(self.txtSourceName_2.text() !=""):
            source2 = etree.Element("source")
            source2.set("name", self.txtSourceName_2.text())
            if(self.txtSourceType_2.text() != ""):
                source2.set("type", self.txtSourceType_2.text())
            if(self.txtSourceFormat_2.text() != ""):
                sourceGetmap2 = etree.Element("getmap")
                sourceGetmapParams2 = etree.Element("params")
                sourceGetmapParamsFormat2 = etree.Element("FORMAT")
                sourceGetmapParamsFormat2.text = self.txtSourceFormat_2.text()
                sourceGetmapParams2.append(sourceGetmapParamsFormat2)
                if(self.txtSourceLayer_2.text() != ""):
                    sourceGetmapParamsLayer2 = etree.Element("LAYERS")
                    sourceGetmapParamsLayer2.text = self.txtSourceLayer_2.text()
                    sourceGetmapParams2.append(sourceGetmapParamsLayer2)
                sourceGetmap2.append(sourceGetmapParams2)
                source2.append(sourceGetmap2)
            if(self.txtSourceUrl_2.text() != ""):
                sourceHttp2 = etree.Element("http")
                sourceHttpUrl2 = etree.Element("url")
                sourceHttpUrl2.text = self.txtSourceUrl_2.text()
                sourceHttp2.append(sourceHttpUrl2)
                if(self.txtSourceUserAgent_2.text() != ""):
                    sourceHttpHeaders2 = etree.Element("headers")
                    sourceHttpHeadersUserAgent2 = etree.Element("User-Agent")
                    sourceHttpHeadersUserAgent2.text = self.txtSourceUserAgent_2.text()
                    sourceHttpHeaders2.append(sourceHttpHeadersUserAgent2)
                    if(self.txtSourceReferer_2.text() != ""):
                        sourceHttpHeadersReferer2 = etree.Element("Referer")
                        sourceHttpHeadersReferer2.text = self.txtSourceReferer_2.text()
                        sourceHttpHeaders2.append(sourceHttpHeadersReferer2)
                    sourceHttp2.append(sourceHttpHeaders2)
                if(self.txtSourceConnectionTimeout_2.text() != ""):
                    sourceHttpConnectionTimeout2 = etree.Element("connection_timeout")
                    sourceHttpConnectionTimeout2.text = self.txtSourceConnectionTimeout_2.text()
                    sourceHttp2.append(sourceHttpConnectionTimeout2)
                source2.append(sourceHttp2)
            mapcache.append(source2)
            
        if(self.txtSourceName_3.text() !=""):
            source3 = etree.Element("source")
            source3.set("name", self.txtSourceName_3.text())
            if(self.txtSourceType_3.text() != ""):
                source3.set("type", self.txtSourceType_3.text())
            if(self.txtSourceFormat_3.text() != ""):
                sourceGetmap3 = etree.Element("getmap")
                sourceGetmapParams3 = etree.Element("params")
                sourceGetmapParamsFormat3 = etree.Element("FORMAT")
                sourceGetmapParamsFormat3.text = self.txtSourceFormat_3.text()
                sourceGetmapParams3.append(sourceGetmapParamsFormat3)
                if(self.txtSourceLayer_3.text() != ""):
                    sourceGetmapParamsLayer3 = etree.Element("LAYERS")
                    sourceGetmapParamsLayer3.text = self.txtSourceLayer_3.text()
                    sourceGetmapParams3.append(sourceGetmapParamsLayer3)
                sourceGetmap3.append(sourceGetmapParams3)
                source3.append(sourceGetmap3)
            if(self.txtSourceUrl_3.text() != ""):
                sourceHttp3 = etree.Element("http")
                sourceHttpUrl3 = etree.Element("url")
                sourceHttpUrl3.text = self.txtSourceUrl_3.text()
                sourceHttp3.append(sourceHttpUrl3)
                if(self.txtSourceUserAgent_3.text() != ""):
                    sourceHttpHeaders3 = etree.Element("headers")
                    sourceHttpHeadersUserAgent3 = etree.Element("User-Agent")
                    sourceHttpHeadersUserAgent3.text = self.txtSourceUserAgent_3.text()
                    sourceHttpHeaders3.append(sourceHttpHeadersUserAgent3)
                    if(self.txtSourceReferer_3.text() != ""):
                        sourceHttpHeadersReferer3 = etree.Element("Referer")
                        sourceHttpHeadersReferer3.text = self.txtSourceReferer_3.text()
                        sourceHttpHeaders3.append(sourceHttpHeadersReferer3)
                    sourceHttp3.append(sourceHttpHeaders3)
                if(self.txtSourceConnectionTimeout_3.text() != ""):
                    sourceHttpConnectionTimeout3 = etree.Element("connection_timeout")
                    sourceHttpConnectionTimeout3.text = self.txtSourceConnectionTimeout_3.text()
                    sourceHttp3.append(sourceHttpConnectionTimeout3)
                source3.append(sourceHttp3)
            mapcache.append(source3)
            
        if(self.txtSourceName_4.text() !=""):
            source4 = etree.Element("source")
            source4.set("name", self.txtSourceName_4.text())
            if(self.txtSourceType_4.text() != ""):
                source4.set("type", self.txtSourceType_4.text())
            if(self.txtSourceFormat_4.text() != ""):
                sourceGetmap4 = etree.Element("getmap")
                sourceGetmapParams4 = etree.Element("params")
                sourceGetmapParamsFormat4 = etree.Element("FORMAT")
                sourceGetmapParamsFormat4.text = self.txtSourceFormat_4.text()
                sourceGetmapParams4.append(sourceGetmapParamsFormat4)
                if(self.txtSourceLayer_4.text() != ""):
                    sourceGetmapParamsLayer4 = etree.Element("LAYERS")
                    sourceGetmapParamsLayer4.text = self.txtSourceLayer_4.text()
                    sourceGetmapParams4.append(sourceGetmapParamsLayer4)
                sourceGetmap4.append(sourceGetmapParams4)
                source4.append(sourceGetmap4)
            if(self.txtSourceUrl_4.text() != ""):
                sourceHttp4 = etree.Element("http")
                sourceHttpUrl4 = etree.Element("url")
                sourceHttpUrl4.text = self.txtSourceUrl_4.text()
                sourceHttp4.append(sourceHttpUrl4)
                if(self.txtSourceUserAgent_4.text() != ""):
                    sourceHttpHeaders4 = etree.Element("headers")
                    sourceHttpHeadersUserAgent4 = etree.Element("User-Agent")
                    sourceHttpHeadersUserAgent4.text = self.txtSourceUserAgent_4.text()
                    sourceHttpHeaders4.append(sourceHttpHeadersUserAgent4)
                    if(self.txtSourceReferer_4.text() != ""):
                        sourceHttpHeadersReferer4 = etree.Element("Referer")
                        sourceHttpHeadersReferer4.text = self.txtSourceReferer_4.text()
                        sourceHttpHeaders4.append(sourceHttpHeadersReferer4)
                    sourceHttp4.append(sourceHttpHeaders4)
                if(self.txtSourceConnectionTimeout_4.text() != ""):
                    sourceHttpConnectionTimeout4 = etree.Element("connection_timeout")
                    sourceHttpConnectionTimeout4.text = self.txtSourceConnectionTimeout_4.text()
                    sourceHttp4.append(sourceHttpConnectionTimeout4)
                source4.append(sourceHttp4)
            mapcache.append(source4)
            
        if(self.txtTilesetName.text() != ""):
            tileset = etree.Element("tileset")
            tileset.set("name", self.txtTilesetName.text())
            if(self.txtTilesetSource.text() != ""):
                tilesetSource = etree.Element("source")
                tilesetSource.text = self.txtTilesetSource.text()
                tileset.append(tilesetSource)
            if(self.txtTilesetCache.text() != ""):
                tilesetCache = etree.Element("cache")
                tilesetCache.text = self.txtTilesetCache.text()
                tileset.append(tilesetCache)
            if(self.txtTilesetFormat.text() != ""):
                tilesetFormat = etree.Element("format")
                tilesetFormat.text = self.txtTilesetFormat.text()
                tileset.append(tilesetFormat)
            if(self.txtTilesetMetatile.text() != ""):
                tilesetMetatile = etree.Element("metatile")
                tilesetMetatile.text = self.txtTilesetMetatile.text()
                tileset.append(tilesetMetatile)
            if(self.txtTilesetMetabuffer.text() != ""):
                tilesetMetabuffer = etree.Element("metabuffer")
                tilesetMetabuffer.text = self.txtTilesetMetabuffer.text()
                tileset.append(tilesetMetabuffer)
            if(self.txtTilesetExpires.text() != ""):
                tilesetExpires = etree.Element("expires")
                tilesetExpires.text = self.txtTilesetExpires.text()
                tileset.append(tilesetExpires)
            if(self.txtTilesetAutoExpire.text() != ""):
                tilesetAutoExpire = etree.Element("auto_expire")
                tilesetAutoExpire.text = self.txtTilesetAutoExpire.text()
                tileset.append(tilesetAutoExpire)
            if(self.txtTilesetGridText_1.text() != ""):
                tilesetGrid1 = etree.Element("grid")
                tilesetGrid1.text = self.txtTilesetGridText_1.text()
                if(self.txtTilesetGridRestrictedExtent_1.text() != ""):
                    tilesetGrid1.set("restricted_extent", self.txtTilesetGridRestrictedExtent_1.text())
                if(self.txtTilesetGridMinzoom_1.text() != ""):
                    tilesetGrid1.set("minzoom", self.txtTilesetGridMinzoom_1.text())
                if(self.txtTilesetGridMaxzoom_1.text() != ""):
                    tilesetGrid1.set("maxzoom", self.txtTilesetGridMaxzoom_1.text())
                tileset.append(tilesetGrid1)
            if(self.txtTilesetGridText_2.text() != ""):
                tilesetGrid2 = etree.Element("grid")
                tilesetGrid2.text = self.txtTilesetGridText_2.text()
                if(self.txtTilesetGridRestrictedExtent_2.text() != ""):
                    tilesetGrid2.set("restricted_extent", self.txtTilesetGridRestrictedExtent_2.text())
                if(self.txtTilesetGridMinzoom_2.text() != ""):
                    tilesetGrid2.set("minzoom", self.txtTilesetGridMinzoom_2.text())
                if(self.txtTilesetGridMaxzoom_2.text() != ""):
                    tilesetGrid2.set("maxzoom", self.txtTilesetGridMaxzoom_2.text())
                tileset.append(tilesetGrid2)
            if(self.txtTilesetMetadataTitle.text() != ""):
                tilesetMetadata = etree.Element("metadata")
                tilesetMetadataTitle = etree.Element("title")
                tilesetMetadataTitle.text = self.txtTilesetMetadataTitle.text()
                tilesetMetadata.append(tilesetMetadataTitle)
                if(self.txtTilesetMetadataAbstract.text() != ""):
                    tilesetMetadataAbstract = etree.Element("abstract")
                    tilesetMetadataAbstract.text = self.txtTilesetMetadataAbstract.text()
                    tilesetMetadata.append(tilesetMetadataAbstract)
                tileset.append(tilesetMetadata)
            if(self.txtTilesetDimensionText_1.text() != "" or self.txtTilesetDimensionText_1.text() != "" or self.txtTilesetDimensionText_3.text() != ""):
                tilesetDimensions = etree.Element("dimensions")
                if(self.txtTilesetDimensionText_1.text() != ""):
                    tilesetDimension1 = etree.Element("dimension")
                    tilesetDimension1.text = self.txtTilesetDimensionText_1.text()
                    if(self.txtTilesetDimensionType_1.text() != ""):
                        tilesetDimension1.set("type", self.txtTilesetDimensionType_1.text())
                    if(self.txtTilesetDimensionName_1.text() != ""):
                        tilesetDimension1.set("name", self.txtTilesetDimensionName_1.text())
                    if(self.txtTilesetDimensionDefault_1.text() != ""):
                        tilesetDimension1.set("default", self.txtTilesetDimensionDefault_1.text())
                    tilesetDimensions.append(tilesetDimension1)
                if(self.txtTilesetDimensionText_2.text() != ""):
                    tilesetDimension2 = etree.Element("dimension")
                    tilesetDimension2.text = self.txtTilesetDimensionText_2.text()
                    if(self.txtTilesetDimensionType_2.text() != ""):
                        tilesetDimension2.set("type", self.txtTilesetDimensionType_2.text())
                    if(self.txtTilesetDimensionName_2.text() != ""):
                        tilesetDimension2.set("name", self.txtTilesetDimensionName_2.text())
                    if(self.txtTilesetDimensionDefault_2.text() != ""):
                        tilesetDimension2.set("default", self.txtTilesetDimensionDefault_2.text())
                    tilesetDimensions.append(tilesetDimension2)
                if(self.txtTilesetDimensionText_3.text() != ""):
                    tilesetDimension3 = etree.Element("dimension")
                    tilesetDimension3.text = self.txtTilesetDimensionText_3.text()
                    if(self.txtTilesetDimensionType_3.text() != ""):
                        tilesetDimension3.set("type", self.txtTilesetDimensionType_3.text())
                    if(self.txtTilesetDimensionName_3.text() != ""):
                        tilesetDimension3.set("name", self.txtTilesetDimensionName_3.text())
                    if(self.txtTilesetDimensionDefault_1.text() != ""):
                        tilesetDimension3.set("default", self.txtTilesetDimensionDefault_3.text())
                    tilesetDimensions.append(tilesetDimension3)
                tileset.append(tilesetDimensions)
            mapcache.append(tileset)    
            
                
        if(self.txtServiceType_1.text() != ""):
            service1 = etree.Element("service")
            service1.set("type", self.txtServiceType_1.text())
            if(self.txtServiceEnabled_1.text() != ""):
                service1.set("enabled", self.txtServiceEnabled_1.text())
            if(self.txtServiceFullWms_1.text() != ""):
                serviceFullWms1 = etree.Element("full_wms")
                serviceFullWms1.text = self.txtServiceFullWms_1.text()
                service1.append(serviceFullWms1)
            if(self.txtServiceResampleMode_1.text() != ""):
                serviceResampleMode1 = etree.Element("resample_mode")
                serviceResampleMode1.text = self.txtServiceResampleMode_1.text()
                service1.append(serviceResampleMode1)
            if(self.txtServiceFormat_1.text() != ""):
                serviceFormat1 = etree.Element("format")
                serviceFormat1.text = self.txtServiceFormat_1.text()
                service1.append(serviceFormat1)
            if(self.txtServiceMaxsize_1.text() != ""):
                serviceMaxsize1 = etree.Element("maxsize")
                serviceMaxsize1.text = self.txtServiceMaxsize_1.text()
                service1.append(serviceMaxsize1)
            mapcache.append(service1)  
        if(self.txtServiceType_2.text() != ""):
            service2 = etree.Element("service")
            service2.set("type", self.txtServiceType_2.text())
            if(self.txtServiceEnabled_2.text() != ""):
                service2.set("enabled", self.txtServiceEnabled_2.text())
            mapcache.append(service2)
        if(self.txtServiceType_3.text() != ""):
            service3 = etree.Element("service")
            service3.set("type", self.txtServiceType_3.text())
            if(self.txtServiceEnabled_3.text() != ""):
                service3.set("enabled", self.txtServiceEnabled_3.text())
            mapcache.append(service3)
        if(self.txtServiceType_4.text() != ""):
            service4 = etree.Element("service")
            service4.set("type", self.txtServiceType_4.text())
            if(self.txtServiceEnabled_4.text() != ""):
                service4.set("enabled", self.txtServiceEnabled_4.text())
            mapcache.append(service4)
        if(self.txtServiceType_5.text() != ""):
            service5 = etree.Element("service")
            service5.set("type", self.txtServiceType_5.text())
            if(self.txtServiceEnabled_5.text() != ""):
                service5.set("enabled", self.txtServiceEnabled_5.text())
            mapcache.append(service5)
        if(self.txtServiceType_6.text() != ""):
            service6 = etree.Element("service")
            service6.set("type", self.txtServiceType_6.text())
            if(self.txtServiceEnabled_6.text() != ""):
                service6.set("enabled", self.txtServiceEnabled_6.text())
            mapcache.append(service6)
        if(self.txtServiceType_7.text() != ""):
            service7 = etree.Element("service")
            service7.set("type", self.txtServiceType_7.text())
            if(self.txtServiceEnabled_7.text() != ""):
                service7.set("enabled", self.txtServiceEnabled_7.text())
            mapcache.append(service7)
        
        if(self.txtGridName.text() != ""):
            grid = etree.Element("grid")
            grid.set("name", self.txtGridName.text())
            if(self.txtGridExtent.text() != ""):
                gridExtent = etree.Element("extent")
                gridExtent.text = self.txtGridExtent.text()
                grid.append(gridExtent)
            if(self.txtGridSize.text() != ""):
                gridSize = etree.Element("size")
                gridSize.text = self.txtGridSize.text()
                grid.append(gridSize)
            if(self.txtGridUnits.text() != ""):
                gridUnits = etree.Element("units")
                gridUnits.text = self.txtGridUnits.text()
                grid.append(gridUnits)
            if(self.txtGridSrs.text() != ""):
                gridSrs = etree.Element("srs")
                gridSrs.text = self.txtGridSrs.text()
                grid.append(gridSrs)
            if(self.txtGridResolution.text() != ""):
                gridResolution = etree.Element("resolution")
                gridResolution.text = self.txtGridResolution.text()
                grid.append(gridResolution)
            if(self.txtGridTitle.text() != ""):
                gridMetadata = etree.Element("metadata")
                gridMetadataTitle = etree.Element("title")
                gridMetadataTitle.text = self.txtGridTitle.text()
                gridMetadata.append(gridMetadataTitle)
                if(self.txtGridWellKnownScaleSet.text() != ""):
                    gridMetadataWellKnownScaleSet = etree.Element("WellKnownScaleSet")
                    gridMetadataWellKnownScaleSet.text = self.txtGridWellKnownScaleSet.text()
                    gridMetadata.append(gridMetadataWellKnownScaleSet)
                grid.append(gridMetadata)
            mapcache.append(grid)
            
        if(self.txtOtherDedaultFormat.text() != ""):
            otherDedaultFormat = etree.Element("default_format")
            otherDedaultFormat.text = self.txtOtherDedaultFormat.text()
            mapcache.append(otherDedaultFormat)
            
        if(self.txtOtherErrors.texte() != ""):
            otherErrors = etree.Element("errors")
            otherErrors.text = self.txtOtherErrors.texte()
            mapcache.append(otherErrors)
            
        if(self.txtOtherLockDir.text() != ""):
            otherLockDir = etree.Element("lock_dir")
            otherLockDir.text = self.txtOtherLockDir.text()
            mapcache.append(otherLockDir)
            
        if(self.txtOtherLogLevel.text() != ""):
            otherLogLevel = etree.Element("log_level")
            otherLogLevel.text = self.txtOtherLogLevel.text()
            mapcache.append(otherLogLevel)
            
        if(self.txtOtherAutoLoad.text() != ""):
            otherAutoLoad = etree.Element("auto_reload")
            otherAutoLoad.text = self.txtOtherAutoLoad.text()
            mapcache.append(otherAutoLoad)
                

        s = etree.tostring(mapcache)
        file_ = open(self.txtXmlConfigFilePath.text(), "w")
        file_.write(s)
        file_.close()