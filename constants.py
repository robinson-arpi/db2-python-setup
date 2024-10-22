import configparser

cfg = configparser.ConfigParser()
cfg.read("database_config.txt", encoding="ansi")

# DATABASE
DRIVER = cfg["DATABASE"]["DRIVER"]
HOST = cfg["DATABASE"]["HOST"]
DATABASE = cfg["DATABASE"]["DATABASE"]
UID_DB = cfg["CREDENTIALS"]["UID"]
PWD_DB = cfg["CREDENTIALS"]["PWD"]