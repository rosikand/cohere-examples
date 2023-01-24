# Notes on `cohere.ai` client 


## Initializing your client 

You connect to your cohere client by initializing an object in Python: 

```python
cohere_client = cohere.Client('YOUR_COHERE_API_KEY')
```

## Debugging 

When debugging, we can look at the class methods for the client to see what functionalities we have access too: 

```python
(Pdb) dir(cohere_client)
['_Client__print_warning_msg', '_Client__pyfetch', '_Client__request', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_executor', 'api_key', 'api_url', 'batch_detokenize', 'batch_generate', 'batch_size', 'batch_tokenize', 'chat', 'check_api_key', 'classify', 'cohere_version', 'detect_language', 'detokenize', 'embed', 'feedback', 'generate', 'max_retries', 'num_workers', 'request_dict', 'request_source', 'tokenize']
```

(as of 1/23/23)

the api docs verify that we have the following functionalities to work with: 

- `generate`
- `embed`
- `classify`
- `tokenize`
- `detokenize`
- `detect-language`
- (new) `chat`

