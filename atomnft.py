import sys
import csv
import json
import base64
from pathlib import Path
from getpass import getpass
from web3 import Web3, HTTPProvider
import pandas as pd

# Replace these with your own values
PRIVATE_KEY = ""
CONTRACT_ADDRESS = ""
ABI_FILE = "abi.json"
GETH_API_URL = ""


# Read ABI from file
with open(ABI_FILE, "r") as abi_file:
    ABI = json.load(abi_file)

# Connect to Geth API
w3 = Web3(HTTPProvider(GETH_API_URL))
if not w3.isConnected():
    print("Error: Could not connect to Geth API.")
    sys.exit(1)

# Set up the contract instance
contract = w3.eth.contract(address=w3.toChecksumAddress(CONTRACT_ADDRESS), abi=ABI)

# Set up the account for minting
account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)


def mint_nft(data_csv):
    df = pd.read_csv(data_csv)
    for index, row in df.iterrows():
        with open(row["file_path"], "rb") as file:
            file_content_base64 = base64.b64encode(file.read()).decode("utf-8")

        nonce = w3.eth.getTransactionCount(account.address)
        txn = contract.functions.mintToken(
            account.address,
            row["pdbid"],
            row["title"],
            file_content_base64,
            row["sequences"],
            row["organism"],
            row["method"],
            row["doi"],
            row["authors"],
            row["accession_date"]
        ).buildTransaction({
            "chainId": w3.eth.chain_id,
            "gas": 2000000000,
            "gasPrice": w3.eth.gas_price,
            "nonce": nonce,
        })

        signed_txn = w3.eth.account.signTransaction(txn, PRIVATE_KEY)
        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

        if txn_receipt["status"]:
            print(f"Successfully minted NFT (ID: {index + 1})")
        else:
            print(f"Failed to mint NFT (ID: {index + 1})")



def show_nft(token_id, download=False):
    metadata = contract.functions.getMetadata(token_id).call()
    metadata_fields = ["pdbid", "title", "fileContent", "sequences", "organism", "method", "doi", "authors", "accession_date"]
    metadata_dict = dict(zip(metadata_fields, metadata))

    for key, value in metadata_dict.items():
        print(f"{key}: {value}")

    if download:
        file_content_base64 = metadata_dict["fileContent"]
        file_content = base64.b64decode(file_content_base64.encode("utf-8"))
        pdbid = metadata_dict["pdbid"]
        file_name = f"{pdbid}_L1.mmtf"
        with open(file_name, "wb") as file:
            file.write(file_content)
        print(f"File successfully downloaded as {file_name}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 atomnft.py [mint|show] [data.csv|token_id] [--download]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "mint":
        data_csv = sys.argv[2]
        mint_nft(data_csv)
    elif command == "show":
        token_id = int(sys.argv[2])
        download = len(sys.argv) > 3 and sys.argv[3] == "--download"
        show_nft(token_id, download)
    else:
        print("Invalid command. Use 'mint' or 'show'.")


















