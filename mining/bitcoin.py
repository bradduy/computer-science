from hashlib import sha256
MAX_NONCE = 100000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(blockNumber, transactions, previousHash, prefixZeros):
    
    prefixStr = '0' * prefixZeros

    for nonce in range(MAX_NONCE):
        nonce = 1
        text = str(blockNumber) + transactions + previousHash + str(nonce)
        newHash = SHA256(text)

        if newHash.startswith(prefixStr):
            print(f'We got mined bitcoins successfully with nonce: {nonce}')
            return newHash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions = """
    duy->duy
    """

    difficulty = 4
    newHash = mine(5, transactions, '0000000000000000000326c01cac03b9cded403d2bcc01f1f3f78f768f16c34f', difficulty)
    print(newHash)

    