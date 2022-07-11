from usuario.models import UserExtraInfo

def total_carrito(request):
    total = 0
    desc = 0.95

    try:
        InformacionUsuario = UserExtraInfo.objects.get(id_id=request.user.id)

        if InformacionUsuario.is_suscribe:
            if "carrito" in request.session.keys():
                for key, value in request.session["carrito"].items():
                    total += int(value["acumulado"])
            return {"total_carrito": round(total*desc)}
        else:
            if "carrito" in request.session.keys():
                for key, value in request.session["carrito"].items():
                    total += int(value["acumulado"])
            return {"total_carrito": total}
    except UserExtraInfo.DoesNotExist:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
        return {"total_carrito": total}