import configparser
import os

cfg = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'database_config.ini')

cfg.read(config_path, encoding="ansi")

# DATABASE
DRIVER = cfg["DATABASE"]["DRIVER"]
HOST = cfg["DATABASE"]["HOST"]
DATABASE = cfg["DATABASE"]["DATABASE"]
UID_DB = cfg["CREDENTIALS"]["UID"]
PWD_DB = cfg["CREDENTIALS"]["PWD"]