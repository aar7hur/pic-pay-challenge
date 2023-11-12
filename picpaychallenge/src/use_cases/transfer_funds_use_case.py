from picpaychallenge.src.interface_adapters.repositories.interfaces.bank_account.bank_account_interface import (
    IBankAccountRepository,
)


class TransferFundsUseCase:
    """Use case for transferring funds between bank accounts."""

    def __init__(self, bank_account_repository: IBankAccountRepository):
        """Initialize the TransferFundsUseCase with a bank account repository.

        Args:
            bank_account_repository (IBankAccountRepository): The repository for bank accounts.
        """
        self.bank_account_repository = bank_account_repository

    def execute(self, sender_account_number: str, recipient_account_number: str, amount: float):
        """Execute the fund transfer between bank accounts.

        Args:
            sender_account_number (str): The account number of the sender.
            recipient_account_number (str): The account number of the recipient.
            amount (float): The amount to be transferred.
        """
        pass
