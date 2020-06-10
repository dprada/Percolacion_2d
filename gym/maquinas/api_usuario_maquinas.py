def que_maquinas_estan_libres():

    from . import listado

    listado_maquinas_libres = []

    if listado.bici1 is True:
        listado_maquinas_libres.append('bici1')

    if listado.bici2 is True:
        listado_maquinas_libres.append('bici2')

    if listado.remo1 is True:
        listado_maquinas_libres.append('remo1')

    if listado.cintacorrer1 is True:
        listado_maquinas_libres.append('cintacorrer1')

    return listado_maquinas_libres

