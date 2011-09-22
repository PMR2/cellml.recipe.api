from cellml_api import CellML_APISPEC

def loadModel(url):
    cellml_bootstrap = CellML_APISPEC.CellMLBootstrap()
    model_loader = cellml_bootstrap.getmodelLoader()
    return model_loader.loadFromURL(url)

if __name__ == '__main__':
    url = 'http://models.cellml.org/e/1/beeler_reuter_1977.cellml'
    model = loadModel(url)
    print 'loaded model:', url
    print 'model cmetaid is:', model.getcmetaId()
