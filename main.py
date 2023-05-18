from tkinter import *
import timer

current_task=None

def start_new_task():
    global current_task
    current_task=timer.Timer("learn",5,"bad")
    current_task.total_time_count_up(timer_label, window)
    current_task.current_time_count_up(current_timer_label,window,False)
    
    start_timer_button.grid_forget()
    start_brake_timer_button.grid(row=0,column=5)


def start_brake():
    current_task.total_brake_time_count_up(timer_brake_label, window)
    current_task.current_brake_time_count_up(current_timer_brake_label,window)
    
    start_brake_timer_button.grid_forget()
    keep_timer_button.grid(row=0,column=6)

def keep_task():
    current_task.total_time_count_up(timer_label, window)
    current_task.current_time_count_up(current_timer_label,window,True)

    current_timer_brake_label.config(text="0:00")

    keep_timer_button.grid_forget()
    start_brake_timer_button.grid(row=0,column=5)



window=Tk()
window.title("Productivity app")
window.minsize(width=800,height=400)

####           TOTAL TIME
info_timer_label=Label(text="Total time: ")
info_timer_label.grid(row=0,column=0)

timer_label=Label(text="0:00")
timer_label.grid(row=0,column=1)

info_timer_brake_label=Label(text="Total brake: ")
info_timer_brake_label.grid(row=0,column=2)

timer_brake_label=Label(text="0:00")
timer_brake_label.grid(row=0,column=3)


####           Current TIME

current_info_timer_label=Label(text="Total time: ")
current_info_timer_label.grid(row=1,column=0)

current_timer_label=Label(text="0:00")
current_timer_label.grid(row=1,column=1)

current_info_timer_brake_label=Label(text="Total brake: ")
current_info_timer_brake_label.grid(row=1,column=2)

current_timer_brake_label=Label(text="0:00")
current_timer_brake_label.grid(row=1,column=3)


####           Button TIME


start_timer_button=Button(text="Start",command=start_new_task)
start_timer_button.grid(row=0,column=4)

start_brake_timer_button=Button(text="Stop",command=start_brake)

keep_timer_button=Button(text="Keep",command=keep_task)

window.mainloop()
