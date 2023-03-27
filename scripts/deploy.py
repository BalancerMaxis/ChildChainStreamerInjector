from brownie import (
    interface,
    accounts,
    periodicRewardsInjector,
)
account = accounts.load("tmdelegate") #load your account here
ADMIN_ADDRESS = "0xc38c5f97B34E175FFd35407fc91a937300E33860" # Balancer Maxi LM Multisig on mainnet, polygon and arbi
LDO_ADDRESS = "0x912ce59144191c1204e64559fe8253a0e49e6548" # LDO address on Arbiturm
injector = periodicRewardsInjector.deploy(
    ADMIN_ADDRESS,
    60 * 60 * 7,  # minWaitPeriodSeconds is 1 week
    LDO_ADDRESS,
    {"from": account}
)
