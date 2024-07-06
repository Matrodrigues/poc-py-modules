class StorageAccount:

    def __init__(self, storage_account_configs):
        self.bronze = storage_account_configs['bronze']
        self.silver = storage_account_configs['silver']
        self.gold = storage_account_configs['gold']