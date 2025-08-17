from typing import Final, Literal


from socket import gethostname

__all__ = [r'HOSTNAME', r'connection_string']

HOSTNAME: Final[str] = gethostname()

# noinspection SpellCheckingInspection
def connection_string(
        version: Literal[17, 18] = 18, *,
        hostname: str=r'localhost', portnumb: int= 1433,
        basename: str, username: str = r'sa', password: str,
        clntname: str = HOSTNAME, appname: str = r'python'):
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

    return r' ; '.join([
        r'DRIVER = {ODBC Driver ' f'{version}' r' for SQL Server}',
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
