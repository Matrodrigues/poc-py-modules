class PrincipalCatalog:

    def __init__(self, principal_catalog_configs):
        self.name = principal_catalog_configs['name']
        self.schema_bronze = principal_catalog_configs['schema_bronze']
        self.schema_silver = principal_catalog_configs['schema_silver']
        self.schema_gold = principal_catalog_configs['schema_gold']
    