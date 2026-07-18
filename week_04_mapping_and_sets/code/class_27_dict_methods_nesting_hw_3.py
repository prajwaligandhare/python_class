# 2 users ka nested dict banao aur dono ke naam print karo.


users = {
            
                "user_1":{"name": "raj", "id": 121, "ofc": "xyz"},
                         
            
            
                 "user_2":{"name": "sanju", "id": 123, "ofc": "wxz"},
                        

        }

print(users["user_1"]["name"])
print(users["user_2"]["name"])



#output: raj
 #       sanju