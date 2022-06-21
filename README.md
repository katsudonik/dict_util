# dict_util
python dict utility

## install

```
pip install dict_util
```

## usage

### initialize

```
from dict_util.dict_util import DictUtil
dict_util = DictUtil()
```

### functions

#### dict_to_df

convert dict to df(pandas dataframe)

```
sample_dict = json.load(open( f'sample.json' , "r"))
sample_df = dict_util.dict_to_df(sample_dict)
```

#### diff_df

compare two df(result of `dict_to_df`) to each other

#### diff_by_df

convert two dict to df & compare them to each other

#### update_dict_df_val

replace val of target_dict_df with val of new_dict_df

```
update_dict_df_val(self, target_dict_df, new_dict_df)
```

#### df_to_dict

convert result of `dict_to_df` to dict

```
sample_dict = dict_util.df_to_dict(sample_df)
s = json.dumps(sample_dict, ensure_ascii=False)
with open(f'{REPOSITORIES_PARENT_PATH}{env}/src/locales/{lang}_before.json', mode='w') as f:
    f.write(s)
```

