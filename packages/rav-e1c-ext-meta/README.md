```python
from rav_e1c_ext_meta import BaseTable, discriminator, parse_meta, MetaData

...

async def meta() -> MetaData:
    global processing
    return orjson.loads(await(await processing.get('/meta')).aread())

class Table(RootModel[Annotated[Union[
    Annotated[create_model(
        r'ДокументТранзакцияВыплаты',
        __module__=r'Метаданные', __base__=BaseTable
    ), Tag(r'Документ.ТранзакцияВыплаты')],
    Annotated[create_model(
        r'ДокументТранзакцияВыплатыСБП',
        __module__=r'Метаданные', __base__=BaseTable
    ), Tag(r'Документ.ТранзакцияВыплатыСБП')]
], discriminator]]): ...
ic(parse_meta(runnify(meta)(), descriptor=Table))
```

```python
{'Документ.ТранзакцияВыплаты': ДокументТранзакцияВыплаты(
   Назначение='Основная', 
   Метаданные='Документ.ТранзакцияВыплаты', 
   ИмяТаблицы='Документ.ТранзакцияВыплаты', 
   ИмяТаблицыХранения='_Document94'),
 'Документ.ТранзакцияВыплатыСБП': ДокументТранзакцияВыплатыСБП(
   Назначение='Основная', 
   Метаданные='Документ.ТранзакцияВыплатыСБП', 
   ИмяТаблицы='Документ.ТранзакцияВыплатыСБП', 
   ИмяТаблицыХранения='_Document5637')}
```