# form_filler_api

prerequisites:

python version: 3.9.7

#how to run

###create python virtualenv
`python3 -m venv _venv`

###activate environment
`source _venv/bin/activate`
###install requirements:
`pip install -r requirements.txt`
###run server

```
cd form_filler/
python manage.py runserver 127.0.0.1:8000 #(use available ip:port)
```

##Endpoint details
###Request type: POST
###Request URL: `http://127.0.0.1:8000/renderer/`
###Sample Request data:
```
{
    "name": "Full name",
    "born_in": "born in",
    "born_in_the": "space after the",
    "citizenship": "citizen of",
    "tax_code": "personal tax code",
    "address": "address",
    "city_zip_prov": "city zip code and province",
    "id_type_num": "id doc type and number",
    "released_by": "id released by authority",
    "expiration": "date of id expiration",
    "representative_of": "representive of",
    "chamber_registration_num": "the chambers registration number",
    "chamber_tax_code": "camber's tax code",
    "chamber_str_civic": "chamber's street and civic number",
    "chamber_city_zip_prov": "chamber's city zip and province",
    "chamber_state": "chamber's state",
    "business_relations": "any business relations",
    "value_of_transaction": "value of transaction",
    "extra_documents": "details of extra documents"
}
```
###Response: pdf file

##Approach used
The document is converted into basic html template with blanks as 
django template variables. The date passed along with request is 
serialized, validated and then put into the template,
that template is then converted into pdf and returned in response.