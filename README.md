# periodicRewardsInjector

This contract is meant to be called by chainlink uplink.  It is used in cases where DAOs wish to add extra yields to their Balancer Gaugue emisisons and want more granular control than using the gauge system would allow.


The tests are based on LDO on Arbitrum where a multisig is curerntly doing these operations.

to run tests

```bash
pip3 install brownie
brownie test --network arbitrum-main-fork
```

If you do not have this network and the following lines to the end of your `~/.brownie/netowrk_config-yaml`
```yaml
  - name: Ganache-CLI (Arbitrum-Mainnet Fork)
    id: arbitrum-main-fork
    cmd: ganache-cli
    host: http://127.0.0.1
    timeout: 120
    cmd_settings:
      port: 8545
      gas_limit: 20000000
      accounts: 10
      evm_version: istanbul
      mnemonic: brownie
      fork: arbitrum-main

```

your .env file will require:
```
WEB3_INFURA_PROJECT_ID=
or other arbitrum RPC
```

To deploy use the deploy script.  

## Once this is deployed
- Sufficient tokens for at least 1 epoch must be sent into the contract and are meant to be stored there.
  - The admin is able to sweep tokens
- The job will only run ever minWaitSeconds and when there is no active epoch

## Further setup

### Setting a watchlist
The admin must setup a watch list.

 `setRecipientList([streamer.address], [weekly_incentive_gwei_in_configured_token], [maximum_payout_periods])`
 
To specify 1 gauge, use the address, the amount, and the number of periods.  For multiple gauges, setup the lists so the same list index provides matching data for all fields.

### Funding the contract
Send at least enough tokens into the contract to pay out one period.  In order to run the full schedule up to max_payout_periods, send max_payout_periods*weekly_incentive to the contract.

