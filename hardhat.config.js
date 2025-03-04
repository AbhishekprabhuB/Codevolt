require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: {
    version: "0.8.28",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    polygon: {
      url: "https://polygon-mainnet.infura.io/v3/8d3c0eaa954f46b2a0b74d2ee724f28f",
      accounts: ["ce64c09f709f4d183417bb87fdd259690546f49408ae6f74a460747b19f8d1f1"]
    }
  }
};
