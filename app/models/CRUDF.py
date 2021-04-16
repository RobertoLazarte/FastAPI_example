from sqlalchemy.orm import Session
from app.models.models import Registro

def store_registro(db: Session, info_dict : dict):
    try:
        db_image = Registro(nome = info_dict['nome'],
                            horario_consulta = info_dict['horario_consulta'])
        db.add(db_image)
        db.commit()
        return True
    except Exception:
        return False


        



