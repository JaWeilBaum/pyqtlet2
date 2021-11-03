class Parser:
    @staticmethod
    def dict_for_js(object_to_parse: dict) -> dict:
        return_dict = {}
        for key, value in object_to_parse.items():
            if isinstance(value, bool):
                return_dict[key] = str(value).lower()
                continue

            return_dict[key] = value
        return return_dict

    @staticmethod
    def js_for_dict(object_to_parse: dict) -> dict:
        return_dict = {}
        for key, value in object_to_parse.items():
            if isinstance(value, str):
                value: str
                if value.lower() in ["true", "false"]:
                    return_dict[key] = True if value.lower() == "true" else False
                    continue

            return_dict[key] = value
        return return_dict
