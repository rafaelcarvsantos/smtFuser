# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:06:53 2019

@author: Rafael
"""
from bisect import *
import math
import json
import itertools
import codecs
from bs4 import BeautifulSoup
import pandas as pd
from tkintertable import TableCanvas, TableModel
from tkinter import *
from tkinter import StringVar, Entry, Frame, Listbox, Scrollbar
from tkinter.constants import *


resultados={}
fusoesEspeciais=['Morax',
'High Pixie',
'Mitra',
'Anahita',
'Black Frost',
'Horkos',
'Frost Ace',
'Kurama Tengu',
'King Frost',
'Asura',
'Ishtar',
'Ouroboros',
'Moloch',
'Mithra',
'Orcus',
'Forneus',
'Asherah',
'Tiamat',
'Ongyo-Ki',
'Isis',
'Zeus',
'Maya',
'Volvo',
'Norn',
'Maria',
'Shaytan',
'Armaiti',
'Cybele',
'Huang Long',
'Amon',
'Anat',
'Zaou-Gongen',
'Mastema',
'Sandalphon',
'Alilat',
'Demeter',
'Kali',
'Seraph',
'Mother Harlot',
'Shiva',
'Masakado',
'Demiurge',
'Beelzebub',
'Belial',
'Lucifuge',
'Nebiros']

relacaoFusaoEspecial=[{'nome': 'Morax', 'ingredientes': ['Oni', 'Melchom', 'Itsumade']},
{'nome': 'High Pixie', 'ingredientes': ['Pixie', 'Lilim', 'Harpy']},
{'nome': 'Mitra', 'ingredientes': ['Ippon-Datara', 'Fomorian', 'Bifrons']},
{'nome': 'Anahita', 'ingredientes': ['Power', 'Jack Frost', 'Azumi']},
{'nome': 'Black Frost', 'ingredientes': ['Jack Frost', 'Fairy Pyro Jack', 'Incubus']},
{'nome': 'Horkos', 'ingredientes': ['Doppelganger', 'Momunofu', 'Macabre']},
{'nome': 'Frost Ace', 'ingredientes': ['Jack Frost', 'Tam Lin', 'Power']},
{'nome': 'Kurama Tengu', 'ingredientes': ['Koppa Tengu', 'Karasu Tengu']},
{'nome': 'King Frost', 'ingredientes': ['Jack Frost', 'Black Frost', 'Frost Ace']},
{'nome': 'Asura', 'ingredientes': ['Pisaca', 'Kwancha', 'Orias']},
{'nome': 'Ishtar', 'ingredientes': ['Skogsra', 'Virtue', 'Churel']},
{'nome': 'Ouroboros', 'ingredientes': ['Dzelarhons', 'Kwancha', 'Wood Mandrake', 'Basilisk', 'Vouivre']},
{'nome': 'Moloch', 'ingredientes': ['Morax', 'Ose']},
{'nome': 'Mithra', 'ingredientes': ['Mitra', 'Inti']},
{'nome': 'Orcus', 'ingredientes': ['Horkos', 'Hel']},
{'nome': 'Forneus', 'ingredientes': ['Decarabia', 'Kikuri-Hime', 'Sui-Ki']},
{'nome': 'Asherah', 'ingredientes': ['Asura', 'Valkyrie']},
{'nome': 'Tiamat', 'ingredientes': ['Tlaltecuhtli', 'Mushussu', 'Kingu', 'Pabilsag']},
{'nome': 'Ongyo-Ki', 'ingredientes': ['Kin-Ki', 'Fuu-Ki', 'Sui-Ki']},
{'nome': 'Isis', 'ingredientes': ['Persephone', 'Rukh', 'Hathor']},
{'nome': 'Zeus', 'ingredientes': ['Hunt', 'Oberon', 'Anzu', 'Throne']},
{'nome': 'Maya', 'ingredientes': ['Hariti', 'Succubus', 'Incubus', 'Airavata']},
{'nome': 'Volvo', 'ingredientes': ['Titania', 'Diana', 'Strigoii']},
{'nome': 'Norn', 'ingredientes': ['Clotho', 'Lachesis', 'Atropos']},
{'nome': 'Maria', 'ingredientes': ['Black Maria', 'Pallas Athena']},
{'nome': 'Shaytan', 'ingredientes': ['Cerberus', 'Harpy']},
{'nome': 'Armaiti', 'ingredientes': ['Gemori', 'Haoma', 'Hariti']},
{'nome': 'Cybele', 'ingredientes': ['Tlazolteotl', 'Xiuhtecuhtli', 'Anzu']},
{'nome': 'Huang Long', 'ingredientes': ['Baihu', 'Feng Huang', 'Long', 'Gui Xian']},
{'nome': 'Amon', 'ingredientes': ['Sphinx', 'Dantalian', 'Orias']},
{'nome': 'Anat', 'ingredientes': ['Tzitzimitl', 'Ishtar']},
{'nome': 'Zaou-Gongen', 'ingredientes': ['Ongyo-Ki', 'Yatagarasu', 'Koumokuten']},
{'nome': 'Mastema', 'ingredientes': ['Abaddon', 'Cherub', 'Throne']},
{'nome': 'Sandalphon', 'ingredientes': ['Aniel', 'Kazfiel']},
{'nome': 'Alilat', 'ingredientes': ['Peri', 'Azrael', 'Israfel']},
{'nome': 'Demeter', 'ingredientes': ['Quetzalcoatl', 'Mayahuel', 'Anahita']},
{'nome': 'Kali', 'ingredientes': ['Ixtab', 'Dakini', 'Parvati']},
{'nome': 'Seraph', 'ingredientes': ['Angel', 'Archangel', 'Principality', 'Power', 'Virtue', 'Dominion', 'Throne', 'Cherub']},
{'nome': 'Mother Harlot', 'ingredientes': ['White Rider', 'Red Rider', 'Black Rider', 'Pale Rider']},
{'nome': 'Shiva', 'ingredientes': ['Barong', 'Rangda']},
{'nome': 'Masakado', 'ingredientes': ['Hachiman','Bishamonten', 'Zouchouten', 'Koumokuten','Jikokuten']},
{'nome': 'Demiurge', 'ingredientes': ['Hachiman', 'Metatron', 'Samael']},
{'nome': 'Beelzebub', 'ingredientes': ['Seth', 'Abaddon']},
{'nome': 'Belial', 'ingredientes': ['Samael', 'Cherub']},
{'nome': 'Lucifuge', 'ingredientes': ['Mot', 'Alciel']},
{'nome': 'Nebiros', 'ingredientes': ['Nergal', 'Omoteotl']}]


fusaoPrime=pd.read_csv('fusaoPrime.csv')
fusaoPrime=fusaoPrime.set_index("Tribo")
f=codecs.open("Fusion chart - SMT Strange Journey.html", 'r', 'utf-8')
document= BeautifulSoup(f.read(),'html.parser')
trs=document.find_all("tr")
l=[]
for i in trs[0]:
    if i.string.rstrip() != "":
        l.append(i.string.rstrip())
        
df = pd.DataFrame(
    columns=l
)


for o in range(41):
    lista1=[]
    lista=document.find_all("tr")[o]
    for i in lista:
        try:
            if i.string.rstrip() != "":
                lista1.append(i.string.rstrip())
        except:
            lista1.append("-")
    df = df.append(pd.Series(lista1, index=df.columns ), ignore_index=True)
    
df=df.set_index("Tribe")
df.loc["Brute","Fallen"]="Night"

        

listaPossiveisMonstros=[]
listadeMonstrosTipoCerto=[]
jsonTodos=[]

count = 8


def fusaoEspecial(nomes):
    for i in relacaoFusaoEspecial:
        if set(i['ingredientes']).issubset(nomes):
            nomesBonitos=""
            with open('compendiumSJ.json', encoding="utf8") as json_file:  
                data = json.load(json_file)
                for n in data:
                    if n["nameEN"]==i['nome']:
                        listaPossiveisMonstros.append(n["nameEN"])
                        m=n
                        for k in range(0,len(i['ingredientes'])):
                            if k != len(i['ingredientes'])-1:
                                nomesBonitos=nomesBonitos+i['ingredientes'][k]+"+"
                            if k == len(set(i['ingredientes']))-1:
                                nomesBonitos=nomesBonitos+i['ingredientes'][k]
                        m["Origin"]=nomesBonitos
                        jsonTodos.append(m)

def FusaoPrime(tribo1,level1,nome1,tribo2,level2,nome2):
    with open('compendiumSJ.json', encoding="utf8") as json_file:  
        data = json.load(json_file)
    listadeMonstrosTipoCerto=[]
    nomedosMonstros=[]
    if tribo1 == 'Prime' and tribo2 != 'Prime':
        fusao = tribo2
        tribo1 = nome1
        levelCerto=level2

    if tribo2 == 'Prime' and tribo1 != 'Prime':
        fusao = tribo1
        tribo2 = nome2
        levelCerto = level1

    try:
        primeResult=fusaoPrime.loc[tribo1][tribo2]

    except:
        primeResult=fusaoPrime.loc[tribo2][tribo1]

    for n in data:
        if n["Race"]==fusao:
            listadeMonstrosTipoCerto.append(int(n["level"]))
            nomedosMonstros.append(n["nameEN"])
    listadeMonstrosTipoCerto.sort()
    d=int(math.trunc((int(level1)+int(level2))/2)+1)
    nivelcerto= int(listadeMonstrosTipoCerto[bisect_right(listadeMonstrosTipoCerto, int(d))])

    if primeResult == '+1':
        nivelreal=listadeMonstrosTipoCerto[listadeMonstrosTipoCerto.index(int(levelCerto))+1]
    elif primeResult == '+2':
        nivelreal=listadeMonstrosTipoCerto[listadeMonstrosTipoCerto.index(int(levelCerto))+2]
    elif primeResult == '-1':
        nivelreal=listadeMonstrosTipoCerto[listadeMonstrosTipoCerto.index(int(levelCerto))-1]
    elif primeResult == '-':
        return


    with open('compendiumSJ.json', encoding="utf8") as json_file:  
        data = json.load(json_file)
        for n in data:
            if n["Race"]==fusao and int(n["level"])==nivelreal:
                listaPossiveisMonstros.append(n["nameEN"])
                m=n    
                m["Origin"]=nome1+"+"+nome2
                jsonTodos.append(m)
                


        

def Fusao(tribo1,level1,nome1,tribo2,level2,nome2):
    listadeMonstrosTipoCerto=[]
    nomedosMonstros=[]
    fusao = df.loc[tribo1,tribo2]
    if fusao == "-":
        fusao = df.loc[tribo2,tribo1]
    if varUMA.get() == TRUE and fusao=='Beast':
        fusao = 'UMA'
    elif varFiend.get() == TRUE and fusao=='Genma':
        fusao = 'Fiend'
    elif varEnigma.get() == TRUE and fusao=='Deity':
        fusao = 'Enigma'


    
    with open('compendiumSJ.json', encoding="utf8") as json_file:  
        data = json.load(json_file)
        for n in data:
            if n["Race"]==fusao:
                listadeMonstrosTipoCerto.append(int(n["level"]))
                nomedosMonstros.append(n["nameEN"])
                
    
    listadeMonstrosTipoCerto.sort()
    d=int(math.trunc((int(level1)+int(level2))/2)+1)
    try:
        nivelcerto= int(listadeMonstrosTipoCerto[bisect_right(listadeMonstrosTipoCerto, int(d))])
    except:
        nivelcerto=listadeMonstrosTipoCerto[-1]
    with open('compendiumSJ.json', encoding="utf8") as json_file:  
        data = json.load(json_file)
        for n in data:
            if n["Race"]==fusao and int(n["level"])==nivelcerto:
                if n["nameEN"] in fusoesEspeciais:
                    return
                else:
                    listaPossiveisMonstros.append(n["nameEN"])
                    m=n
                    m["Origin"]=nome1+"+"+nome2
                    jsonTodos.append(m)
                


                    

def getMonstro(nome1,nome2):
    with open('compendiumSJ.json', encoding="utf8-") as json_file:  
        data = json.load(json_file)
        for n in data:
            if n["nameEN"]==nome1:
                tribo1=n["Race"]
                level1=n["level"]
            if n["nameEN"]==nome2:
                tribo2=n["Race"]
                level2=n["level"]
    if tribo1 == 'Prime' or tribo2 == 'Prime':
        try:
            FusaoPrime(tribo1,level1,nome1,tribo2,level2,nome2)
        except:
            return
    else:
        try:
            Fusao(tribo1,level1,nome1,tribo2,level2,nome2)
        except:
            return 
    
    
def fusion(*argv):
    jsonTodos.clear()
    nomes = []
    listaPossiveisMonstros.clear()
    for arg in argv:
        nomes.append(arg)
    fusaoEspecial(nomes)
    if var.get() == 'one':
        for pair in itertools.combinations(nomes,2):
            getMonstro(pair[0],pair[1])
            nomes=nomes+listaPossiveisMonstros
    if var.get() == 'two':
        for pair in itertools.combinations(nomes,2):
            getMonstro(pair[0],pair[1])
            nomes=nomes+listaPossiveisMonstros
            nomes = list(dict.fromkeys(nomes))
        for pair in itertools.combinations(nomes,2):
            getMonstro(pair[0],pair[1])
    if var.get() =='three':
        for pair in itertools.combinations(nomes,2):
            getMonstro(pair[0],pair[1])
            nomes=nomes+listaPossiveisMonstros
            nomes = list(dict.fromkeys(nomes))
        for pair in itertools.combinations(nomes,2):
            getMonstro(pair[0],pair[1])
            nomes=nomes+listaPossiveisMonstros
            nomes = list(dict.fromkeys(nomes))
        for pair in itertools.combinations(nomes,2):
            getMonstro(pair[0],pair[1])
    novaJanela()
        
def fundir():
    listadeBotoes=[]
    listadeNomes=[]
    for i in root.winfo_children():
        if "!combobox_autocomplete" in str(i):
            listadeBotoes.append(i)
    for i in range(len(listadeBotoes)):
        if listadeBotoes[i].get() !="":
            listadeNomes.append(listadeBotoes[i].get())

    fusion(*listadeNomes)

def adicionarMonstro():
    global count
    count=count+1
    combobox_autocomplete = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete.grid(row=count-1,column=0,padx=5,pady=7)
    combobox_autocomplete2 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete2.grid(row=count-1,column=1,padx=5,pady=5)
    

def novaJanela():
    jafoi=[]
    global resultados
    global table
    resultados.clear()
    print(jsonTodos)
    tamanho=root.winfo_screenheight()
    for i in range(0,len(jsonTodos)):
        try:
            if jsonTodos[i]["Origin"] in jafoi:
                continue
            else:
                resultados.update({'rec'+str(i): {'Origin': jsonTodos[i]["Origin"],'Name': jsonTodos[i]["nameEN"], 'Alignment': jsonTodos[i]["Alignment"], 'Level': jsonTodos[i]["level"]
                ,'Phys': jsonTodos[i]["Phys"],'Gun': jsonTodos[i]["Gun"],
                'Fire': jsonTodos[i]["Fire"],'Ice': jsonTodos[i]["Ice"],'Elec': jsonTodos[i]["Elec"],
                'Wind': jsonTodos[i]["Wind"],'Light': jsonTodos[i]["Light"],'Dark': jsonTodos[i]["Dark"],
                'Skills': jsonTodos[i]["Skill1"]+" , "+jsonTodos[i]["Skill2"]+" , "+jsonTodos[i]["Skill3"],'DSkills':jsonTodos[i]["DS Skill1"] + ", "+ jsonTodos[i]["DS Skill2"]+", "+jsonTodos[i]["DS Skill3"],
                'HP': jsonTodos[i]["HP"],'MP': jsonTodos[i]["MP"],'St': jsonTodos[i]["St"],
                'Ma': jsonTodos[i]["Ma"],'Vi': jsonTodos[i]["Vi"],'Ag': jsonTodos[i]["Ag"],
                'Lu': jsonTodos[i]["Lu"]}})
                jafoi.append(jsonTodos[i]["Origin"])
        except:
            continue
    root2 = Tk()
    root2.focus_force()
    root2.geometry('%dx%d+%d+%d' % (1900, tamanho-300, 0, 0))
    root2.title('Fusion Results')
#    root2.geometry('1900x'+str(tamanho-300))
    tframe = Frame(root2)
    tframe.pack(expand=1,fill=BOTH)
    table = TableCanvas(tframe, data=resultados)
    table.adjustColumnWidths() 
    table.show()
    table.redraw()
    table=table.adjustColumnWidths()
    root.mainloop()
    
def clear():
    listadeBotoes=[]
    for i in root.winfo_children():
        if "!combobox_autocomplete" in str(i):
            listadeBotoes.append(i)
    for i in range(len(listadeBotoes)):
        listadeBotoes[i].delete(0,END)


#-----------------------------------------------------------------------------------------------------------------#
    
    # -*- GUI -*-


def autoscroll(sbar, first, last):
    """Hide and show scrollbar as needed."""
    first, last = float(first), float(last)
    if first <= 0 and last >= 1:
        sbar.grid_remove()
    else:
        sbar.grid()
    sbar.set(first, last)


class Combobox_Autocomplete(Entry, object):
    def __init__(self, master, list_of_items=None, autocomplete_function=None, listbox_width=None, listbox_height=7, ignorecase_match=False, startswith_match=True, vscrollbar=True, hscrollbar=True, **kwargs):
        if hasattr(self, "autocomplete_function"):
            if autocomplete_function is not None:
                raise ValueError("Combobox_Autocomplete subclass has 'autocomplete_function' implemented")
        else:
            if autocomplete_function is not None:
                self.autocomplete_function = autocomplete_function
            else:
                if list_of_items is None:
                    raise ValueError("If not guiven complete function, list_of_items can't be 'None'")

                if ignorecase_match:
                    if startswith_match:
                        def matches_function(entry_data, item):
                            return item.startswith(entry_data)
                    else:
                        def matches_function(entry_data, item):
                            return item in entry_data

                    self.autocomplete_function = lambda entry_data: [item for item in self.list_of_items if matches_function(entry_data, item)]
                else:
                    if startswith_match:
                        def matches_function(escaped_entry_data, item):
                            if re.match(escaped_entry_data, item, re.IGNORECASE):
                                return True
                            else:
                                return False
                    else:
                        def matches_function(escaped_entry_data, item):
                            if re.search(escaped_entry_data, item, re.IGNORECASE):
                                return True
                            else:
                                return False
                    
                    def autocomplete_function(entry_data):
                        escaped_entry_data = re.escape(entry_data)
                        return [item for item in self.list_of_items if matches_function(escaped_entry_data, item)]

                    self.autocomplete_function = autocomplete_function

        self._listbox_height = int(listbox_height)
        self._listbox_width = listbox_width

        self.list_of_items = list_of_items
        
        self._use_vscrollbar = vscrollbar
        self._use_hscrollbar = hscrollbar

        kwargs.setdefault("background", "white")

        if "textvariable" in kwargs:
            self._entry_var = kwargs["textvariable"]
        else:
            self._entry_var = kwargs["textvariable"] = StringVar()

        Entry.__init__(self, master, **kwargs)

        self._trace_id = self._entry_var.trace('w', self._on_change_entry_var)
        
        self._listbox = None

        self.bind("<Tab>", self._on_tab)
        self.bind("<Up>", self._previous)
        self.bind("<Down>", self._next)
        self.bind('<Control-n>', self._next)
        self.bind('<Control-p>', self._previous)

        self.bind("<Return>", self._update_entry_from_listbox)
        self.bind("<Escape>", lambda event: self.unpost_listbox())
        
    def _on_tab(self, event):
        self.post_listbox()
        return "break"

    def _on_change_entry_var(self, name, index, mode):
        
        entry_data = self._entry_var.get()

        if entry_data == '':
            self.unpost_listbox()
            self.focus()
        else:
            values = self.autocomplete_function(entry_data)
            if values:
                if self._listbox is None:
                    self._build_listbox(values)
                else:
                    self._listbox.delete(0, END)

                    height = min(self._listbox_height, len(values))
                    self._listbox.configure(height=height)

                    for item in values:
                        self._listbox.insert(END, item)
                
            else:
                self.unpost_listbox()
                self.focus()

    def _build_listbox(self, values):
        listbox_frame = Frame()

        self._listbox = Listbox(listbox_frame, background="white", selectmode=SINGLE, activestyle="none", exportselection=False)
        self._listbox.grid(row=0, column=0,sticky = N+E+W+S)

        self._listbox.bind("<ButtonRelease-1>", self._update_entry_from_listbox)
        self._listbox.bind("<Return>", self._update_entry_from_listbox)
        self._listbox.bind("<Escape>", lambda event: self.unpost_listbox())
        
        self._listbox.bind('<Control-n>', self._next)
        self._listbox.bind('<Control-p>', self._previous)

        if self._use_vscrollbar:
            vbar = Scrollbar(listbox_frame, orient=VERTICAL, command= self._listbox.yview)
            vbar.grid(row=0, column=1, sticky=N+S)
            
            self._listbox.configure(yscrollcommand= lambda f, l: autoscroll(vbar, f, l))
            
        if self._use_hscrollbar:
            hbar = Scrollbar(listbox_frame, orient=HORIZONTAL, command= self._listbox.xview)
            hbar.grid(row=1, column=0, sticky=E+W)
            
            self._listbox.configure(xscrollcommand= lambda f, l: autoscroll(hbar, f, l))

        listbox_frame.grid_columnconfigure(0, weight= 1)
        listbox_frame.grid_rowconfigure(0, weight= 1)

        x = -self.cget("borderwidth") - self.cget("highlightthickness") 
        y = self.winfo_height()-self.cget("borderwidth") - self.cget("highlightthickness")

        if self._listbox_width:
            width = self._listbox_width
        else:
            width=self.winfo_width()

        listbox_frame.place(in_=self, x=x, y=y, width=width)
        
        height = min(self._listbox_height, len(values))
        self._listbox.configure(height=height)

        for item in values:
            self._listbox.insert(END, item)

    def post_listbox(self):
        if self._listbox is not None: return

        entry_data = self._entry_var.get()
        if entry_data == '': return

        values = self.autocomplete_function(entry_data)
        if values:
            self._build_listbox(values)

    def unpost_listbox(self):
        if self._listbox is not None:
            self._listbox.master.destroy()
            self._listbox = None

    def get_value(self):
        return self._entry_var.get()

    def set_value(self, text, close_dialog=False):
        self._set_var(text)

        if close_dialog:
            self.unpost_listbox()

        self.icursor(END)
        self.xview_moveto(1.0)
        
    def _set_var(self, text):
        self._entry_var.trace_vdelete("w", self._trace_id)
        self._entry_var.set(text)
        self._trace_id = self._entry_var.trace('w', self._on_change_entry_var)

    def _update_entry_from_listbox(self, event):
        if self._listbox is not None:
            current_selection = self._listbox.curselection()
            
            if current_selection:
                text = self._listbox.get(current_selection)
                self._set_var(text)

            self._listbox.master.destroy()
            self._listbox = None

            self.focus()
            self.icursor(END)
            self.xview_moveto(1.0)
            
        return "break"

    def _previous(self, event):
        if self._listbox is not None:
            current_selection = self._listbox.curselection()

            if len(current_selection)==0:
                self._listbox.selection_set(0)
                self._listbox.activate(0)
            else:
                index = int(current_selection[0])
                self._listbox.selection_clear(index)

                if index == 0:
                    index = END
                else:
                    index -= 1

                self._listbox.see(index)
                self._listbox.selection_set(first=index)
                self._listbox.activate(index)

        return "break"

    def _next(self, event):
        if self._listbox is not None:

            current_selection = self._listbox.curselection()
            if len(current_selection)==0:
                self._listbox.selection_set(0)
                self._listbox.activate(0)
            else:
                index = int(current_selection[0])
                self._listbox.selection_clear(index)
                
                if index == self._listbox.size() - 1:
                    index = 0
                else:
                    index +=1
                    
                self._listbox.see(index)
                self._listbox.selection_set(index)
                self._listbox.activate(index)
        return "break"
    
   

if __name__ == '__main__':
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk

    list_of_items = ['Seraph',
 'Metatron',
 'Sandalphon',
 'Mastema',
 'Aniel',
 'Armaiti',
 'Sraosha',
 'Azrael',
 'Kazfiel',
 'Israfel',
 'Victor',
 'Demeter',
 'Amaterasu',
 'Maria',
 'Laksmi',
 'Norn',
 'Tlazolteotl',
 'Pallas Athena',
 'Ishtar',
 'Scathach',
 'Parvati',
 'Fortuna',
 'Hathor',
 'Garuda',
 'Yatagarasu',
 'Feng Huang',
 'Thunderbird',
 'Phoenix',
 'Suparna',
 'Hamsa',
 'Yggdrasil',
 'Haoma',
 'Kukunochi',
 'Mayahuel',
 'Daphne',
 'Cherub',
 'Throne',
 'Dominion',
 'Virtue',
 'Power',
 'Principality',
 'Archangel',
 'Angel',
 'Da Peng',
 'Rukh',
 'Toufei',
 'Caladrius',
 'Gu Huo Niao',
 'Harpy',
 'Tangata Manu',
 'Shaytan',
 'Ganesha',
 'Master Therion',
 'Xiuhtecuhtli',
 'Valkyrie',
 'Shiwanna',
 'Dis',
 'Karasu Tengu',
 'Vodyanik',
 'Koppa Tengu',
 'Peri',
 'Sarasvati',
 'Kikuri-Hime',
 'Senri',
 'Anahita',
 'Ame no Uzume',
 'Apsaras',
 'Demiurge',
 'Seth',
 'Mada',
 'Samael',
 'Pales',
 'Alciel',
 'Taotie',
 'Pachacamac',
 'Mishaguji',
 'Baphomet',
 'Hresvelgr',
 'Huoniao',
 'Anzu',
 'Gurr',
 'Camazotz',
 'Zhen',
 'Moh Shuvuu',
 'Itsumade',
 'Onmoraki',
 'Erlkonig',
 'Alraune',
 'Zaccoum',
 'Skogsra',
 'Mandrake',
 'Shan Xiao',
 'Vishnu',
 'Hachiman',
 'Odin',
 'Zeus',
 'Omoteotl',
 'Prometheus',
 'Inti',
 'Thoth',
 'Barong',
 'Anubis',
 'Chimera',
 'Kaiming Shou',
 'Makami',
 '"Kamapuaa"',
 'Shiisaa',
 'Sphinx',
 'Sleipnir',
 'Baihu',
 'Airavata',
 'Qing Niuguai',
 'Pabilsag',
 'Apis',
 'Heqet',
 'Heimdall',
 'Hanuman',
 'Kresnik',
 'Cu Chulainn',
 'Tlaloc',
 'Kurama Tengu',
 'Frost Ace',
 'Tam Lin',
 'Nadja',
 'Demonee-ho',
 'Titania',
 'Oberon',
 'Vivian',
 'Spriggan',
 'Lorelei',
 'Silky',
 'High Pixie',
 'Pyro Jack',
 'Jack Frost',
 'Goblin',
 'Pixie',
 'Cerberus',
 'Ammut',
 'Gryphon',
 'Orthrus',
 'Hsing-Hsing',
 'Nekomata',
 'Inugami',
 'Katakirauwa',
 'Kaso',
 'Gogmagog',
 'Tlaltecuhtli',
 'Titan',
 'Tsuchigumo',
 'Kwancha',
 'Bugaboo',
 'Bogaboo',
 'Bagaboo',
 'Dwarf',
 'Sudama',
 'Hua-Po',
 'Knocker',
 'Vritra',
 'Ananta',
 'Orochi',
 'Ouroboros',
 'Gui Xian',
 'Vouivre',
 'Yurlungur',
 'Nozuchi',
 'Naga',
 'Mot',
 'Ixtab',
 'Nergal',
 'Thanatos',
 'Guedhe',
 'Persephone',
 'Orcus',
 'Hel',
 'Fenrir',
 'Cabracan',
 'Catoblepas',
 'Manticore',
 'Pellaidh',
 'Nue',
 'Raiju',
 'Jueyuan',
 'Hecatoncheir',
 'Girimehkala',
 'Grendel',
 'Rakshasa',
 'Black Frost',
 'Wendigo',
 'Ippon-Datara',
 'Gremlin',
 'Arachne',
 'Mothman',
 'Myrmecolion',
 'Ubu',
 'Okiku-Mushi',
 'Shiva',
 'Susano-O',
 'Zaou-Gongen',
 'Kartikeya',
 'Wu Kong',
 'Tonatiuh',
 'Ares',
 'Xi Wangmu',
 'Cybele',
 'Skadi',
 'Isis',
 'Black Maria',
 'Asherah',
 'Diana',
 'Hariti',
 'Sedna',
 'Dzelarhons',
 'Pele',
 'Huang Long',
 'Quetzalcoatl',
 'Zhu Yin',
 'Long',
 'Gucumatz',
 'Patrimpas',
 'Makara',
 'Thor',
 'Bishamonten',
 'Jikokuten',
 'Koumokuten',
 'Zouchouten',
 'Takeminakata',
 'Nebiros',
 'Gemori',
 'Forneus',
 'Mitra',
 'Decarabia',
 'Ose',
 'Dantalian',
 'Orias',
 'Halphas',
 'Bifrons',
 'Melchom',
 'Ongyo-Ki',
 'Berserker',
 'Sui-Ki',
 'Fuu-Ki',
 'Kin-Ki',
 'Yamawaro',
 'Momunofu',
 'Azumi',
 'Oni',
 'Kali',
 'Volvo',
 'Rangda',
 'Dakini',
 'Atropos',
 'Lachesis',
 'Clotho',
 'Yuki Jyorou',
 'Leanan Sidhe',
 'Acheri',
 'Maya',
 'Lilith',
 'Wild Hunt',
 'Succubus',
 'Kaiwan',
 'Hypnos',
 'Incubus',
 'Fomorian',
 'Lilim',
 'Sandman',
 'Beelzebub',
 'Lucifuge',
 'Belial',
 'Mara',
 'Amon',
 'Surt',
 'Tzitzimitl',
 'Abaddon',
 'Loki',
 'Moloch',
 'Balor',
 'Asura',
 'King Frost',
 'Horkos',
 'Mithras',
 'Morax',
 'Vasuki',
 'Fafnir',
 'Nidhoggr',
 'Tiamat',
 'Mushussu',
 'Kingu',
 'Basilisk',
 'Bai Suzhen',
 'Zhu Tun She',
 'Legion',
 'Pisaca',
 'Inferno',
 'Macabre',
 'Poltergeist',
 'Dybbuk',
 'Mad Gasser',
 'Night Stalker',
 'Doppelganger',
 'Jack the Ripper',
 'Slime',
 'Vetala',
 'Kudlak',
 'Strigoii',
 'Ghoul',
 'Churel',
 'Mou-Ryo',
 'Preta',
 'Mother Harlot',
 'Trumpeter',
 'Pale Rider',
 'Black Rider',
 'Red Rider',
 'White Rider',
 'Alice',
 'Matador',
 'David',
 'Kangiten',
 'Kama',
 'Kinmamon',
 'Futotama',
 'Kanbari',
 'Hare of Inaba',
 'Kuda',
 'Chupacabra',
 'Mamedanuki',
 'Masakado',
 'Tezcatlipoca',
 'Attis',
 'Aramisaki',
 'Dionysus',
 'Ogun',
 'Alilat',
 'Anat',
 'Salamander',
 'Undine',
 'Sylph',
 'Gnome',
 'Flaemis',
 'Aquans',
 'Aeros',
 'Erthys',
 'Saki Mitama',
 'Kusi Mitama',
 'Nigi Mitama',
 'Ara Mitama',
 'Demonica-C',
 'Demonica-N']

    root = Tk()
    root.iconbitmap('icon.ico')
    root.geometry("393x500")
    root.title('Demon Fuser')
    root.resizable(False, True)
    root.focus_force()
    for n in range(0,10):
        root.grid_rowconfigure(n, minsize=40)
    opcoes={1,2,3}
    titulo=Label(root,text="Strange Journey - Demon Fuser",justify=RIGHT, font="Arial 15")
    titulo.grid(row=0,columnspan=5,padx=20)
    label1 = Label(root, text="Demons to fuse:", font = "Arial 11")
    label1.grid(row=1,column=0,sticky=W, padx=3,pady=10)
    botaodeAdicionar=Button(root,text="Add Demons",command=adicionarMonstro).grid(column=4,row=7,padx=10)
    botaodeFundir=Button(root,text="Fuse Demons",command=fundir).grid(column=4,row=2,pady=10)
    botaodeReset=Button(root,text="Clear",command=clear).grid(column=4,row=3)
    varUMA = BooleanVar()
    varFiend= BooleanVar()
    varEnigma= BooleanVar()
    var = StringVar(root)
    var.set('one')
    p = ttk.OptionMenu(root, var, "","one","two","three")
    Label(root,text="Depth:",font = "Arial 11").place(x=280,y=52)
    p.place(x=330,y=52)
    umaConverter = Checkbutton(root, text="UMA Converter", variable=varUMA).grid(column=4,row=4,pady=7)
    fiendConverter = Checkbutton(root, text="Fiend Converter", variable=varFiend).grid(column=4,row=5,pady=5)
    enigmaConverter = Checkbutton(root, text="Enigma Converter", variable=varEnigma).grid(column=4,row=6,pady=5)


    combobox_autocomplete = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete.grid(row=2,column=0,padx=5)
    combobox_autocomplete2 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete2.grid(row=2,column=1,padx=5)
    combobox_autocomplete3 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete3.grid(row=3,column=0,padx=5)
    combobox_autocomplete4 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete4.grid(row=3,column=1,padx=5)
    combobox_autocomplete5 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete5.grid(row=4,column=0,padx=5)
    combobox_autocomplete6 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete6.grid(row=4,column=1,padx=5)
    combobox_autocomplete7 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete7.grid(row=5,column=0,padx=5)
    combobox_autocomplete8 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete8.grid(row=5,column=1,padx=5,pady=0)
    combobox_autocomplete9 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete9.grid(row=6,column=0,padx=5)
    combobox_autocomplete10 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete10.grid(row=6,column=1,padx=5)
    combobox_autocomplete11 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete11.grid(row=7,column=0,padx=5)
    combobox_autocomplete12 = Combobox_Autocomplete(root, list_of_items, highlightthickness=1)
    combobox_autocomplete12.grid(row=7,column=1,padx=5)
#    depth=Combobox_Autocomplete(root,(1,2,3))
#    depth.grid(row=4,column=3)
    
    combobox_autocomplete.focus()
    
    root.mainloop()

