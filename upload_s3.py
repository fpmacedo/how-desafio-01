#%%
import s3_utils
# %%

#%%
s3_utils.create_bucket('desafio-01', 'us-east-1')
# %%
s3_utils.list_bucket()
# %%
s3_utils.upload_file()