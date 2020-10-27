from typing import Any, Dict
from uuid import UUID


def get_edgeql_type(value: Any) -> str:
    if type(value) == bool:
        return "<bool>"
    elif type(value) == str:
        return "<str>"
    elif type(value) == int:
        return "<int64>"
    elif type(value) == UUID:
        return "<uuid>"
    else:
        raise ValueError("Type not found.")


def turn_dict_to_edgeql_expressions(data: Dict[str, Any]) -> str:
    shape_list = [f"{k} := {get_edgeql_type(v)}${k}" for k, v in data.items()]
    return ", ".join(shape_list)
