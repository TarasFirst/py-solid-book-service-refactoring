import json
import xml.etree.ElementTree as Et


def serializer_object_to_json(obj_to_json: object) -> json:
    return json.dumps(obj_to_json, default=lambda o: o.__dict__)


def serializer_obj_to_xml(obj_to_xml: object) -> str:
    name_obj = obj_to_xml.__class__.__name__.lower()
    root = Et.Element(name_obj)
    for key, value in obj_to_xml.__dict__.items():
        child = Et.SubElement(root, key)
        child.text = str(value)
    return Et.tostring(root, encoding="unicode")


def choose_type_serializer(
        object_to_serialize: object,
        serializer_type: str
) -> str | dict:
    if serializer_type == "json":
        return serializer_object_to_json(object_to_serialize)
    elif serializer_type == "xml":
        return serializer_obj_to_xml(object_to_serialize)
    else:
        raise ValueError(f"Unknown serialize type: {serializer_type}")
