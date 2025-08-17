from contextlib import suppress
from pathlib import PurePosixPath
from typing import Protocol, Final, Literal, TypedDict, Type, Annotated

from pydantic import BaseModel, Discriminator, ValidationError, RootModel, field_validator, Tag, create_model

__all__ = [r'BaseTable', r'ProtocolMeta', r'discriminator', r'MetaData', r'parse_meta', r'table_model']


class ProtocolMeta(Protocol):

    @property
    def literal(self) -> str: ...


class BaseMeta(BaseModel):
    Метаданные: PurePosixPath | None

    # noinspection PyPep8Naming
    @field_validator(r'Метаданные', mode='before')
    def val_before_Метаданные(cls, v: str) -> str | None:
        return v.replace(r'.', r'/') if v else None


class BaseField(BaseMeta):
    ИмяПоля: str
    ИмяПоляХранения: str

    @property
    def literal(self) -> str:
        return self.ИмяПоляХранения


class BaseTable(BaseMeta):
    Назначение: str
    ИмяТаблицы: str
    ИмяТаблицыХранения: str

    Поля: dict[str, BaseField]  # = Field(validation_alias=AliasPath())

    @property
    def literal(self) -> str:
        return self.ИмяТаблицыХранения

    # noinspection PyPep8Naming
    @field_validator(r'Поля', mode='before')
    def val_before_Метаданные(cls, v: dict) -> dict[str, dict]:
        return {v[r'ИмяПоля']: v for v in iter(v[r'Строки'])}


def discriminator(v: dict) -> str:
    return v['Метаданные']


discriminator: Final[Discriminator] = Discriminator(discriminator)


class MetaData(TypedDict):
    Строки: list


# noinspection PyRedeclaration
def table_model(name: str, *, module: str, meta: str) -> Type[BaseTable]:
    return Annotated[create_model(name, __module__=module, __base__=BaseTable), Tag(meta)]


def parse_meta[T=RootModel](meta: MetaData, *, descriptor: Type[T]) -> dict[str, ProtocolMeta]:
    tables: list[T] = []
    for t in meta[r'Строки']:
        with suppress(ValidationError):
            tables.append(descriptor.model_validate(t))
    return {v.root.ИмяТаблицы: v.root for v in iter(tables)}
