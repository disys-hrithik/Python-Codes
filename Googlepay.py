class​ ​Googlepay​:                                                                                    
 ​     
 ​    ​def​ ​_init_​(​self​,​E_mail​,​P_num​,​Name​):                                                                  
 ​        ​self​.​emailid​=​E_mail
 ​        ​self​.​mobile​=​P_num 
 ​        ​self​.​name​=​Name 
 ​         
 ​    ​def​ ​open_gpay​(​self​): 
 ​        ​print​(​"Google Pay"​) 
 ​         
 ​    ​def​ ​email_verification​(​self​): 
 ​        ​if​ ​type​(​self​.​emailid​) ​==​ ​str​:                                                                                
 ​            ​if​ ​len​(​self​.​emailid​) ​<=​ ​35​:                                                                               
 ​                ​print​(​"email_id verified"​) 
 ​            ​else​: 
 ​                ​raise​ ​ValueError​(​"the emailid should contain < 35 values"​) 
 ​        ​else​: 
 ​            ​raise​ ​TypeError​(​"invalid emailid"​) 
 ​    ​def​ ​mobile_verification​(​self​): 
 ​        ​if​ (​len​(​self​.​mobile​)​==​10​): 
 ​            ​if​ ​type​(​self​.​mobile​) ​==​ ​str​:                                                                            
 ​                ​print​(​"phone number verified"​) 
 ​            ​else​: 
 ​                ​raise​ ​TypeError​(​"the phone number should contain only integers "​) 
 ​        ​else​: 
 ​            ​raise​ ​ValueError​(​"the phone number should be = 10 digits"​) 
 ​         
 ​    ​def​ ​name_verification​(​self​): 
 ​        ​if​ ​type​(​self​.​name​) ​==​ ​str​: 
 ​            ​if​ ​len​(​self​.​name​) ​<=​ ​25​:                                                                                 
 ​                ​print​(​"name verified"​) 
 ​            ​else​: 
 ​                ​raise​ ​ValueError​(​"The name should contain <= 25 characters"​) 
 ​        ​else​: 
 ​            ​raise​ ​TypeError​(​"The name should contain letters only"​) 
  
 ​    ​def​ ​otp_verification​(​self​,​code​,​otp​): 
 ​        ​if​(​otp​==​code​): 
 ​            ​print​(​"otp verified"​) 
 ​        ​else​: 
 ​            ​raise​ ​ValueError​(​"Incorrect OTP"​) 
  
 ​    ​def​ ​Bank_verification​(​self​): 
 ​        ​self​.​account_number​=​"62423489087" 
 ​        ​if​ (​len​(​self​.​account_number​) ​==​ ​12​): 
 ​            ​print​(​"Account number verified"​) 
 ​        ​else​: 
 ​            ​raise​ ​ValueError​(​"Inavlid Account number")



 ​import​ ​Googlepay 
  
 ​Hrithik=​googlepay​.​Google_pay​(​"Hrithik.thirugnanam@gmail.com"​,​"9500740108"​,​"Hrithik_Baarathi"​) 
 ​Hrithik.​open_gpay​() 
 ​Hrithik.​email_verification​() 
 ​Hrithik.​mobile_verification​() 
 ​Hrithik.​name_verification​() 
 ​Hrithik.​otp_verification​(​675847​,​675847​) 
 ​Hrithik.​Bank_verification​() 
 ​Hrithik.​PanCard_Verification​() 
 ​Hrithik.​set_Pin​(​"2000"​) 
 ​Hrithik.​Enter_your_Pin​(​2000​,​2000​) 
  
 ​class​ ​Phone_pe​(​googlepay​.​Google_pay​):                                                                                           
 ​    ​def​ ​_init_​(​self​,​Email_ID​,​Phone_number​,​Name​): 
 ​        ​super​().​_init_​(​Email_ID​,​Phone_number​,​Name​) 
  
 ​    ​def​ ​open_phonepe​(​self​): 
 ​        ​print​(​"Phone pe"​) 
 ​         
 ​HB=​Phone_pe​(​"Hrithik. Thirugnanam@gmail.com"​,​"9500740108"​,​"Hrithik_Baarathi"​) 
 ​HB.​open_phonepe​() 
 ​HB.​mobile_verification​() 
 ​HB.​name_verification​() 
 ​HB.​otp_verification​(​860695​,​860695​) 
 ​HB.​Bank_verification​() 
 ​HB.​PanCard_Verification​() 
 ​HB.​set_Pin​(​"2000"​) 
 ​HB.​Enter_your_Pin​(​2000​,​20020) 
  
 ​         
 ​googlepay​=​[{​"name"​:​"Hrithik"​,​"num"​:​9500740108​,​"type"​:​"personal"​,​"trans"​:​"regular"​},                      
 ​                  {​"name"​:​"Saravana"​,​"num"​:​8825555140​,​"type"​:​"personal"​,​"trans"​:​"regular"​}, 
 ​                  {​"name"​:​"JK"​,​"num"​:​9600114878​,​"type"​:​"personal"​,​"trans"​:​"rare"​}, 
 ​                  {​"name"​:​"Aftab"​,​"num"​:​9360763652​,​"type"​:​"personal"​,​"trans"​:​"never"​}, 
 ​                  {​"name"​:​"Arul"​,​"num"​:​8596266985​,​"type"​:​"personal"​,​"trans"​:​"rare"​}, 
 ​                  {​"name"​:​"Aarthi"​,​"num"​:​9597916931​,​"type"​:​"personal"​,​"trans"​:​"rare"}]

for j,k in i.items():
    print(f"{j}:{k}")
