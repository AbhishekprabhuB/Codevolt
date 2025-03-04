from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Connect to Polygon network
infura_url = "https://polygon-mainnet.infura.io/v3/8d3c0eaa954f46b2a0b74d2ee724f28f"
web3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "YOUR_DEPLOYED_CONTRACT_ADDRESS"
contract_abi = [YOUR_CONTRACT_ABI]  # Replace with actual ABI

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/grant_access', methods=['POST'])
def grant_access():
    user_address = request.json['user']
    tx = contract.functions.grantAccess(user_address).transact()
    return jsonify({"tx": tx.hex()})

@app.route('/check_access', methods=['GET'])
def check_access():
    user_address = request.args.get('user')
    has_access = contract.functions.checkAccess(user_address).call()
    return jsonify({"access": has_access})

if __name__ == '__main__':
    app.run(debug=True)
