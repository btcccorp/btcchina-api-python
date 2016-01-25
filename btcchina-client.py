#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import btcchina
 
access_key="YOUR_ACCESS_KEY"
secret_key="YOUR_SECRET_KEY"
 
bc = btcchina.BTCChina(access_key,secret_key)
 
''' These methods have no arguments '''
#result = bc.get_account_info()
#print result
 
#result = bc.get_market_depth2()
#print result
 
# NOTE: for all methods shown here, the transaction ID could be set by doing
#result = bc.get_account_info(post_data={'id':'stuff'})
#print result
 
''' buy and sell require price (CNY, 5 decimals) and amount (LTC/BTC, 8 decimals) '''
#result = bc.buy(500,1)
#print result
#result = bc.sell(500,1)
#print result
 
''' cancel requires id number of order '''
#result = bc.cancel(2)
#print result
 
''' request withdrawal requires currency and amount '''
#result = bc.request_withdrawal('BTC',0.1)
#print result
 
''' get deposits requires currency. the optional "pending" defaults to true '''
#result = bc.get_deposits('BTC',pending=False)
#print result
 
''' get orders returns status for one order if ID is specified,
    otherwise returns all orders, the optional "open_only" defaults to true '''
#result = bc.get_orders(2)
#print result
#result = bc.get_orders(open_only=True)
#print result
 
''' get withdrawals returns status for one transaction if ID is specified,
    if currency is specified it returns all transactions,
    the optional "pending" defaults to true '''
#result = bc.get_withdrawals(2)
#print result
#result = bc.get_withdrawals('BTC',pending=True)
#print result
 
''' Fetch transactions by type. Default is 'all'. 
    Available types 'all | fundbtc | withdrawbtc | fundmoney | withdrawmoney | 
    refundmoney | buybtc | sellbtc | tradefee'
    Limit the number of transactions, default value is 10 '''
#result = bc.get_transactions('all',10)
#print result

'''get archived order returns a specified id order which is archived,
   the market default to "BTCCNY" and the "withdetail" default to false,if "withdetail" is specified to "true", the result will include the order's detail'''
#result = bc.get_archived_order(2,'btccny',False)
#print result

'''get archived orders returns the orders which order id is less than the specified "less_than_order_id",and the returned amount is defined in "limit",
   default value is 200, if "withdetail" is specified to "true",
   the result will include to orders' detail'''
#result = bc.get_archived_orders('btccny',200,10000,False)
#print result
