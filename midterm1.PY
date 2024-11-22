print("midterm exam")

from abc import ABC, abstractmethod

class Wallet(ABC):
    @abstractmethod
    def transaction(self, amount: float, transaction_type: str):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

class BitcoinWallet(Wallet):
    def __init__(self, owner: str, btc_balance: float):
        self.owner = owner
        self.__btc_balance = btc_balance

    def transaction(self, amount: float, transaction_type: str):
        if transaction_type == "buy":
            print(f"Performing Transaction: Buy {amount} BTC")
            self.__btc_balance += amount
        elif transaction_type == "sell":
            if self.__btc_balance >= amount:
                print(f"Performing Transaction: Sell {amount} BTC")
                self.__btc_balance -= amount
            else:
                print(f"Transaction failed: {self.owner} has insufficient BTC balance!")
        else:
            print("Invalid transaction type!")

    @property
    def balance(self):
        return self.__btc_balance

class EthereumWallet(Wallet):
    def __init__(self, owner: str, eth_balance: float):
        self.owner = owner
        self.__eth_balance = eth_balance

    def transaction(self, amount: float, transaction_type: str):
        if transaction_type == "buy":
            print(f"Performing Transaction: Buy {amount} ETH")
            self.__eth_balance += amount
        elif transaction_type == "sell":
            if self.__eth_balance >= amount:
                print(f"Performing Transaction: Sell {amount} ETH")
                self.__eth_balance -= amount
            else:
                print(f"Transaction failed: {self.owner} has insufficient ETH balance!")
        else:
            print("Invalid transaction type!")

    @property
    def balance(self):
        return self.__eth_balance
    
    def __str__(self):
        return f"Eterium Wallet for {self.owner}: {self.__eth_balance} ETH"

Johnpaul_wallet = BitcoinWallet("Johnpaul", 0.5)
Bobby_wallet = EthereumWallet("Bobby", 2.0)

print(f"Bitcoin Wallet for {Johnpaul_wallet.owner}")
print(f"Initial Balance: {Johnpaul_wallet.balance} BTC")

Johnpaul_wallet.transaction(0.2, "buy")

print(f"New Balance: {Johnpaul_wallet.balance} BTC\n")

print(f"Ethereum Wallet for {Bobby_wallet.owner}")
print(f"Initial Balance: {Bobby_wallet.balance} ETH")

Bobby_wallet.transaction(1.0, "sell")

print(f"New Balance: {Bobby_wallet.balance} ETH")