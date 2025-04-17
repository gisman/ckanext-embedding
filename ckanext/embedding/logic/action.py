import ckan.plugins.toolkit as tk
import ckanext.embedding.logic.schema as schema


@tk.side_effect_free
def embedding_get_sum(context, data_dict):
    tk.check_access(
        "embedding_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.embedding_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'embedding_get_sum': embedding_get_sum,
    }
