from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    born_in = serializers.CharField()
    born_in_the = serializers.CharField()
    citizenship = serializers.CharField()
    tax_code = serializers.CharField()
    address = serializers.CharField()
    city_zip_prov = serializers.CharField()
    id_type_num = serializers.CharField()
    released_by = serializers.CharField()
    expiration = serializers.CharField()
    representative_of = serializers.CharField()
    chamber_registration_num = serializers.CharField()
    chamber_tax_code = serializers.CharField()
    chamber_str_civic = serializers.CharField()
    chamber_city_zip_prov = serializers.CharField()
    chamber_state = serializers.CharField()
    business_relations = serializers.CharField()
    value_of_transaction = serializers.CharField()
    extra_documents = serializers.CharField()