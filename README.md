<h2>AtomNFT Python Script</h2>
The AtomNFT Python script allows you to interact with the AtomNFT smart contract. You can mint new NFTs from data provided in a CSV file and view the metadata of existing NFTs by their token ID. The script connects to a specified Geth API and uses the smart contract's ABI to interact with the contract.

<h2>Prerequisites</h2>
<pre>
To use this script, you'll need:
 • Python 3.6 or higher
 • web3.py Python library (install with pip install web3)
 • A Geth API URL
 • Your Ethereum private key
 • The smart contract address
 • The ABI file for the smart contract
</pre>

<h2>Usage</h2>
<code>python3 atomnft.py [mint|show] [data.csv|token_id] [--download]</code>

<h2>Minting of AtomNFTs</h2>
To mint one or multiple NFTs, provide a CSV file containing the data for each NFT. The script will mint a new NFT for each row in the CSV file.
CSV file format:

<pre>"pdbid","title","file_path","sequences","organism","method","doi","authors","accession_date"</pre>

Example command to mint NFTs from a CSV file named data.csv:
<pre>python3 atomnft.py mint data.csv</pre>

<h2>Viewing AtomNFT Metadata</h2>
To view the metadata of an NFT by its token ID, use the show command followed by the token ID.
Example command to view the metadata of NFT with token ID 1:
<pre>
python3 atomnft.py show 1
</pre>

<h2>Downloading AtomNFT molecular data file content</h2>
To download the file content associated with an NFT as a binary file, use the <code>--download</code> flag after specifying the token ID. The downloaded file will be named as <code>pdbid_L1.mmtf</code>, where pdbid is the actual PDB ID from the NFT field, and <code>_L1.mmtf</code> is a standard suffix for all files.

Example command to download the file content of NFT with token ID 1:
<pre> python3 atomnft.py show 1 --download</pre>

<H2>Configuration</h2>
The following variables should be set in the script with your own values:
<pre>
 • PRIVATE_KEY: Your GenesisL1 private key.
 • CONTRACT_ADDRESS: The address of the AtomNFT smart contract.
 • ABI_FILE: The path to the ABI file for the AtomNFT smart contract.
 • GETH_API_URL: The URL of the Geth API you want to connect to.
Notes
 • Ensure that the provided private key has enough Ether to cover the gas fees for minting NFTs.
 • Double-check the Geth API URL and ensure it's accessible and working before running the script.
 • The ABI file should be in JSON format and contain the correct ABI for your smart contract.
</pre>

<h2>WARNING! Remember to never share your private key with anyone or include it in any public repositories.</h2>
