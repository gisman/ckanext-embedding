import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def embedding_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "embedding_get_sum": embedding_get_sum,
    }
