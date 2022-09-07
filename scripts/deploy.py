from brownie import SimpleStorage, network, accounts, config
def deployer():
    simple_storage= SimpleStorage.deploy({"from":get_account()},publish_source= True)
    # simple_storage= SimpleStorage[-1]
    print(simple_storage.retrieve())
    txn1= simple_storage.store(144,{"from":get_account()})
    txn1.wait(1)
    print(simple_storage.retrieve())

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deployer()