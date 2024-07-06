from poc_constants.modules.configs.parameters import ConfigLoader

def main():
    config_loader = ConfigLoader('th')

    print('\n')
    print('# Teste com os storage accounts')
    print(config_loader.get_storage_account().bronze)
    print(config_loader.get_storage_account().silver)
    print(config_loader.get_storage_account().gold)


    print('\n')
    print('# Teste com a service principal')
    print(config_loader.get_service_principal().id)


    print('\n')
    print('# Teste com os catálogos')
    print(config_loader.get_principal_catalog().name)
    print(config_loader.get_principal_catalog().schema_bronze)
    print(config_loader.get_principal_catalog().schema_silver)
    print(config_loader.get_principal_catalog().schema_gold)

if __name__ == "__main__":
    main()    