from dataclasses import dataclass

@dataclass
class Wire:
    fileId: str
    origin: str
    fileDate: str
    executionDate: str 
    beneficiaryAccount: str
    originAccount: str 
    wireAmount: str
    wireAmountCurrency: str