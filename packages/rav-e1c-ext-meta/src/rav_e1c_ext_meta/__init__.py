from contextlib import suppress
from pathlib import PurePosixPath
from typing import Protocol, Final, Literal, TypedDict, get_args, Type

from pydantic import BaseModel, Discriminator, ValidationError, RootModel, field_validator

__all__ = [r'BaseTable', r'ProtocolTable', r'discriminator', r'MetaData', r'parse_meta']


class ProtocolTable(Protocol):
    ИмяТаблицыХранения: str


# noinspection PyDataclass
class BaseTable(BaseModel, frozen=True):
    Назначение: Literal[r'Основная']
    Метаданные: PurePosixPath
    ИмяТаблицы: str
    ИмяТаблицыХранения: str

    # noinspection PyPep8Naming
    @field_validator(r'Метаданные', mode='before')
    def val_before_Метаданные(cls, v: str)->str:
        return v.replace(r'.',r'/')

def discriminator(v: dict) -> str:
    return v['Метаданные']


discriminator: Final[Discriminator] = Discriminator(discriminator)


class MetaData(TypedDict):
    Строки: list



def parse_meta[T=RootModel](meta: MetaData, *, descriptor: Type[T]) -> dict[str, T]:
    tables:list[T] = []
    for t in meta[r'Строки']:
        with suppress(ValidationError):
            tables.append(descriptor.model_validate(t))
    return {v.root.ИмяТаблицы:v.root for v in iter(tables)}
