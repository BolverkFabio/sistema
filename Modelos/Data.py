from datetime import datetime


class datas():

    
    def dataAtual(self):
        dataAgora = datetime.now() 
        dataAgora = dataAgora.strftime("%d/%m/%Y - %H:%M")
        
        return dataAgora
        
    

        #print(dataAgora)
        

