from mttkinter import mtTkinter as tk
#import tkinter as tk
import threading
import time
import numpy as np
import time


#class with GUI
class Application():

    
   #init 
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry("1700x950")
        self.root.title("Cache Coherence Sim")
        self.create_widgets()
        self.cache1 = {1:{"state":"","addr":"","value":""},2:{"state":"","addr":"","value":""},3:{"state":"","addr":"","value":""},4:{"state":"","addr":"","value":""},"LI":{"inst":"","addr":"","value":""},"CI":{"inst":"","addr":"","value":""}}
        self.cache2 = {1:{"state":"","addr":"","value":""},2:{"state":"","addr":"","value":""},3:{"state":"","addr":"","value":""},4:{"state":"","addr":"","value":""},"LI":{"inst":"","addr":"","value":""},"CI":{"inst":"","addr":"","value":""}}
        self.cache3 = {1:{"state":"","addr":"","value":""},2:{"state":"","addr":"","value":""},3:{"state":"","addr":"","value":""},4:{"state":"","addr":"","value":""},"LI":{"inst":"","addr":"","value":""},"CI":{"inst":"","addr":"","value":""}}
        self.cache4 = {1:{"state":"","addr":"","value":""},2:{"state":"","addr":"","value":""},3:{"state":"","addr":"","value":""},4:{"state":"","addr":"","value":""},"LI":{"inst":"","addr":"","value":""},"CI":{"inst":"","addr":"","value":""}}
        self.cache = {"cache1":self.cache1,"cache2":self.cache2,"cache3":self.cache3,"cache4":self.cache4}
        self.bus = {"0000":"","0001":"","0010":"","0011":"","0100":"","0101":"","0110":"","0111":""}
        self.mainmemory={0:hex(0),1:hex(0),10:hex(0),11:hex(0),100:hex(0),101:hex(0),110:hex(0),111:hex(0),"Instruction":""}
        self.mainmemory_label = {0:self.mm1,1:self.mm2,10:self.mm3,11:self.mm4,100:self.mm5,101:self.mm6,110:self.mm7,111:self.mm8}
        self.cache1_label = {1:self.cache1_1,2:self.cache1_2,3:self.cache1_3,4:self.cache1_4,"LI": self.li_cache1,"CI":self.ci_cache1}
        self.cache2_label = {1:self.cache2_1,2:self.cache2_2,3:self.cache2_3,4:self.cache2_4,"LI": self.li_cache2,"CI":self.ci_cache2}
        self.cache3_label = {1:self.cache3_1,2:self.cache3_2,3:self.cache3_3,4:self.cache3_4,"LI": self.li_cache3,"CI":self.ci_cache3}
        self.cache4_label = {1:self.cache4_1,2:self.cache4_2,3:self.cache4_3,4:self.cache4_4,"LI": self.li_cache4,"CI":self.ci_cache4}
        self.cache_label = {"cache1":self.cache1_label,"cache2":self.cache2_label,"cache3":self.cache3_label,"cache4":self.cache4_label}
        self.p={"cache1":self.p1,"cache2":self.p2,"cache3":self.p3,"cache4":self.p4}
        self.instruction=[]
        self.processor_list=["P1","P2","P3","P4"]
        self.cache_list=["cache1","cache2","cache3","cache4"]
        self.cache_dic={"cache1":"P1","cache2":"P2","cache3":"P3","cache4":"P4"}
        self.instructions_list=["read","calc","read"]
        self.state_flag = False
        self._lock = threading.Lock()
        self._lock1 = threading.Lock()
        self._lock2 = threading.Lock()
        self.count=0
        
##    def start_threads(self):
##        self.p1= threading.Thread(target=self.processor_main, args=("P1",))
##        self.p2= threading.Thread(target=self.processor_main, args=("P2",))
##        self.p3= threading.Thread(target=self.processor_main, args=("P3",))
##        self.p4= threading.Thread(target=self.processor_main, args=("P4",))
##        self.p1.start()
##        self.p2.start()
##        self.p3.start()
##        self.p4.start()
##        self.p1.join()
##        self.p2.join()
##        self.p3.join()
##        self.p4.join()

    # run app
    def run(self):
        self.root.mainloop()
  

    # create widgets
    def create_widgets(self):
        self.bg = tk.PhotoImage(file = "fondo_a.png")
        # Create Canvas
        self.canvas1 = tk.Canvas( self.root, width = 1700,
                 height = 950)
  
        self.canvas1.pack(fill = "both", expand = True)
 
        # Display image
        self.canvas1.create_image( 0, 0, image = self.bg, 
                     anchor = "nw")
        # State_button
        self.state_button = tk.Button( self.root, text = "Start", font=('Georgia 15'), bg="GREEN",
                                      command = self.state_change)

        self.state_button_canvas = self.canvas1.create_window( 1050, 680, 
                                       anchor = "nw",
                                       window = self.state_button)
        # Enter_button
        self.enter_button = tk.Button( self.root, text = "Enter", command = self.enter, font=('Georgia 10'), state='disabled')
        self.enter_button_canvas = self.canvas1.create_window( 857, 888, 
                                       anchor = "nw",
                                       window = self.enter_button)
        #Entry 
        self.entry = tk.Entry(self.root, width=35, font=('Georgia 15'),bg="LIGHT GRAY", state='disabled')
        self.entry.place(x=300, y=888)

        # label instructions
        #cache1
        self.li_cache1 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.li_canvas1 = self.canvas1.create_window( 232, 87, 
                                       anchor = "nw",
                                       window = self.li_cache1)

        self.ci_cache1 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.ci_canvas1 = self.canvas1.create_window( 232, 187, 
                                       anchor = "nw",
                                       window = self.ci_cache1)
        #cache2
        self.li_cache2 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.li_canvas2 = self.canvas1.create_window( 660, 87, 
                                               anchor = "nw",
                                               window = self.li_cache2)
        self.ci_cache2 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.ci_canvas2 = self.canvas1.create_window( 660, 187, 
                                               anchor = "nw",
                                               window = self.ci_cache2)

        #cache3
        self.li_cache3 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.li_canvas3 = self.canvas1.create_window( 1088, 87, 
                                               anchor = "nw",
                                               window = self.li_cache3)
        self.ci_cache3 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.ci_canvas3 = self.canvas1.create_window( 1088, 187, 
                                               anchor = "nw",
                                               window = self.ci_cache3)

        #cache4
        self.li_cache4 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.li_canvas4 = self.canvas1.create_window( 1516, 87, 
                                               anchor = "nw",
                                               window = self.li_cache4)
        self.ci_cache4 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.ci_canvas4 = self.canvas1.create_window( 1516, 187, 
                                               anchor = "nw",
                                               window = self.ci_cache4)
        #mainmemory
        #0000
        self.mm1 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm1_canvas1 = self.canvas1.create_window( 250, 567, 
                                               anchor = "nw",
                                               window = self.mm1)
        #0001
        self.mm2 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm2_canvas1 = self.canvas1.create_window( 250, 637, 
                                               anchor = "nw",
                                               window = self.mm2)
        #0010
        self.mm3 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm3_canvas1 = self.canvas1.create_window( 250, 710, 
                                               anchor = "nw",
                                               window = self.mm3)
        #0011
        self.mm4 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm4_canvas1 = self.canvas1.create_window( 250, 790, 
                                               anchor = "nw",
                                               window = self.mm4)
        #0100
        self.mm5 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm5_canvas1 = self.canvas1.create_window( 700, 567, 
                                               anchor = "nw",
                                               window = self.mm5)
        #0101
        self.mm6 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm6_canvas1 = self.canvas1.create_window( 700, 637, 
                                               anchor = "nw",
                                               window = self.mm6)
        #0110
        self.mm7 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm7_canvas1 = self.canvas1.create_window( 700, 710, 
                                               anchor = "nw",
                                               window = self.mm7)
        #0111
        self.mm8 = tk.Label(self.root, bg= "white", text = "0x0000", font =("Georgia", 20))
        self.mm8_canvas1 = self.canvas1.create_window( 700, 790, 
                                               anchor = "nw",
                                               window = self.mm8)
        #instructions
        #p1
        self.p1 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.p1_canvas1 = self.canvas1.create_window( 1370, 580, 
                                               anchor = "nw",
                                               window = self.p1)
        #p2
        self.p2 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.p2_canvas1 = self.canvas1.create_window( 1370, 665, 
                                               anchor = "nw",
                                               window = self.p2)
        #p3
        self.p3 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.p3_canvas1 = self.canvas1.create_window( 1370, 740, 
                                               anchor = "nw",
                                               window = self.p3)
        #p4
        self.p4 = tk.Label(self.root, bg= "white", text = "", font =("Georgia", 14))
        self.p4_canvas1 = self.canvas1.create_window( 1370, 825, 
                                               anchor = "nw",
                                               window = self.p4)

        #L1 cache values
        #cache1
        self.cache1_1 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c11_canvas1 = self.canvas1.create_window( 52, 77, 
                                               anchor = "nw",
                                               window = self.cache1_1)
        self.cache1_2 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c12_canvas1 = self.canvas1.create_window( 52, 135, 
                                               anchor = "nw",
                                               window = self.cache1_2)
        self.cache1_3 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c13_canvas1 = self.canvas1.create_window( 52, 195, 
                                               anchor = "nw",
                                               window = self.cache1_3)
        self.cache1_4 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c14_canvas1 = self.canvas1.create_window( 52, 260, 
                                               anchor = "nw",
                                               window = self.cache1_4)
        #cache2
        self.cache2_1 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c21_canvas1 = self.canvas1.create_window( 475, 77, 
                                               anchor = "nw",
                                               window = self.cache2_1)
        self.cache2_2 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c22_canvas1 = self.canvas1.create_window( 475, 135, 
                                               anchor = "nw",
                                               window = self.cache2_2)
        self.cache2_3 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c23_canvas1 = self.canvas1.create_window( 475, 195, 
                                               anchor = "nw",
                                               window = self.cache2_3)
        self.cache2_4 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c24_canvas1 = self.canvas1.create_window( 475, 260, 
                                               anchor = "nw",
                                               window = self.cache2_4)
        #cache3
        self.cache3_1 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c31_canvas1 = self.canvas1.create_window( 895, 77, 
                                               anchor = "nw",
                                               window = self.cache3_1)
        self.cache3_2 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c32_canvas1 = self.canvas1.create_window( 895, 135, 
                                               anchor = "nw",
                                               window = self.cache3_2)
        self.cache3_3 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c33_canvas1 = self.canvas1.create_window( 895, 195, 
                                               anchor = "nw",
                                               window = self.cache3_3)
        self.cache3_4 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c34_canvas1 = self.canvas1.create_window( 895, 260, 
                                               anchor = "nw",
                                               window = self.cache3_4)
        #cache4
        self.cache4_1 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c41_canvas1 = self.canvas1.create_window( 1315, 77, 
                                               anchor = "nw",
                                               window = self.cache4_1)
        self.cache4_2 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c42_canvas1 = self.canvas1.create_window( 1315, 135, 
                                               anchor = "nw",
                                               window = self.cache4_2)
        self.cache4_3 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c43_canvas1 = self.canvas1.create_window( 1315, 195, 
                                               anchor = "nw",
                                               window = self.cache4_3)
        self.cache4_4 = tk.Label(self.root, bg= "white", text = "", font =("Cambria", 10))
        self.c44_canvas1 = self.canvas1.create_window( 1315, 260, 
                                               anchor = "nw",
                                               window = self.cache4_4)

        #last
        self.instr = tk.Label(self.root, bg= "white", text = "Write Instruction", font =("Georgia", 14))
        self.instr_canvas1 = self.canvas1.create_window( 1370, 884, 
                                       anchor = "nw",
                                       window = self.instr)

    # Enter button
    def enter(self):
        instruction_complete = self.entry.get()
        instruction_split = self.entry.get().split()
        # Validate  entry instruction format

        try:
            if(len(instruction_split)==2):
                if (instruction_split[0] in self.processor_list and instruction_split[1] == "calc"):
                    self.instr.config(text = instruction_complete)
                    self.instruction=instruction_split
                else:
                    self.instr.config(text = "Instruction format not correct")
            elif(len(instruction_split)==3):
                if (instruction_split[0] in self.processor_list and instruction_split[1] == "read" and int(instruction_split[2],2) in range(0,8)):
                    self.instr.config(text = instruction_complete)
                    self.instruction=instruction_split
                else:
                    self.instr.config(text = "Instruction format not correct")
            elif(len(instruction_split)==4):
                if (instruction_split[0] in self.processor_list and instruction_split[1] == "write" and int(instruction_split[2],2) in range(0,8) and int(instruction_split[3],16) in range (0,65536)):
                    self.instr.config(text = instruction_complete)
                    self.instruction=instruction_split
                else:
                    self.instr.config(text = "Instruction format not correct")
            else:
                self.instr.config(text = "Instruction format not correct")
        except:
                self.instr.config(text = "Instruction format not correct")
    # Running or pause
    def state_change(self):
        if(self.state_flag == True):
            self.enter_button.configure(state="normal")
            self.entry.configure(state="normal")
            self.state_button.configure(bg = "GREEN")
            self.state_button.config(text = "Continue")
            self.state_flag = False
        else:
            
            self.enter_button.configure(state="disabled")
            self.entry.configure(state="disabled")
            self.state_button.configure(bg = "RED")
            self.state_button.config(text = "Pause")
            self.state_flag = True

    # Processors method
    def processor_main(self,cacheName):

        print ("Starting " + cacheName + "\n")
        #print(self.state_flag)
        while(True):
            if(self.state_flag):
                addr = ""
                inst = self.random_instruction()
                value = ""

                #Generate random values
                if(inst=="calc"):
                    pass
                elif(inst=="read"):
                    addr=self.random_addr()
                elif(inst=="write"):
                    addr=self.random_addr()
                    value=self.random_value()
                else:
                    print("Instruction not valid")
                    exit()

                #set if entry
                if(len(self.instruction)!=0):
                    if(self.cache_dic[cacheName]==self.instruction[0]):
                        self.instr.config(text = "")
                        if(len(self.instruction)==2):
                            inst=self.instruction[1]
                            addr = ""
                            value = ""
                        elif(len(self.instruction)==3):
                            inst=self.instruction[1]
                            addr=int(self.instruction[2])
                            value = ""
                        elif(len(self.instruction)==4):
                            inst=self.instruction[1]
                            addr=int(self.instruction[2])
                            value=hex(int(self.instruction[3],16))
                        else:
                            pass
                        self.instruction=[]

                #set dictionary values

                self.cache[cacheName]["LI"]["inst"]=self.cache[cacheName]["CI"]["inst"]
                self.cache[cacheName]["LI"]["addr"]=self.cache[cacheName]["CI"]["addr"]
                self.cache[cacheName]["LI"]["value"]=self.cache[cacheName]["CI"]["value"]

                self.cache[cacheName]["CI"]["inst"]= inst
                self.cache[cacheName]["CI"]["addr"]= addr
                self.cache[cacheName]["CI"]["value"]= value

                self.cache_label[cacheName]["LI"].config(text = self.cache[cacheName]["LI"]["inst"]+ " " +str(self.cache[cacheName]["LI"]["addr"])+ " " +str(self.cache[cacheName]["LI"]["value"]))
                self.cache_label[cacheName]["CI"].config(text = self.cache[cacheName]["CI"]["inst"]+ " " +str(self.cache[cacheName]["CI"]["addr"])+ " " +str(self.cache[cacheName]["CI"]["value"]))
                self.p[cacheName].config(text = self.cache[cacheName]["CI"]["inst"]+ " " +str(self.cache[cacheName]["CI"]["addr"])+ " " +str(self.cache[cacheName]["CI"]["value"]))

                #State machine
                if(inst == "write" or inst == "read"):
                    self.state_main(cacheName)

                #print values
                #print(self.cache)
                for cache in self.cache_list:
                    for i in [1,2,3,4]:
                        self.cache_label[cache][i].config(text =self.cache[cache][i]["state"]+":"+str(self.cache[cache][i]["addr"])+ "->" + str(self.cache[cache][i]["value"]))
                for j in [0,1,10,11,100,101,110,111]:
                    self.mainmemory_label[j].config(text =str(self.mainmemory[j]))
                time.sleep(10)

        #self.root.after(1000, self.start_threads,threadName)
        #time.sleep(1)
        #self.processor_main(threadName)

    #generate random instruction using hypergeometric distribution
    def random_instruction(self):
        s = np.random.hypergeometric(2, 2, 2)
        if s==0:
            s = "read"
        elif s==1:
            s = "write"
        else:
            s = "calc"
        return s
        
##    def random_processor(self):
##        s = np.random.binomial(1, 0.5,2)
##        s = map(str, s)
##        s = ''.join(s)          
##        s = int(s)
##        
##        if s==0:
##            s = "P0"
##        elif s==1:
##            s = "P1"
##        elif s==2:
##            s = "P2"
##        else:
##            s = "P3"
##        return s

#generate random address using binomial distribution
    def random_addr(self):
        s = np.random.binomial(1, 0.5,3)
        s = map(str, s)
        s = ''.join(s)          
        s = int(s)
        return s
#generate random value using binomial distribution
    def random_value(self):
        s = np.random.binomial(1, 0.5,16)
        s = map(str, s)
        s = ''.join(s)          
        s = hex(int(s,2))
        return s

    def snoop(self,state,cacheName,cache_space):
        if(state=="RM"):
            # if in caches -> get value from them
            #else get from memory
            return_flag=self.search_other_caches_read(cacheName,cache_space)
            if(return_flag=="SHR"):
                pass
            else:
                cache_space["state"]="E"
                cache_space["addr"]= self.cache[cacheName]["CI"]["addr"]
                cache_space["value"]= self.mainmemory[self.cache[cacheName]["CI"]["addr"]]
        # write miss -> write in memory
        elif(state=="WM"):
            if(cache_space["state"]=="M"):
                self.write_memory(cache_space)
        else:
            pass

        
    def write_memory(self,cache_space):
        with self._lock1:
            self.mainmemory[cache_space["addr"]]=cache_space["value"]

    def state_main(self,cacheName):
        # get whats in space
        module=int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1
        cache_space= self.cache[cacheName][module]
        # if read
        if(self.cache[cacheName]["CI"]["inst"] == "read"):
             # data possibly in cache
            if (cache_space["addr"]==self.cache[cacheName]["CI"]["addr"]):
                if(cache_space["state"]=="M"):
                     print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":RH\n")
                     cache_space["state"]="M"
                elif(cache_space["state"]=="E"):
                     print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":RH\n")
                     cache_space["state"]="E" 
                elif(cache_space["state"]=="S"):
                     print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":RH\n")
                     cache_space["state"]="S"
                elif(cache_space["state"]=="I"):
                     print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":RM\n")
                     self.bus_state("RM",cacheName,cache_space)
                else:
                    pass
            # data not in cache
            else:
                print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":RM\n")
                if(cache_space["state"]==""):
                    print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":Cold Cache\n")
                    pass
                else:
                    if(cache_space["state"]=="M"):
                        self.write_memory(cache_space)   
                self.bus_state("RM",cacheName,cache_space)
                
        # if write
        elif(self.cache[cacheName]["CI"]["inst"] == "write"):
            # data possibly in cache
            if (cache_space["addr"]==self.cache[cacheName]["CI"]["addr"]):
                if(cache_space["state"]=="M"):
                     print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":WH\n")
                     cache_space["state"]="M"
                     cache_space["addr"]= self.cache[cacheName]["CI"]["addr"]
                     cache_space["value"]= self.cache[cacheName]["CI"]["value"]
                elif(cache_space["state"]=="E"):
                     print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":WH\n")
                     cache_space["state"]="M"
                     cache_space["addr"]= self.cache[cacheName]["CI"]["addr"]
                     cache_space["value"]= self.cache[cacheName]["CI"]["value"]
                elif(cache_space["state"]=="S"):
                     print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":WH\n")
                     cache_space["state"]="M"
                     cache_space["addr"]= self.cache[cacheName]["CI"]["addr"]
                     cache_space["value"]= self.cache[cacheName]["CI"]["value"]
                elif(cache_space["state"]=="I"):
                    print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":WM\n")
                    cache_space["state"]="M"
                    cache_space["addr"]= self.cache[cacheName]["CI"]["addr"]
                    cache_space["value"]= self.cache[cacheName]["CI"]["value"]
                else:
                    pass
            # data not in cache
            else:
                print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":WM\n")
                if(cache_space["state"]==""):
                    print(cacheName +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":Cold Cache\n")
                else:
                    self.bus_state("WM",cacheName,cache_space)
                cache_space["state"]="M"
                cache_space["addr"]= self.cache[cacheName]["CI"]["addr"]
                cache_space["value"]= self.cache[cacheName]["CI"]["value"]
            self.bus_state("invalidation",cacheName,cache_space)

        else:
            pass
        

    def bus_state(self,state,cacheName,cache_space):
        with self._lock:
            # Others snoop
            if(state=="WM" or state=="RM"):
                self.snoop(state,cacheName,cache_space)

            # Invalidate others       
            elif(state=="invalidation"):
                self.writing_invalidation(cacheName,cache_space)
    def writing_invalidation(self,cacheName,cache_space):
        with self._lock2:
            for cache in self.cache_list:
                if (cache==cacheName):
                    pass
                else:
                    if(self.cache[cacheName]["CI"]["addr"]==self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["addr"]):
                        self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"]="I"
                        print(cache +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":SHI\n")
                    else:
                        pass
##    def search_cache(self,cacheName):
##        module=self.cache[cacheName]["CI"]["addr"]%4+1
##        cache_space= self.cache[cacheName][module]
##        print("a")
##
##        if (cache_space[addr]==self.cache[cacheName]["CI"]["addr"]):
##            pass
##        else:
##            print(cachename +":"+ cache_space[addr] + ":RM\n")
    def search_other_caches_read(self,cacheName,cache_space):
        return_flag="RM"
        for cache in self.cache_list:
            if (cache==cacheName):
                pass
            else:
                if(self.cache[cacheName]["CI"]["addr"]==self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["addr"]):
                    if(self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"] == "M"):
                        return_flag="SHR"
                        print(cache +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":SHR\n")
                        # set cache
                        cache_space["state"]="S"
                        cache_space["addr"]= self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["addr"]
                        cache_space["value"]= self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["value"]
                        # set other state
                        self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"]="S"
                        # write on memory
                        self.write_memory(self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1])
                    elif(self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"] == "E"):
                        return_flag="SHR"
                        print(cache +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":SHR\n")
                        # set cache
                        cache_space["state"]="S"
                        cache_space["addr"]= self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["addr"]
                        cache_space["value"]= self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["value"]
                        # set other state
                        self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"]="S"
                    elif(self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"] == "S"):
                        return_flag="SHR"
                        print(cache +":"+ str(self.cache[cacheName]["CI"]["addr"]) + ":SHR\n")
                        # set cache
                        cache_space["state"]="S"
                        cache_space["addr"]= self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["addr"]
                        cache_space["value"]= self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["value"]
                        # set other state
                        self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"]="S"
                    elif(self.cache[cache][int(int(str(self.cache[cacheName]["CI"]["addr"])))%4+1]["state"] == "I"):
                        pass
                    else:
                        pass
                else:
                    pass
        return return_flag



if __name__ == "__main__":
    print("Starting app")
    app = Application()
    #GUI_thread= threading.Thread(target=app.run())
    p1= threading.Thread(target=app.processor_main, args=("cache1",))
    p2= threading.Thread(target=app.processor_main, args=("cache2",))
    p3= threading.Thread(target=app.processor_main, args=("cache3",))
    p4= threading.Thread(target=app.processor_main, args=("cache4",))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    #app.mainloop()
   

