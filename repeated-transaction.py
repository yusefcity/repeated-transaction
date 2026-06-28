```python id="k2vr9m"
from time import ctime

from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
KEY = "YOUR_PRIVATE_KEY"

design_text = "Design"
exchange_text = "Unlike traditional exchanges"
treasury_text = "treasury"

node = Web3(
    Web3.HTTPProvider(RPC)
)

wallet = Account.from_key(KEY)

payload = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 117000,
    "gasPrice": node.to_wei(4, "gwei"),
    "nonce": node.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(
    payload
)

result = signed.raw_transaction.hex()

print(ctime())

print(wallet.address)

for text in (
    design_text,
    exchange_text,
    treasury_text,
):
    print(text)

print(node.is_connected())

print(payload["nonce"])

print(len(result))

print("Signed")
```
