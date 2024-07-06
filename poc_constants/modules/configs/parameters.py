import yaml
from poc_constants.modules.configs.env import Environment
from poc_constants.modules.utils.yaml_func import YamlFunctions
from poc_constants.modules.models.principal_catalog import PrincipalCatalog
from poc_constants.modules.models.service_principal import ServicePrincipal
from poc_constants.modules.models.storage_account import StorageAccount

class ConfigLoader:

    def __init__(self, force_env='tu'):
        self.current_env = Environment.get_current_env(force_env)
        self.config = YamlFunctions('poc_constants\modules\configs\config.yaml').process_yaml_replacement('{env_acronym}', self.current_env)

    def get_principal_catalog(self) -> PrincipalCatalog:
        return PrincipalCatalog(self.config['principal_catalog'])

    def get_service_principal(self) -> ServicePrincipal:
        return ServicePrincipal(self.config['service_principal'][self.current_env])
    
    def get_storage_account(self) -> StorageAccount:
        return StorageAccount(self.config['storage_account'])

