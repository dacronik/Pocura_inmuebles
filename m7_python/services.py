from m7_python.models import Inmuebles

def get_all_inmuebles():
    Inm = Inmuebles.objects.all()
    return Inm

def insertar_inmueble(data):
    id_user = data[0]
    id_tipo_inmueble = data[1]
    id_comuna = data[2]
    id_region = data[3]
    nombre_inmueble = data[4]
    descripcion = data[5]
    m2_construido = data[6]
    m2_terreno = data[7]
    numero_est = data[8]
    numero_banos = data[9]
    direccion = data[10]
    precio = data[11]

    inm = Inmuebles(
        id_user = id_user,
        id_tipo_inmueble = id_tipo_inmueble,
        id_comuna = id_comuna,
        id_region = id_region,
        nombre_inmueble = nombre_inmueble,
        descripcion = descripcion,
        m2_construido = m2_construido,
        m2_terreno = m2_terreno,
        numero_est = numero_est,
        numero_banos = numero_banos,
        direccion = direccion,
        precio = precio
    )
    inm.save()

def actualizar_descrp_inmueble(id_inmueble,new_descrip):
    Inmuebles.objects.filter(pk=id_inmueble).update(descripcion=new_descrip)

def eliminar_inmueble(id_inmueble):
    Inmuebles.objects.get(id=id_inmueble).delete()