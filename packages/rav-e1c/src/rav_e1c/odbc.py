from typing_extensions import Literal


# noinspection SpellCheckingInspection
def connection_string(
        version: Literal[17, 18] = 18, *,
        hostname: str, portnumb: int,
        basename: str, username: str, password: str,
        clntname: str, appname: str = r'python'):
    """
    Создает строку подключения ODBC

    :param version: версия драйвера ODBC
    :param hostname: SERVER: fqdn/ip
    :param portnumb: PASSWORD: номер порта
    :param basename: DATABASE
    :param username: UID
    :param password: PASSWORD
    :param clntname: WSID
    :param appname: APP
    :return:
    """

    return r';'.join([
        f'DRIVER = ODBC Driver {version} for SQL Server',
        f'SERVER = {hostname}, {portnumb}'
        f'DATABASE = {basename}',
        f'UID = {username}',
        f'PASSWORD = {password}',
        f'WSID = {clntname}',
        f'APP = {appname}',
        'Trusted_Connection = No',
        'TransparentNetworkIPResolution = Disabled',
        'Regional = Yes',
        'QueryLog_On = No',
        'TrustServerCertificate = Yes',
        'LANGUAGE = русский'])
