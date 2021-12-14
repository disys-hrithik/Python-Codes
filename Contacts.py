​class​ ​Mobcontacts​:                                                                                    
 ​     
 ​    ​def​ ​_init_​(​self​,​Fname​,​Lname​,​P_num​):                              
 ​        ​self​.​fn=​Fname 
 ​        ​self​.​ln​=​Lname 
 ​        ​self​.​pnr=​P_num
 ​         
 ​         
 ​    def​ ​open_mobcontacts(​self​): 
 ​        ​print​(​"Mobile Contacts"​) 
 ​      
 #validation
 ​    ​def​ ​fn_verification​(​self​): 
 ​        ​if​ ​type​(​self​.​fn​) ​==​ ​str​: 
 ​            ​if​ ​len​(​self​.​fn​) ​<=​ ​15​:                                                                                 
 ​                ​print​(​"Fname verified"​) 
 ​            ​else​: 
 ​                ​raise​ ​ValueError​(​"Fname should contain <= 15 letters"​) 
 ​        ​else​: 
 ​            ​raise​ ​TypeError​(​"Fname should not contain any symbols"​) 
 ​         
 ​    ​def​ ​ln_verification​(​self​): 
 ​        ​if​ ​type​(​self​.​ln) ​==​ ​str​: 
 ​            ​if​ ​len​(​self​.​ln​) ​<=​ ​15​:                                                                                
 ​                ​print​(​"Lname verified"​) 
 ​            ​else​: 
 ​                ​raise​ ​ValueError​(​"Lname should contain <=15 letters"​) 
 ​        ​else​: 
 ​            ​raise​ ​TypeError​(​"Lname should not contain any symbols"​) 
 ​         
 ​    ​def​ ​pnr_verification​(​self​): 
 ​        ​if​ (​len​(​self​.​pnr​)​==​10​): 
 ​            ​if​ ​type​(​self​.​pnr​) ​==​ ​str​:                                                                             
 ​                ​print​(​"P_num verified"​) 
 ​            ​else​: 
 ​                ​raise​ ​TypeError​(​"P_num should contain only integers "​) 
 ​        ​else​: 
 ​            ​raise​ ​ValueError​(​"P_num should be = 10 digits"​)
