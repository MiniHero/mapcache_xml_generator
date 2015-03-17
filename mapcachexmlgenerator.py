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
                cacheServerHost1.text = elf.txtCacheHost_1.text()
                cacheServer1.append(cacheServer1)
                if(self.txtCachePort_1.text() != ""):
                    cacheServerPort1 = etree.Element("port")
                    cacheServerPort1.text = self.txtCachePort_1.text()
                cache1.append(cacheServer1)
            if(self.txtCacheDbfile_1.text() != ""):
                cacheDbfile1 = etree.element("dbfile")
                cacheDbfile1.text = self.txtCacheDbfile_1.text()
                cache1.append(cacheDbfile1)
            mapcache.append(cache1)
        
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
                    sourceGetmapParams1.append(sourceGetmapParamsLayer1)
                sourceGetmap1.append(sourceGetmapParams1)
                source1.append(sourceGetmap1)
            if(self.txtSourceUrl_1.text() != ""):
                sourceHttp1 = etree.Element("http")
                sourceHttpUrl1 = stree.Element("url")
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
            mapcache.append(service2)
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
            
                

        s = etree.tostring(mapcache)
        file_ = open(self.txtXmlConfigFilePath.text(), "w")
        file_.write(s)
        file_.close()