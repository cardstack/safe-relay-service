from logging import getLogger

from django.conf import settings

from eth_account import Account

from gnosis.eth import EthereumClient, EthereumClientProvider

from safe_relay_service.gas_station.gas_station import (GasStation,
                                                        GasStationProvider)

logger = getLogger(__name__)


#TODO Test this service
class FundingServiceProvider:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = FundingService(EthereumClientProvider(), GasStationProvider(),
                                          settings.SAFE_FUNDER_PRIVATE_KEY, settings.SAFE_FUNDER_MAX_ETH)
        return cls.instance

    @classmethod
    def del_singleton(cls):
        if hasattr(cls, "instance"):
            del cls.instance


class FundingService:
    def __init__(self, ethereum_client: EthereumClient, gas_station: GasStation,
                 funder_private_key: str, max_eth_to_send: int):
        self.ethereum_client = ethereum_client
        self.gas_station = gas_station
        self.funder_account = Account.privateKeyToAccount(funder_private_key)
        self.max_eth_to_send = max_eth_to_send

    def send_eth_to(self, to: str, value: int, gas: int = 22000, gas_price=None,
                    retry: bool = False, block_identifier='pending'):
        if not gas_price:
            gas_price = self.gas_station.get_gas_prices().standard
        return self.ethereum_client.send_eth_to(self.funder_account.privateKey, to, gas_price, value,
                                                gas=gas,
                                                retry=retry,
                                                block_identifier=block_identifier,
                                                max_eth_to_send=self.max_eth_to_send)