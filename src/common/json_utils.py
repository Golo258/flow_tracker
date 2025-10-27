
import json


class JsonUtil:

    @staticmethod
    def convert_string_to_json(string: str):
        """
            Converts a given @string to a JSON object

            :param string: string to convert
            :return: JSON object
        """
        try:
            return json.loads(string)
        except json.JSONDecodeError as e:
            print(e)
            raise e