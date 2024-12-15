print("midterm exam")

from abc import ABC, abstractmethod

class Wallet(ABC):
    @abstractmethod
    def transaction(self, amount, transaction_type):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

class BitcoinWallet(Wallet):
    def __init__(self, owner, btc_balance):
        self.owner = owner
        self._btc_balance = btc_balance

    def transaction(self, amount, transaction_type):
        if transaction_type == "buy":
            print(f"Performing Transaction: Buy {amount} BTC")
            self._btc_balance += amount
        elif transaction_type == "sell":
            if self._btc_balance >= amount:
                print(f"Performing Transaction: Sell {amount} BTC")
                self._btc_balance -= amount
            else:
                print(f"Transaction failed: {self.owner} has insufficient BTC balance!")
        else:
            print("Invalid transaction type!")

    @property
    def balance(self):
        return self._btc_balance

class EthereumWallet(Wallet):
    def __init__(self, owner, eth_balance):
        self.owner = owner
        self._eth_balance = eth_balance

    def transaction(self, amount, transaction_type):
        if transaction_type == "buy":
            print(f"Performing Transaction: Buy {amount} ETH")
            self._eth_balance += amount
        elif transaction_type == "sell":
            if self._eth_balance >= amount:
                print(f"Performing Transaction: Sell {amount} ETH")
                self._eth_balance -= amount
            else:
                print(f"Transaction failed: {self.owner} has insufficient ETH balance!")
        else:
            print("Invalid transaction type!")

    @property
    def balance(self):
        return self._eth_balance

johnpaul_wallet = BitcoinWallet("johnpaul", 0.5)
bobby_wallet = EthereumWallet("bobby", 2.0)

print(f"Bitcoin Wallet for {johnpaul_wallet.owner}")
print(f"Initial Balance: {johnpaul_wallet.balance} BTC")

johnpaul_wallet.transaction(0.2, "buy")

print(f"New Balance: {johnpaul_wallet.balance} BTC\n")

print(f"Ethereum Wallet for {bobby_wallet.owner}")
print(f"Initial Balance: {bobby_wallet.balance} ETH")

bobby_wallet.transaction(1.0, "sell")

print(f"New Balance: {bobby_wallet.balance} ETH")
