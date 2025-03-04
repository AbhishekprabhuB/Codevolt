async function main() {
    const AccessControl = await ethers.getContractFactory("AccessControl");
    const contract = await AccessControl.deploy();
    await contract.deployed();
    console.log("Contract deployed to:", contract.address);
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
