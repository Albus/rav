```python
from rav_e1c_ext_meta import discriminator, parse_meta, MetaData, table_model

async def meta(src: AsyncClient) -> MetaData:
    return orjson.loads(await(await src.get('/meta')).aread())

class Table(RootModel[Annotated[Union[
    table_model(r'ДокументТранзакцияВыплаты', module=r'Метаданные', meta=r'Документ.ТранзакцияВыплаты'),
    table_model(r'ДокументТранзакцияВыплаты', module=r'Метаданные', meta=r'Документ.ТранзакцияВыплаты')
], discriminator]]): ...

tables = parse_meta(runnify(meta)(), descriptor=Table)
```

```python
{'Документ.ТранзакцияВыплаты': ДокументТранзакцияВыплаты(
    Назначение='Основная', Метаданные=PurePosixPath('Документ/ТранзакцияВыплаты'),
    ИмяТаблицы='Документ.ТранзакцияВыплаты', ИмяТаблицыХранения='_Document94'),
 'Документ.ТранзакцияВыплатыСБП': ДокументТранзакцияВыплатыСБП(
     Назначение='Основная', Метаданные=PurePosixPath('Документ/ТранзакцияВыплатыСБП'),
     ИмяТаблицы='Документ.ТранзакцияВыплатыСБП', ИмяТаблицыХранения='_Document5637')}
```