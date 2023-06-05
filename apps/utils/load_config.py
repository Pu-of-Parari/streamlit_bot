import os
import configparser


def load_openai_key(conf_path: str):
    config = configparser.ConfigParser()
    config.read(conf_path)
    key = config["OPENAI"]["API_KEY"]
    os.environ["OPENAI_API_KEY"] = key

    return True