atm_card=input("enter atm card")
if atm_card=="Right_side" or atm_card=="right_side":
    language=input("enter language")
    if language=="English" or language=="Hindi":
        pin=int(input("enter pin"))
        if pin>=1000 and pin<=9999:
            transaction_type=input("enter transaction_type")
            if transaction_type=="Withdrawal" or transaction_type=="withdrawal":
                amount=int(input("enter amount"))
                key_name=input("enter key")
                if amount>=500 and amount<=20000 and amount%500==0:
                    a=amount//2000
                    b=amount%2000
                    c=b//500
                    d=b%500
                    print("notes of 2000",a,"notes of 500",c)
                    money_reciept=input("enter money reciept")
                    if money_reciept=="yes" or money_reciept=="no":
                        print("money_reciept")
                    else:
                        print("thanks for transaction")
                else:
                    print("limited amount")
            elif transaction_type=="balance enquiry" or transaction_type=="Blance enquiry":
                account_type=input("enter account type")
                key_name=input("enter key")
                if key_name=="ok" or key_name=="Ok":
                    print("thanks for enquiry")
                else:
                    print("invalid key")
            elif transaction_type=="Deposit money" or transaction_type=="deposit money":
                account_no=int(input("enter account no"))
                if account_no>=1000000000 and account_no<=999999999:
                    bill_amt=int(input("enter bill amt"))
                    if bill_amt>=1000000000 and bill_amt<=999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter ok")
                        if key_name=="ok" or key_name=="Ok":
                            print("succesful")
                        else:
                            print("unsuccesful")    
            elif transaction_type=="Bill_payment" or transaction_type=="bill_payment":
                account_no=int(input("enter account no"))
                if account_no>=1000000000 and account_no<=999999999:
                    bill_id=int(input("enter bill id"))
                    if bill_id>=1000000000 and bill_id<=999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter ok")
                        print("succesful")
                    else:
                        print("unsuccesful")
                else:
                    print("not succesful")
            else:
                print("invalid pin")
        else:
            print("enter valid language")
    else:
        print("rejected")                                                    