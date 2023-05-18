# def start_count():
    
#     if rep % 8 == 0:
#         count_down(20*60)
#         title.config(text="Long Break")
#     elif rep % 2 == 0:
#         count_down(5*60)
#         title.config(text="Short Break")
#     else:
#         count_down(25*60)
#         title.config(text="Work")

# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# def count_down(num):
#     sec =num%60
#     if sec < 10 :
#         sec=f"0{sec}"
#     canvas.itemconfig(canvas_text,text=f"{math.floor(num/60)}:{sec}")
#     if num>0:
#         global timer
#         timer = window.after(1000,count_down,num-1)

import math
class Timer:
    def __init__(self, name,start,category):
        self.name=name
        self.start = start
        self.timer_time=None
        self.timer_brake=None
        self.current_timer_time=None
        self.current_timer_brake=None
        self.total_time = 0
        self.total_brake_time=0
        self.current_time=0
        self.current_brake_time=0
        self.category=category
        self.notes=""
    def total_time_count_up(self,item,window):
        self.total_time +=1
        sec = self.total_time %60
        if sec < 10:
            sec=f"0{sec}"
        self.timer_time=window.after(1000,self.total_time_count_up,item,window)
        if self.timer_brake:
            window.after_cancel(self.timer_brake)

        return item.config(text=f"{math.floor(self.total_time/60)}:{sec}")
    def total_brake_time_count_up(self,item,window):
        self.total_brake_time +=1
        sec = self.total_brake_time %60
        if sec < 10:
            sec=f"0{sec}"
        self.timer_brake=window.after(1000,self.total_brake_time_count_up,item,window)
        window.after_cancel(self.timer_time)
        return item.config(text=f"{math.floor(self.total_brake_time/60)}:{sec}")
    def current_brake_time_count_up(self,item,window):
        self.current_brake_time +=1
        sec = self.current_brake_time %60
        if sec < 10:
            sec=f"0{sec}"
        self.current_timer_brake = window.after(1000,self.current_brake_time_count_up,item,window)
        window.after_cancel(self.current_timer_time)
        return item.config(text=f"{math.floor(self.current_brake_time/60)}:{sec}")
    def current_time_count_up(self,item,window,is_keep):
        if is_keep:
            self.current_time=-1
            self.current_brake_time=0
            window.after_cancel(self.current_timer_brake)
        self.current_time +=1
        sec = self.current_time %60
        if sec < 10:
            sec=f"0{sec}"
        self.current_timer_time=window.after(1000,self.current_time_count_up,item,window,False)
        
        return item.config(text=f"{math.floor(self.current_time/60)}:{sec}")
    
    
    

        