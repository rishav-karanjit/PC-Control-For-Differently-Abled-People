class GreetMe:
    def Welcome(self,name):
        if name: 
            return "Welcome back " + name + ". How may I help you today?" 
        else:
            return "Hello I am your virtual assistant.\nI will be helping you in controlling the PC.\nCan I know your name?"

    def Ans_Yes(self):
        return "Yes I can"