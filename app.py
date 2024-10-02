{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c08d4f2b-546c-41f8-84e6-eb70f57ebc8f",
   "metadata": {},
   "outputs": [
    {
     "ename": "InternalHashError",
     "evalue": "module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_model()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_model at 0x00000143ACC38900>\n```\n\nPlease see the `hash_funcs` [documentation](https://docs.streamlit.io/library/advanced-features/caching#the-hash_funcs-parameter)\nfor more details.\n            ",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:361\u001b[0m, in \u001b[0;36m_CodeHasher.to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    359\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m    360\u001b[0m     \u001b[38;5;66;03m# Hash the input\u001b[39;00m\n\u001b[1;32m--> 361\u001b[0m     b \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m:\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m (tname, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_to_bytes(obj, context))\n\u001b[0;32m    363\u001b[0m     \u001b[38;5;66;03m# Hmmm... It's possible that the size calculation is wrong. When we\u001b[39;00m\n\u001b[0;32m    364\u001b[0m     \u001b[38;5;66;03m# call to_bytes inside _to_bytes things get double-counted.\u001b[39;00m\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:622\u001b[0m, in \u001b[0;36m_CodeHasher._to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    621\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m code \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m--> 622\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_file_should_be_hashed(code\u001b[38;5;241m.\u001b[39mco_filename):\n\u001b[0;32m    623\u001b[0m     context \u001b[38;5;241m=\u001b[39m _get_context(obj)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:403\u001b[0m, in \u001b[0;36m_CodeHasher._file_should_be_hashed\u001b[1;34m(self, filename)\u001b[0m\n\u001b[0;32m    401\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m    402\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_is_in_folder_glob(\n\u001b[1;32m--> 403\u001b[0m     filepath, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_get_main_script_directory()\n\u001b[0;32m    404\u001b[0m ) \u001b[38;5;129;01mor\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_in_pythonpath(filepath)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:709\u001b[0m, in \u001b[0;36m_CodeHasher._get_main_script_directory\u001b[1;34m()\u001b[0m\n\u001b[0;32m    707\u001b[0m \u001b[38;5;66;03m# This works because we set __main__.__file__ to the\u001b[39;00m\n\u001b[0;32m    708\u001b[0m \u001b[38;5;66;03m# script path in ScriptRunner.\u001b[39;00m\n\u001b[1;32m--> 709\u001b[0m abs_main_path \u001b[38;5;241m=\u001b[39m pathlib\u001b[38;5;241m.\u001b[39mPath(__main__\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__file__\u001b[39m)\u001b[38;5;241m.\u001b[39mresolve()\n\u001b[0;32m    710\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(abs_main_path\u001b[38;5;241m.\u001b[39mparent)\n",
      "\u001b[1;31mAttributeError\u001b[0m: module '__main__' has no attribute '__file__'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mInternalHashError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 36\u001b[0m\n\u001b[0;32m     33\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(df)\n\u001b[0;32m     35\u001b[0m \u001b[38;5;66;03m# 加载模型并进行预测\u001b[39;00m\n\u001b[1;32m---> 36\u001b[0m model \u001b[38;5;241m=\u001b[39m load_model()\n\u001b[0;32m     37\u001b[0m prediction \u001b[38;5;241m=\u001b[39m model\u001b[38;5;241m.\u001b[39mpredict(df)\n\u001b[0;32m     39\u001b[0m \u001b[38;5;66;03m# 显示预测结果\u001b[39;00m\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\caching.py:716\u001b[0m, in \u001b[0;36mcache.<locals>.wrapped_func\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    714\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m show_spinner:\n\u001b[0;32m    715\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m spinner(message, cache\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m):\n\u001b[1;32m--> 716\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m get_or_create_cached_value()\n\u001b[0;32m    717\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    718\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m get_or_create_cached_value()\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\caching.py:638\u001b[0m, in \u001b[0;36mcache.<locals>.wrapped_func.<locals>.get_or_create_cached_value\u001b[1;34m()\u001b[0m\n\u001b[0;32m    631\u001b[0m \u001b[38;5;28;01mnonlocal\u001b[39;00m cache_key\n\u001b[0;32m    632\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m cache_key \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    633\u001b[0m     \u001b[38;5;66;03m# Delay generating the cache key until the first call.\u001b[39;00m\n\u001b[0;32m    634\u001b[0m     \u001b[38;5;66;03m# This way we can see values of globals, including functions\u001b[39;00m\n\u001b[0;32m    635\u001b[0m     \u001b[38;5;66;03m# defined after this one.\u001b[39;00m\n\u001b[0;32m    636\u001b[0m     \u001b[38;5;66;03m# If we generated the key earlier we would only hash those\u001b[39;00m\n\u001b[0;32m    637\u001b[0m     \u001b[38;5;66;03m# globals by name, and miss changes in their code or value.\u001b[39;00m\n\u001b[1;32m--> 638\u001b[0m     cache_key \u001b[38;5;241m=\u001b[39m _hash_func(non_optional_func, hash_funcs)\n\u001b[0;32m    640\u001b[0m \u001b[38;5;66;03m# First, get the cache that's attached to this function.\u001b[39;00m\n\u001b[0;32m    641\u001b[0m \u001b[38;5;66;03m# This cache's key is generated (above) from the function's code.\u001b[39;00m\n\u001b[0;32m    642\u001b[0m mem_cache \u001b[38;5;241m=\u001b[39m _mem_caches\u001b[38;5;241m.\u001b[39mget_cache(cache_key, max_entries, ttl)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\caching.py:768\u001b[0m, in \u001b[0;36m_hash_func\u001b[1;34m(func, hash_funcs)\u001b[0m\n\u001b[0;32m    757\u001b[0m update_hash(\n\u001b[0;32m    758\u001b[0m     (func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__module__\u001b[39m, func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__qualname__\u001b[39m),\n\u001b[0;32m    759\u001b[0m     hasher\u001b[38;5;241m=\u001b[39mfunc_hasher,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    762\u001b[0m     hash_source\u001b[38;5;241m=\u001b[39mfunc,\n\u001b[0;32m    763\u001b[0m )\n\u001b[0;32m    765\u001b[0m \u001b[38;5;66;03m# Include the function's body in the hash. We *do* pass hash_funcs here,\u001b[39;00m\n\u001b[0;32m    766\u001b[0m \u001b[38;5;66;03m# because this step will be hashing any objects referenced in the function\u001b[39;00m\n\u001b[0;32m    767\u001b[0m \u001b[38;5;66;03m# body.\u001b[39;00m\n\u001b[1;32m--> 768\u001b[0m update_hash(\n\u001b[0;32m    769\u001b[0m     func,\n\u001b[0;32m    770\u001b[0m     hasher\u001b[38;5;241m=\u001b[39mfunc_hasher,\n\u001b[0;32m    771\u001b[0m     hash_funcs\u001b[38;5;241m=\u001b[39mhash_funcs,\n\u001b[0;32m    772\u001b[0m     hash_reason\u001b[38;5;241m=\u001b[39mHashReason\u001b[38;5;241m.\u001b[39mCACHING_FUNC_BODY,\n\u001b[0;32m    773\u001b[0m     hash_source\u001b[38;5;241m=\u001b[39mfunc,\n\u001b[0;32m    774\u001b[0m )\n\u001b[0;32m    775\u001b[0m cache_key \u001b[38;5;241m=\u001b[39m func_hasher\u001b[38;5;241m.\u001b[39mhexdigest()\n\u001b[0;32m    776\u001b[0m _LOGGER\u001b[38;5;241m.\u001b[39mdebug(\n\u001b[0;32m    777\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmem_cache key for \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m.\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m: \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m, func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__module__\u001b[39m, func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__qualname__\u001b[39m, cache_key\n\u001b[0;32m    778\u001b[0m )\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:109\u001b[0m, in \u001b[0;36mupdate_hash\u001b[1;34m(val, hasher, hash_reason, hash_source, context, hash_funcs)\u001b[0m\n\u001b[0;32m    106\u001b[0m hash_stacks\u001b[38;5;241m.\u001b[39mcurrent\u001b[38;5;241m.\u001b[39mhash_source \u001b[38;5;241m=\u001b[39m hash_source\n\u001b[0;32m    108\u001b[0m ch \u001b[38;5;241m=\u001b[39m _CodeHasher(hash_funcs)\n\u001b[1;32m--> 109\u001b[0m ch\u001b[38;5;241m.\u001b[39mupdate(hasher, val, context)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:386\u001b[0m, in \u001b[0;36m_CodeHasher.update\u001b[1;34m(self, hasher, obj, context)\u001b[0m\n\u001b[0;32m    384\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mupdate\u001b[39m(\u001b[38;5;28mself\u001b[39m, hasher, obj: Any, context: Optional[Context] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    385\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Update the provided hasher with the hash of an object.\"\"\"\u001b[39;00m\n\u001b[1;32m--> 386\u001b[0m     b \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mto_bytes(obj, context)\n\u001b[0;32m    387\u001b[0m     hasher\u001b[38;5;241m.\u001b[39mupdate(b)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:375\u001b[0m, in \u001b[0;36m_CodeHasher.to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    372\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m\n\u001b[0;32m    374\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m ex:\n\u001b[1;32m--> 375\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m InternalHashError(ex, obj)\n\u001b[0;32m    377\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m    378\u001b[0m     \u001b[38;5;66;03m# In case an UnhashableTypeError (or other) error is thrown, clean up the\u001b[39;00m\n\u001b[0;32m    379\u001b[0m     \u001b[38;5;66;03m# stack so we don't get false positives in future hashing calls\u001b[39;00m\n\u001b[0;32m    380\u001b[0m     hash_stacks\u001b[38;5;241m.\u001b[39mcurrent\u001b[38;5;241m.\u001b[39mpop()\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:361\u001b[0m, in \u001b[0;36m_CodeHasher.to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    357\u001b[0m hash_stacks\u001b[38;5;241m.\u001b[39mcurrent\u001b[38;5;241m.\u001b[39mpush(obj)\n\u001b[0;32m    359\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m    360\u001b[0m     \u001b[38;5;66;03m# Hash the input\u001b[39;00m\n\u001b[1;32m--> 361\u001b[0m     b \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m:\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m (tname, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_to_bytes(obj, context))\n\u001b[0;32m    363\u001b[0m     \u001b[38;5;66;03m# Hmmm... It's possible that the size calculation is wrong. When we\u001b[39;00m\n\u001b[0;32m    364\u001b[0m     \u001b[38;5;66;03m# call to_bytes inside _to_bytes things get double-counted.\u001b[39;00m\n\u001b[0;32m    365\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msize \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m sys\u001b[38;5;241m.\u001b[39mgetsizeof(b)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:622\u001b[0m, in \u001b[0;36m_CodeHasher._to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    620\u001b[0m code \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mgetattr\u001b[39m(obj, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__code__\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m)\n\u001b[0;32m    621\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m code \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m--> 622\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_file_should_be_hashed(code\u001b[38;5;241m.\u001b[39mco_filename):\n\u001b[0;32m    623\u001b[0m     context \u001b[38;5;241m=\u001b[39m _get_context(obj)\n\u001b[0;32m    624\u001b[0m     defaults \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mgetattr\u001b[39m(obj, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__defaults__\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:403\u001b[0m, in \u001b[0;36m_CodeHasher._file_should_be_hashed\u001b[1;34m(self, filename)\u001b[0m\n\u001b[0;32m    400\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file_is_blacklisted:\n\u001b[0;32m    401\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m    402\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_is_in_folder_glob(\n\u001b[1;32m--> 403\u001b[0m     filepath, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_get_main_script_directory()\n\u001b[0;32m    404\u001b[0m ) \u001b[38;5;129;01mor\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_in_pythonpath(filepath)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:709\u001b[0m, in \u001b[0;36m_CodeHasher._get_main_script_directory\u001b[1;34m()\u001b[0m\n\u001b[0;32m    705\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01m__main__\u001b[39;00m\n\u001b[0;32m    707\u001b[0m \u001b[38;5;66;03m# This works because we set __main__.__file__ to the\u001b[39;00m\n\u001b[0;32m    708\u001b[0m \u001b[38;5;66;03m# script path in ScriptRunner.\u001b[39;00m\n\u001b[1;32m--> 709\u001b[0m abs_main_path \u001b[38;5;241m=\u001b[39m pathlib\u001b[38;5;241m.\u001b[39mPath(__main__\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__file__\u001b[39m)\u001b[38;5;241m.\u001b[39mresolve()\n\u001b[0;32m    710\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(abs_main_path\u001b[38;5;241m.\u001b[39mparent)\n",
      "\u001b[1;31mInternalHashError\u001b[0m: module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_model()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_model at 0x00000143ACC38900>\n```\n\nPlease see the `hash_funcs` [documentation](https://docs.streamlit.io/library/advanced-features/caching#the-hash_funcs-parameter)\nfor more details.\n            "
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# 加载模型\n",
    "@st.cache(allow_output_mutation=True)\n",
    "def load_model():\n",
    "    return joblib.load('gbr_model.pkl')\n",
    "\n",
    "# 应用标题\n",
    "st.title(\"GBR 模型预测应用\")\n",
    "\n",
    "# 输入参数\n",
    "st.sidebar.header('输入参数')\n",
    "\n",
    "def user_input_features():\n",
    "    feature1 = st.sidebar.number_input('特征 1')\n",
    "    feature2 = st.sidebar.number_input('特征 2')\n",
    "    # 添加更多特征...\n",
    "    \n",
    "    data = {\n",
    "        'feature1': feature1,\n",
    "        'feature2': feature2,\n",
    "        # 添加更多特征...\n",
    "    }\n",
    "    features = pd.DataFrame(data, index=[0])\n",
    "    return features\n",
    "\n",
    "df = user_input_features()\n",
    "\n",
    "# 显示输入参数\n",
    "st.subheader('输入的参数')\n",
    "st.write(df)\n",
    "\n",
    "# 加载模型并进行预测\n",
    "model = load_model()\n",
    "prediction = model.predict(df)\n",
    "\n",
    "# 显示预测结果\n",
    "st.subheader('预测结果')\n",
    "st.write(prediction)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da78a06b-c354-4d6c-a9d6-be08fbd011f9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
