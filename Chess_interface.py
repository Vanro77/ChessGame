from tkinter import *
from tkinter import messagebox


class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title('Échecs')
        self.root.geometry("1080x840")
        self.root.minsize(720, 720)
        self.root.iconbitmap('Ressources\chess.ico')
        self.newgame = Button(self.root, command=self.initialise, text='Nouvelle partie')
        self.frame_black = Frame(self.root)
        self.entry_black = Button(self.frame_black, text='->', bg='#008080', command=self.mouvement_noir)
        self.b1 = StringVar()
        self.b2 = StringVar()
        self.Move_black1 = Entry(self.frame_black, textvariable=self.b1)
        self.Move_black2 = Entry(self.frame_black, textvariable=self.b2)
        self.frame_white = Frame(self.root)
        self.entry_white = Button(self.frame_white, text='->', bg='#E0FFFF', command=self.mouvement_blanc)
        self.w1 = StringVar()
        self.w2 = StringVar()
        self.Move_white1 = Entry(self.frame_white, textvariable=self.w1)
        self.Move_white2 = Entry(self.frame_white, textvariable=self.w2)
        self.table = Frame(self.root)
        self.entry_black.grid(column=2, row=1)
        self.Move_black1.grid(column=1, row=1)
        self.Move_black2.grid(column=3, row=1)
        self.entry_white.grid(column=2, row=1)
        self.Move_white1.grid(column=1, row=1)
        self.Move_white2.grid(column=3, row=1)
        self.newgame.pack()
        self.frame_black.pack(side=TOP)
        self.table.pack(expand=1)
        self.frame_white.pack(side=BOTTOM)
        self.pionnoir = PhotoImage(file='Ressources/pionnoir.gif')
        self.founoir = PhotoImage(file='Ressources/founoir.gif')
        self.foublanc = PhotoImage(file='Ressources/foublanc.gif')
        self.cavalierblanc = PhotoImage(file='Ressources/cavalierblanc.gif')
        self.cavaliernoir = PhotoImage(file='Ressources/cavaliernoir.gif')
        self.pionnoir = PhotoImage(file='Ressources/pionnoir.gif')
        self.pionblanc = PhotoImage(file='Ressources/pionblanc.gif')
        self.roiblanc = PhotoImage(file='Ressources/roiblanc.gif')
        self.roinoir = PhotoImage(file='Ressources/roinoir.gif')
        self.tournoir = PhotoImage(file='Ressources/tournoir.gif')
        self.tourblanc = PhotoImage(file='Ressources/tourblanc.gif')
        self.reineblanc = PhotoImage(file='Ressources/reineblanc.gif')
        self.reinenoir = PhotoImage(file='Ressources/reinenoir.gif')
        self.listenoir = {}
        self.listeblanc = {}

    def construction(self):
        colonne = 0
        for i in range(8):
            ligne = 1
            colonne += 1
            case = Label(self.table,  padx=24, pady=22, text='{}{}'.format(ligne, colonne))
            if i % 2 == 0:
                case['bg'] = '#008080'
            else:
                case['bg'] = '#E0FFFF'
            case.grid(column=colonne, row=ligne)
            for j in range(7):
                ligne += 1
                case2 = Label(self.table, padx=24, pady=22, text='{}{}'.format(ligne, colonne))
                if i % 2 != 0:
                    if j % 2 == 0:
                        case2['bg'] = '#008080'
                    else:
                        case2['bg'] = '#E0FFFF'
                else:
                    if j % 2 != 0:
                        case2['bg'] = '#008080'
                    else:
                        case2['bg'] = '#E0FFFF'
                case2.grid(column=colonne, row=ligne)

    def initialise(self):
        for casei in self.table.grid_slaves():
            if casei['text'] in ['13', '16']:
                casei['image'] = self.founoir
                self.listenoir['fou'] = casei['image']
            elif casei['text'] in ['11', '18']:
                casei['image'] = self.tournoir
                self.listenoir['tour'] = casei['image']
            elif casei['text'] == '14':
                casei['image'] = self.reinenoir
                self.listenoir['reine'] = casei['image']
            elif casei['text'] == '15':
                casei['image'] = self.roinoir
                self.listenoir['roi'] = casei['image']
            elif casei['text'][0] == '2':
                casei['image'] = self.pionnoir
                self.listenoir['pion'] = casei['image']
            elif casei['text'] in ['12', '17']:
                casei['image'] = self.cavaliernoir
                self.listenoir['cavalier'] = casei['image']
            elif casei['text'] in ['83', '86']:
                casei['image'] = self.foublanc
                self.listeblanc['fou'] = casei['image']
            elif casei['text'] in ['81', '88']:
                casei['image'] = self.tourblanc
                self.listeblanc['tour'] = casei['image']
            elif casei['text'] == '84':
                casei['image'] = self.reineblanc
                self.listeblanc['reine'] = casei['image']
            elif casei['text'] == '85':
                casei['image'] = self.roiblanc
                self.listeblanc['roi'] = casei['image']
            elif casei['text'][0] == '7':
                casei['image'] = self.pionblanc
                self.listeblanc['pion'] = casei['image']
            elif casei['text'] in ['82', '87']:
                casei['image'] = self.cavalierblanc
                self.listeblanc['cavalier'] = casei['image']
            else:
                casei['image'] = ''
        self.entry_black['state'] = DISABLED
        self.entry_white['state'] = NORMAL

    def mouvement_noir(self):
        b1 = self.Move_black1.get()
        b2 = self.Move_black2.get()
        if int(b1) in range(11, 89) and int(b2) in range(11, 89):
            liste_de_mouvement = []
            for casei in self.table.grid_slaves():
                if casei['image'] in self.listenoir.values():
                    if casei['text'] == b1:
                        liste_de_mouvement.append(casei)
            for casei in self.table.grid_slaves():
                if liste_de_mouvement != [] and casei['image'] not in self.listenoir.values():
                    if casei['text'] == b2:
                        liste_de_mouvement.append(casei)
            if len(liste_de_mouvement) == 2:
                if self.contrainte_de_déplacement(liste_de_mouvement[0], liste_de_mouvement[1]) is True:
                    liste_de_mouvement[1]['image'] = liste_de_mouvement[0]['image']
                    liste_de_mouvement[0]['image'] = ''
                    self.entry_black['state'] = DISABLED
                    self.entry_white['state'] = NORMAL

    def mouvement_blanc(self):
        w1 = self.Move_white1.get()
        w2 = self.Move_white2.get()
        if int(w1) in range(11, 89) and int(w2) in range(11, 89):
            liste_de_mouvement = []
            for casei in self.table.grid_slaves():
                if casei['image'] in self.listeblanc.values():
                    if casei['text'] == w1:
                        liste_de_mouvement.append(casei)
            for casei in self.table.grid_slaves():
                if liste_de_mouvement != [] and casei['image'] not in self.listeblanc.values():
                    if casei['text'] == w2:
                        liste_de_mouvement.append(casei)
            if len(liste_de_mouvement) == 2:
                if self.contrainte_de_déplacement(liste_de_mouvement[0], liste_de_mouvement[1]) is True:
                    liste_de_mouvement[1]['image'] = liste_de_mouvement[0]['image']
                    liste_de_mouvement[0]['image'] = ''
                    self.entry_white['state'] = DISABLED
                    self.entry_black['state'] = NORMAL
                else:
                    messagebox.showerror('Erreur', 'Mouvement Impossible')

    def contrainte_de_déplacement(self, pointa, pointb):
        if pointa['image'] == self.listenoir['pion']:
            if pointb['image'] == '':
                if int(pointa['text']) in [21, 22, 23, 24, 25, 26, 27, 28]:
                    if int(pointb['text']) - int(pointa['text']) == 20:
                        return True
                if int(pointb['text']) - int(pointa['text']) == 10:
                    return True
                return False
            if pointb['image'] in self.listeblanc.values():
                if int(pointb['text'][0]) - int(pointa['text'][0]) == 1:
                    if abs(int(pointb['text'][1]) - int(pointa['text'][1])) == 1:
                        return True
                return False
        if pointa['image'] == self.listeblanc['pion']:
            if pointb['image'] == '':
                if int(pointa['text']) in [71, 72, 73, 74, 75, 76, 77, 78]:
                    if int(pointb['text']) - int(pointa['text']) == -20:
                        return True
                if int(pointb['text']) - int(pointa['text']) == -10:
                    return True
                return False
            if pointb['image'] in self.listenoir.values():
                if int(pointb['text'][0]) - int(pointa['text'][0]) == -1:
                    if abs(int(pointb['text'][1]) - int(pointa['text'][1])) == 1:
                        return True
                return False
        if pointa['image'] == self.listeblanc['fou']:
            if pointb['image'] == '':
                if abs(int(pointb['text'][0]) - int(pointa['text'][0])) == abs(int(pointb['text'][1]) - int(pointa['text'][1])):
                    return True
                return False






Mon_echequier = Interface()
Mon_echequier.construction()
Mon_echequier.initialise()
Mon_echequier.root.mainloop()
