import pytest
from app.calculation import add, subtract, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    print("Creating empty account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(95)
  

@pytest.mark.parametrize("num1, num2, expected", [
  (3, 2, 5),
  (7, 2, 9),
  (20, 20, 40)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add (num1, num2) == expected
    
def test_subtract():
    assert subtract (9, 3) == 6
 
 
       
def test_bank_set_initial_amount(bank_account):
    #bank_account = BankAccount(70)
    assert bank_account.balance == 95
    

def test_bank_default_amount(zero_bank_account):
    print("testing my empty account")
    assert zero_bank_account.balance == 0
    
def test_withdraw(bank_account):
    #Bank_account = BankAccount(70)
    bank_account.withdraw(15)
    assert bank_account.balance == 80
  
def test_deposit(bank_account):
    #Bank_account = BankAccount (55)
    bank_account.deposit(20)
    assert bank_account.balance == 115

def test_collect_Interest(bank_account):
    #Bank_account = BankAccount (90)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 104.5
    
    
@pytest.mark.parametrize("deposit, withdraw, expected", [
  (300, 200, 100),
  (700, 200, 500),
  (20, 10, 10),
  (1000, 300, 700),
  (4000, 200, 3800),
  #(30, 40, -10 )
])   


def test_bank_transaction(zero_bank_account, deposit, withdraw, expected):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected#
  

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
         bank_account.withdraw(300)
    
    
  
  
  