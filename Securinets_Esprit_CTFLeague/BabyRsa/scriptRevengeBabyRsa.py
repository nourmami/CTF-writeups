from Crypto.Util.number import *
import json

Flag = b"Securinets{REDACTED}"
welcome_Msg = "Like usual I encrypted the flag and I will give you my parameters with a lil Hint :3"



class Challenge():
    def __init__(self):
        self.p = getPrime(1024)
        self.q = getPrime(1024)
        self.n = self.p*self.q
        self.e = 65537
        assert(GCD(self.e,(self.p-1)*(self.q-1)) == 1)
        print(welcome_Msg)
        print("encrypted_Flag : ", hex(pow(bytes_to_long(Flag),self.e,self.n)))
        print("N : ",hex(self.n))
        print("e : ",hex(self.e))


    def Challenge(self,your_input):
        if 'X' not in your_input:
            return {"error": "Sorry Can't find X in your input :("}
        x = int(your_input['X'])
        if (x<3):
            return {"error": "X must be superior to 2"}
        if (x>20):
            return {"error": "X is too big "}    
        return (f"My lil hint is p**{x} - q**{x} : " + str(hex(self.p**x - self.q**x)))



if (__name__ == "__main__") :
    try : 
        challenge = Challenge()
        inp = json.loads(input(("Give an integer X  (X > 2) and I will return (p^x - q^x) but this time only ONE VALUE is permitted\n")))
        print(challenge.Challenge(inp))
        print("That's All Folkssss byeeeee :)")
        exit(0)
    except:
        print("Make sure to read the source code Carefuulllyyyy :)")
        exit(0)