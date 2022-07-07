

from web3 import Web3

ganache_url="http://192.168.29.185:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))


def isAddress(address):
    return (web3.isAddress(address))

def lend(account_1,amount,private_key):
    
#Tutorial Code Goes Here..
    
    
    account_2="0xc806768Ee5F30766BBE3D29f896ac09d121Cb57E"
    #private_key="fad035698bbcc8e53be4e9f33b8ab2b01c31efea0dd46776f63b94deb1819df5"
    nonce=web3.eth.getTransactionCount(account_1)
    
    print(web3.isConnected())

    
    tx={
        'nonce': nonce,
        'to': account_2,
        'value': web3. toWei(amount, 'ether'),
        'gas': 200000,
        'gasPrice': web3.toWei('50', 'gwei')

    }
    signed_tx=web3.eth.account.signTransaction(tx, private_key)
    tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(web3. toHex(tx_hash))




#lend()

import json

def borrow(account_2,amount):
    print(isAddress(account_2))


    
    account_1="0xd34eFe2bD22237487C51E789e65561dd7e97b9A9"
    #account_2="0xDdf40da63Bb248d4364F5a942CF3F46B684e6F58"
    private_key="0x24abc5f4fe893dda0d8ba5ad889a6728fc39725d6219ab58ec0589571343a562"
    nonce=web3.eth.getTransactionCount(account_1)
    print(nonce)

    #amount=input("Enter amount:")
    tx={
        'nonce': nonce,
        'to': account_2,
        'value': web3. toWei(amount, 'ether'),
        'gas': 200000,
        'gasPrice': web3.toWei('50', 'gwei')

    }
    signed_tx=web3.eth.account.signTransaction(tx, private_key)
    tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return(web3. toHex(tx_hash))




#print("Borrow")

#borrow()
import pickle

def New_account(name,username,password):

    
    account={}
    user={}
    acc_address=[]
    acc_private_key=[]


    
    acc=web3.eth.account.create()
        
    user['Name']=name
    user['username']=username
    user['Account_Address']=acc.address
    user['private_key']=acc.privateKey
    user['password']=password

    account[username]=user

    accountinfo=[acc.address,acc.privateKey]


        
    convert_file=open('account_details.pkl', 'ab') 

    pickle.dump(account,convert_file)
    convert_file.close()
        
        

    
    return accountinfo
    


#accounts()
#print("Account\n\n")

def check_balance(address):


    wallet=web3.eth.get_balance(address)
    wallet=wallet/1000000000000000000

    print(wallet)
    return(wallet)




def verify_private_key(address,private_key):

    pa=web3.eth.account.from_key(private_key)
    print(pa.address)

    if pa.address==address:
        return(True)
    
    else:
        return(False)


#check_balance('0x8c9e9D99aA384202E250051018D57dA984ec6aC8')

#verify_private_key('0xc6003Ee79EFFbE0560fB3147399A1896c76a8218','0x0f1fb67560ca2d67efb8b9e805b72d6694e7ba1db9c93233706f9c6e85532cc9')