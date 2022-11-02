

// ## ACCOUNTS USING mnemonic ##
const { mkAccounts } = require("@algo-builder/algob");
let accounts = mkAccounts([
  {
    name: "master",
    addr: process.env.ADDR_CREATOR,
    mnemonic: process.env.MNEMONIC_CREATOR,
  },
  {
    name: "acc1",
    addr: process.env.ACC1_ADDR,
    mnemonic: process.env.ACC1_MNEMONIC,
  },
  {
    name: "acc2",
    addr: process.env.ACC2_ADDR,
    mnemonic: process.env.ACC2_MNEMONIC,
  }
]);


let defaultCfg = {
  host: "http://localhost",
  port: 4001,
  token: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  accounts: accounts,
 
};


module.exports = {
  networks: {
    default: defaultCfg,
    
  },
};
