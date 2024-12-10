from typing import Optional, List
from .models.filter import FilterSchema
from .models.updateTransporte import UpdateTransporte
from src.database import get_database
from bson import ObjectId



async def getTrasportes(filter: Optional[FilterSchema] = None):
    query_filter = {key: value for key, value in filter.model_dump().items() if value is not None} if filter else {}
    transportes_cursor = get_database()["transporte"].find(query_filter)
    transportes = await transportes_cursor.to_list(length=None)  

    transportes = [
        {**doc, "_id": str(doc["_id"])} for doc in transportes
    ]
    return {"facturas": transportes}

async def updateTransporte(updateTransporte: List[UpdateTransporte]):
    update_results = {"updated": 0, "not_updated": 0, "errors": []}
    for update in updateTransporte:
        update_dict = {key: value for key, value in update.model_dump().items() if value is not None}
        transporte_id = update_dict.pop("id")
        try:
            result = await get_database()["transporte"].update_one({"_id": ObjectId(transporte_id)}, {"$set": update_dict})
            if result.modified_count:
                update_results["updated"] += 1
            else:
                update_results["not_updated"] += 1
                update_results["errors"].append({"id": transporte_id, "error": "Document not updated"})
        except Exception as e:
            update_results["not_updated"] += 1
            update_results["errors"].append({"id": transporte_id, "error": str(e)})
    return update_results