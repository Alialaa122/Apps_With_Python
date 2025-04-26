
sourcelist=["USD","EUR","CAD"]
currency_history=[]

def american_dollar(amount,target):

    if  target=="CAD":
       result=f"{amount} USD is equal {amount*1.42} CAD"
    
    if  target=="EUR":
        result=f"{amount} USD is equal {amount*0.96} EUR"
    print(result)
    currency_history.append(result)

def Euro(amount,target):

    if  target=="USD":
        result=f"{amount} EUR is equal {amount*1.05} USD"

    if  target=="CAD":
        result=f"{amount} EUR is equal {amount*1.49} CAD"

    print(result)
    currency_history.append(result)

def Canidian_dollar(amount,target):
    
    if  target=="EUR":
        result=f"{amount} CAD is equal {amount*0.67} EUR"

    if  target=="USD":
        result=f"{amount} CAD is equal {amount*0.70} USD"

    print(result)
    currency_history.append(result)

def display_equivalence(source):

    if source=="USD":
        print(f"{1} USD is equal {1*1.42} CAD")
        print(f"{1} USD is equal {1*0.96} EUR")
    
    elif source=="EUR":
        print(f"{1} EUR is equal {1*1.05} USD")
        print(f"{1} EUR is equal {1*1.49} CAD")

    else:
        print(f"{1} CAD is equal {1*0.67} EUR")
        print(f"{1} CAD is equal {1*0.70} USD")



def get_user_inputs():
 
 try:

    amount=float(input("Enter the amount: "))
    source=input("Source currency (USD/EUR/CAD): ").strip().upper()

    if source not in sourcelist:
            print("Sorry We Don't Support this Currency Right Now")
            return None

    display_equivalence(source)    
    target=input("Target currency (USD/EUR/CAD): ").strip().upper()

    if target not in sourcelist:
            print("Sorry We Don't Support this Currency Right Now")
            return None
    
    if source==target:
         print("Source and target currencies must be different.")
         return None
    
    return amount,source,target
 
 except ValueError:
      print("Please, Enter A vaild Number.")
        
def convertor(source,amount,target):
        
        if source=="USD":
            american_dollar(amount,target)
        
        elif source=="EUR":
            Euro(amount,target)

        else:
            Canidian_dollar(amount,target)


def Program():
    while True:

        user_inputs=get_user_inputs()

        if user_inputs:
            amount,source,target=user_inputs
            convertor(source,amount,target)
        
        Continuation=input("Continue?(y/n)").strip().lower()
        if Continuation=="n":
            if currency_history:
                print("Currency History: ")
                for result in currency_history:
                    print(result)
            break
        else:
            continue


Program()
    

   

    
    

    
