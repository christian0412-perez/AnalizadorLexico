class gramatica:

    def __init__(self):
        self.l={}
        self.letras =f"[a-zA-Z]"
        self.id=f"^\({{1}}{self.letras}*\){{1}}"
        self.reserved=["tabla","crear","agregar","foranea","en tabla","de tabla","con"]
        self.simbols=["\(","\)","\;","\.","\,"]
        self.tokens=["T","CR","A","FO","ET","DT","CON","PA","PC","PUC","P","CO"]
        # self.qf = f"\{self.a,self.fo,self.pa,self.id,self.pc,self.f}"
        # self.qc = f"\{self.cr,self.t,self.pa,self.id,self.pc,self.c}"
        # self.i = f"\{self.qc}\{self.puc}\{self.rr}"
        # self.sh = f".start\{self.pa}\{self.pc}"