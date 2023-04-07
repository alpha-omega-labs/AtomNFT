// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AtomNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct NFTMetadata {
        string pdbid;
        string title;
        string fileContent;
        string sequences;
        string organism;
        string method;
        string doi;
        string authors;
        string accession_date;
    }

    mapping(uint256 => NFTMetadata) private _tokenMetadata;
    
    string private _versionLabel;
    string private _versionDate;

    constructor(string memory tokenName, string memory symbol, string memory versionLabel, string memory versionDate) ERC721(tokenName, symbol) {
        _versionLabel = versionLabel;
        _versionDate = versionDate;
    }

    function mintToken(address owner, string memory pdbid, string memory title, string memory fileContent, string memory sequences, string memory organism,
        string memory method, string memory doi, string memory authors, string memory accession_date)
        public onlyOwner
        returns (uint256)
    {
        _tokenIds.increment();

        uint256 id = _tokenIds.current();
        _safeMint(owner, id);

        _tokenMetadata[id] = NFTMetadata({
            pdbid: pdbid,
            title: title,
            fileContent: fileContent,
            sequences: sequences,
            organism: organism,
            method: method,
            doi: doi,
            authors: authors,
            accession_date: accession_date
        });

        return id;
    }

    function getMetadata(uint256 tokenId) public view returns (string memory, string memory, string memory, string memory, string memory, string memory, string memory, string memory, string memory) {
        require(_exists(tokenId), "Token does not exist");

        NFTMetadata storage metadata = _tokenMetadata[tokenId];
        return (metadata.pdbid, metadata.title, metadata.fileContent, metadata.sequences, metadata.organism, metadata.method, metadata.doi, metadata.authors, metadata.accession_date);
    }

    function getVersion() public view returns (string memory, string memory) {
        return (_versionLabel, _versionDate);
    }

    function setVersion(string memory versionLabel, string memory versionDate) public onlyOwner {
        _versionLabel = versionLabel;
        _versionDate = versionDate;
    }
}
