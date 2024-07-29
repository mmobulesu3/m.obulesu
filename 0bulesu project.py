 #item and details
powder= ['turmanic','chilli','salt','wheat','corn floor','sugar','tea powder']
quantity = [100,200,100,40,50,100,500]
price = [40,400,10,40,50,60,450]
s_qty=[0,0,0,0,0,0,0]
o_price =[10,15,20,25,30,10,9]
profit =[]
i_profit = [0,0,0,0,0,0,0]
ui=0
revenue=[]
c=1
p=0
raw=['meat','fish','beaf','camel','egg']
quantity1=[650,150,300,400,120]
price1=[800,200,400,600,20]
s_qty1=[0,0,0,0,0]
o_price1=[20,40,50,60,2]
profit1=[]
i_profit1=[0,0,0,0,0]
ri=0
revenue1=[]
c=1
p=1


 #s_qty = sold quantity, o_price = original price, i_profit = itemiezed profit, pqty = purchased quantity

while True:
#asking input to the owner
    ch = input('user or out :')
    print('')
    if ch == 'user':
#items will be shown to the customers
        print('@'*29,'available items are:','@'*29)
        print('')
        for it in zip(powder ,quantity,price):
            print(it[0],'-->',it[1],'kgs''-->',it[2],'/- per kg')
        print('@'*39,'available items are','@'*39)
        print('')
        for it in zip(raw,quantity1,price1):
            print(it[0],'-->',it[1],'kg''-->',it[2],'/-per kg')
        print('^'*20,'available items are','^'*40)
        print('')
        
        cart = []
        itemizedbill = []
        pqty = []
        bill=0
        print('')
        while True:
            print("")
            item = input('Enter an item to buy: ')
#checking item in list
            if item in powder:
                qty = float(input('how many kgs do you want: '))
                idx = powder.index(item)
                cart.append(item)
                print("")
#checkng for available quantity, calculating the bill and profits for each and every item and adding purchased quantity,itemizedbill into the empty lists
            if qty<=quantity[idx]:
                    pqty.append(qty)
                    amount = qty*price[idx]
                    prf=(price[idx]*qty)-(o_price[idx]*qty)
                    profit.append(prf)
                    itemizedbill.append(amount)
                    quantity[idx]=quantity[idx]-qty
                    s_qty[idx]= s_qty[idx]+qty
                    bill = amount+bill
                    i_profit[idx]=i_profit[idx]+(price[idx]*qty)-(o_price[idx]*qty)
                
#asking customer if they want more to buy
                    ch = input('want to buy more (yes/no): ')
                    print("")
                    if ch== 'no':
                        revenue.append(bill)
#asking customer to select cart or bill
                        ch =input('cart/bill: ')
                        print('')
                        if ch == 'cart':
                            for it in zip(cart,itemizedbill,pqty):
                                print(it[0],it[1],'/-',it[2],'kgs')
                                print("")
                            ch= input('wanto buy items again or goto bill (buy/bill): ')
                            if ch=="bill":
                                for it in zip(cart,itemizedbill,pqty):
                                    print(it[0],it[1],'/-',it[2],'kgs')
                                print("")
                                print('the total amount is: ',bill)
                                print("")
                                print('*'*40,'Thank You for shopping','*'*40)
                                break
                        else:
                            for it in zip(cart,itemizedbill,pqty):
                                print(it[0],it[1],'/-',it[2],'kgs')
                            print("")
                            print('the total amount is: ',bill)
                            print("")
                            print('*'*40,'Thank You for shopping','*'*40)
                            break
#after one customer shops, the program restarts and waits for another customer to shop
                        
                    else:  
                     print(item,'added to cart')
            else:
                    print('quantity is unavailable')                                 
        else:
                print('item unavailable')
#manger_display
    else:
#entering  to manger to login
        print('enter your login details')
        ch1 = input('username: ')
        ch2 = input('password: ')
        if ch1== 'obulesu' and ch2== 'siva':
            print('_'*40,'welcome obulesu','_'*40)
            print("")
            ch=(input('info/close: '))
            if ch=='close':
                print('hi my dear  obulesu')
                for v in range (len(powder)):
                    if quantity[v]<5:
                        print('You are lacking of',powder[v],'the available quantity is: ',quantity[v],'kgs only')
                print('Thank You')
                print('>'*50,'you closed the store','<'*50)
                break
            else:
                while True:
                    print(''')
                        1.REVENUE
                        2.PROFIT
                        3.ITEMIEZED PROFIT
                        4.close the store''')
                    print('')
                    ch= input('select an option: ')
                    if ch=='1':
                        for j in revenue:
                            print('customer',c,'--',j)
                            c=c+1
                        for r in revenue:
                            ui=ui+r
                        print('')
                        print('your total revenue today is:',ui)
                        print('')
                    elif ch == '2':
                        for f in profit:
                            p=p+f
                        print('your profit today is: ',p)
                        print('')
                    elif ch=='3':
                        print('')
                        print('your itemeized profit today is: ')
                        print('')
                        for a in zip(powder,s_qty,i_profit):
                            print(a[0],'-->',a[1],'kgs',a[2],'/-')
                            print("")
                    elif ch=='4':
                        print('')
                        print('hi my dear obulesu')
                        for v in range (len(powder)):
                            if quantity[v]<5:
                                print('You are lacking of',powder[v],'the available quantity is: ',quantity[v],'kgs only')
                        print('Thank You')
                        print("")
                        print('>'*45,'you closed the shop','<'*45)
                        break
                break
        else:
            print('username or password invalid')
            
                


