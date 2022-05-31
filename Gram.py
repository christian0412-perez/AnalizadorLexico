class gramatica:

    def __init__(self):
        self.l={}
        self.letras =f"[a-z]"
        self.id=f"{self.letras}*"
        self.reserved=["EN TABLA","DE TABLA","CREAR","AGREGAR","FORANEA","Tabla","CON"]
        self.simbols2=["\-","\_","[0-9]","\+","\{","\}"]
        self.simbols=["\(","\)","\;","\.","\,"]
        self.tokens=["ET","DT","CR","A","FO","T","CON","PA","PC","PUC","P","CO"]
        # self.qf = f"\{self.a,self.fo,self.pa,self.id,self.pc,self.f}"
        # self.qc = f"\{self.cr,self.t,self.pa,self.id,self.pc,self.c}"
        # self.i = f"\{self.qc}\{self.puc}\{self.rr}"
        # self.sh = f".start\{self.pa}\{self.pc}"