class Truss:
    def __init__(self):
        # ----------------------
        # Propriedade do pontos
        # -----------------------
        self.Xpositions = []
        self.Ypositions = []
        self.Zpositions = []
        self.pointID = []
        self.flag = False

        # --------------------------
        #   Propriedades das forças
        # ---------------------------
        self.ForcesID = []
        self.Forcesx = []
        self.Forcesy = []
        self.Forcesz = []
        self.flag_forces = False
        self.flagCalc = False
        # ----------------------------------
        #     Propriedades dos membros
        # ----------------------------------
        self.Members = [[""], [""]]
        # armazena x1, x2
        self.MembersX = [[], []]
        # armazena y1, y2
        self.MembersY = [[], []]
        # armasena z1,z2
        self.MembersZ = [[], []]
        self.MembersID = ""
        self.flagM = False

        # -----------------------------
        #  Propriedades dos apoios
        # -----------------------------
        self.flag_s = False
        #               tipo x ponto
        '''      credo
        :d   
            0 - PINO 
            1 - Rolete 
            2 - engaste

            supportsID[0] tipo do apoio
            supportsID[1] onde ele está
        '''
        self.supportsID = [[], []]
        self.supportsPoints = []
    # ----------------------------
    #           Gets
    # ----------------------------
    def getFlagC(self):
            return self.flagCalc
    
    def getForceFlag(self):
        return self.flag_forces

    def getMembersX(self, i):
        if i >= 0:
            # return x1 and x2 (where the segment starts and finishes on x)
            return self.MembersX[0][i], self.MembersX[1][i]

    def getMembersY(self, i):
        if i >= 0:
            # return y1 and y2 (where the segment starts and finishes on y)
            return self.MembersY[0][i], self.MembersY[1][i]

    def getMembersZ(self, i):
        if i >= 0:
            return self.MembersZ[0][i], self.MembersZ[1][i]

    def getFlagM(self):
        return self.flagM

    def getFlag(self):
        return self.flag

    def getID(self):
        '''
        Retorna a lista de IDs de nós inseridos
        '''
        return self.pointID

    def IDp(self, i):
        if(i >= 0):
            return self.pointID[i]
        return 0

    def xp(self, i):
        if(i >= 0):
            return self.Xpositions[i]
        return 0

    def yp(self, i):
        if(i >= 0):
            return self.Ypositions[i]
        return 0

    def zp(self, i):
        if(i >= 0):
            return self.Zpositions[i]
        return 0
    
    def fx(self,i):
        if i >= 0:
            return self.Forcesx[i]
        return 0

    def fy(self,i):
        if i>= 0:
            return self.Forcesy[i]
        return 0

    def fz(self,i):
        if i>= 0:
            return self.Forcesz[i]
        return 0

    def getXpositions(self):
        return self.Xpositions

    def getYpositions(self):
        return self.Ypositions

    def getZpositions(self):
        return self.Zpositions

    def getForcesID(self):
        return self.ForcesID

    def getForcesx(self):
        return self.Forcesx

    def getForcesy(self):
        return self.Forcesy

    def getForcesz(self):
        return self.Forcesz

    def getMembers(self):
        return self.Members

    def getMembersid(self, i):
        if i >= 0:
            return self.MembersID
        return 0
    
    def getZpositionSum(self):
        '''
        Get para a soma das posições z dos pontos,
        que será utilizado como um seletor para uma versão do código em 2d e outra em 3d no solver
        '''
        return sum(self.Zpositions)
    def getSupports(self):
        return self.supportsPoints

    # ----------------------------
    #           Sets
    # ----------------------------
    def setflaCalc(self,state: bool):
        self.flagCalc = state
    def setSupportsFlag(self, state: bool):
        self.flag_s = state

    def setForcesFlag(self, state: bool):
        self.flag_forces = state

    def setFlagM(self, state: bool):
        self.flagM = state

    def setFlag(self, state: bool):
        self.flag = state

    def setID(self, id):
        self.pointID.append(id)

    def setXpositions(self, x: float):
        print("Voce colocou x")
        self.Xpositions.append(x)
        print(self.Xpositions)

    def setYpositions(self, y: float):
        self.Ypositions.append(y)

    def setZpositions(self, z: float):
        self.Zpositions.append(z)

    def setForcesID(self, id):
        self.ForcesID.append(id)

    def setForcesx(self, x: int):
        self.Forcesx.append(x)

    def setForcesy(self, y: int):
        self.Forcesy.append(y)

    def setForcesz(self, z: int):
        self.Forcesz.append(z)

    def setMembers(self, nodeA: str, nodeB: str):
        '''
        cria um membro entre as entrada nodeA e nodeB
        nodeA: str -- nome do node
        nodeB: str -- nome do node
        '''
        self.Members[0].append(nodeA)
        self.Members[1].append(nodeB)

    def setMembersX(self, x1, x2):
        # função vai devolver a posição de x1 e x2 para o plot no graphWidget
        print("debug, amanda NAO eh corna")
        print(x1, x2)
        print(self.Xpositions)
        self.MembersX[0].append(self.Xpositions[x1])
        self.MembersX[1].append(self.Xpositions[x2])

    def setMembersY(self, y1, y2):
        # função vai devolver a posição y1 e y2 para o plot no graphWidget
        self.MembersY[0].append(self.Ypositions[y1])
        self.MembersY[1].append(self.Ypositions[y2])

    def setMembersZ(self, z1, z2):
        # função vai devole a posição z1 e z2 para o plot no graphWidget
        self.MembersZ[0].append(self.Zpositions[z1])
        self.MembersZ[1].append(self.Zpositions[z2])

    def setMembersID(self, id):
        self.MembersID = id

    def setSupports(self, type, id):
        # id é referente ao ponto que o suporte esta
        if(type == "pino"):
            self.supportsID[0].append(0)
            self.supportsID[1].append(id)
        elif(type == "rolete"):
            self.supportsID[0].append(1)
            self.supportsID[1].append(id)
        elif(type == "engaste"):
            self.supportsID[0].append(2)
            self.supportsID[1].append(id)

    # função que vai devolver as coordenadas de um ponto baseado no id
    def get_coordinates(self, ID):
        try:
            x = self.Xpositions[ID]
            y = self.Ypositions[ID]
            z = self.Zpositions[ID]
            return x, y, z
        except:
            return None
        
