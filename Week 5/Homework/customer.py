import prodcheck

def buy(product,num,price):
    if prodcheck.func(product, num):
        print( "You bougt", product,"and spent", num*price, "price." )
    else:
        print("Sorry! We are out of this product.")


def main():
    return buy("candy",5,30)

    
main()
