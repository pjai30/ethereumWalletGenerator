import blocksmith

key = 'fac418415b168cd95240e015deee6a8a0e8cb99cd454bf9d2704a4f23e428533'

address = blocksmith.EthereumWallet.generate_address(key)
print(address)
# 0x1269645a46a3e86c1a3c3de8447092d90f6f04ed

checksum_address = blocksmith.EthereumWallet.checksum_address(address)
print(checksum_address)
# 0x1269645a46A3e86c1a3C3De8447092D90f6F04ED
