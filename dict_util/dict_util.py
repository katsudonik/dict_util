import numpy as np
import pandas as pd


class DictUtil:
    ks = []
    ds = []
    
    def to_kv(self, src):
        for k, v in src.items():
            self.ks.append(k)
            if type(v) == dict:
                self.to_kv(v)
            else:            
                self.ds.append(np.array([".".join(self.ks), v]))
            self.ks.pop(-1)

    # _dict: nested dict
    def dict_to_df(self, _dict):
            self.ks = []
            self.ds = []
            self.to_kv(_dict)
            return pd.DataFrame(np.array(self.ds), columns=["key", "val"])      
        
    def separate_head(self, df):
        tmp = df['key'].str.extract('(.+?)\.(.+)', expand=True)
        df['t_key'] = tmp[0]
        df['key'] = tmp[1]
        return df

    # df['key']: nested keys joined by dot.
    # df['val']: dict value.
    def df_to_dict(self, df):
        t = {}
        # set t_key
        other_df = df[ ~(df['key'].str.contains('.', regex=False)) ]
        other_df['t_key'] = other_df['key']
        other_df['key'] = np.nan
        target_df = df[ df['key'].str.contains('.', regex=False) ]
        target_df = self.separate_head(target_df)
        merge_df = pd.concat([other_df, target_df])

        head_keys = list(set(merge_df['t_key']))
        for k in head_keys:
            r = merge_df[merge_df['t_key'] == k]
            if len( r[ ~(r['key'].isnull()) ] ) > 0:
                r = self.df_to_dict(r)
            else:
                r = r['val'].iloc[0]
            t[k] = r
        return t
    
    def diff_df(self, left_df, right_df):
        left_df = left_df.rename(columns={'val': 'val_left'}).copy()
        right_df = right_df.rename(columns={'val': 'val_right'}).copy()

        key_df = pd.DataFrame((list(set( list(left_df['key']) + list(right_df['key']) ))), columns=['key'])
        m_df = pd.merge(key_df, left_df, on='key', how='left')
        m_df = pd.merge(m_df, right_df, on='key', how='left')
        diff_df = m_df[m_df['val_left'] != m_df['val_right']]
        diff_df = diff_df[ ~(diff_df['val_left'].isnull() & diff_df['val_right'].isnull()) ]
        return diff_df
    
    def diff_by_df(self, left_dict, right_dict):
        return self.diff_df(
            dict_util.dict_to_df(left_dict), 
            dict_util.dict_to_df(right_dict))


dict_util = DictUtil()
