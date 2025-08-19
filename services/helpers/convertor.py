import bson


def convert_bson_types(obj):
    if isinstance(obj, dict):
        return {k: convert_bson_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_bson_types(i) for i in obj]
    elif isinstance(obj, bson.objectid.ObjectId):
        return str(obj)
    else:
        return obj