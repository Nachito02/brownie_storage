from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange -> Organizar o arreglar las cosas
    account = accounts[0]
    #Act -> Hacer algo
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    #Assert -> Comprobar que halgo ha ido bien 
    assert starting_value == expected


def test_updating_storage():
     # Arrange -> Organizar o arreglar las cosas
    account = accounts[0]
    #Act -> Hacer algo
    simple_storage = SimpleStorage.deploy({"from": account})

    txn = simple_storage.store(42, {"from" : account})
    txn.wait(1)
    expected = 42
    # Assert
    assert simple_storage.retrieve() == expected