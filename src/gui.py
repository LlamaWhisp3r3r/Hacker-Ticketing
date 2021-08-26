import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import time
import threading
import winsound
import random

class GUI:

	def __init__(self, master=None):
		self.master = master
		self.master.title("Hacker Ticket")
		self.master.geometry("800x800")
		self.launch_frame = ttk.Frame(self.master, width=200, height=100)
		self.launch_frame.pack()
		self.port_line = 0
		self.description_line = 0
		self.current_line_count = 0
		self.last_save = ""
		self.priority_num = 0

	def launch_page(self):
		start_button = ttk.Button(self.launch_frame, text="Start a Ticket", command=self.start_ticket)
		start_button.place(relx=.5, rely=.5, anchor="center")

	def start_ticket(self):
		self.master.ticket = filedialog.asksaveasfile(filetypes=(("text files","*.txt"),), defaultextension=(("text file","*.txt"),), initialfile="Hackin' The Past")
		self.file_show_frame_create()

	def write_to_ticket(self, message):
		self.master.ticket.write(message)

	def open_ticket(self):
		self.master.ticket = filedialog.askopenfilename(initialdir = "C:\\",title = "Select file",filetypes = (("text files","*.txt"),))

	def file_show_frame_create(self):
		self.master.ticket.close()
		self.launch_frame.destroy()
		self.file_show_frame = ttk.Frame(self.master, width=800, height=800)
		self.file_show_frame.pack()
		self.file_entry = Text(self.file_show_frame)
		start_file_seq = "=" * 20 + "\n"
		start_file_seq += self.master.ticket.name.split("/")[-1].split(".")[0] + "\n"
		start_file_seq += "=" * 20 + "\n"
		self.current_line_count += 4
		self.last_save += start_file_seq 
		self.file_entry.insert(END, start_file_seq)
		self.file_entry.grid(row=0, columnspan=6)
		self.port_button = ttk.Button(self.file_show_frame, text="Add Port Info", command=self.add_port)
		self.port_button.grid(row=1, column=0)
		self.desscription_button = ttk.Button(self.file_show_frame, text="Add Hypothesis Info", command=self.add_description)
		self.desscription_button.grid(row=2, column=0)
		self.timer_button = ttk.Button(self.file_show_frame, text="Start Timer", command=self.timer_go)
		self.timer_button.grid(row=3, column=0)
		self.timer_amount = ttk.Entry(self.file_show_frame)
		self.timer_amount.insert(0, "900")
		self.timer_amount.grid(row=3, column=1)
		self.save_button = ttk.Button(self.file_show_frame, text="Save File", command=self.save_file)
		self.save_button.grid(row=4, column=1, pady=15)
		self.save_button = ttk.Button(self.file_show_frame, text="Close Program", command=self.quit)
		self.save_button.grid(row=4, column=3, pady=15)

	def save_file(self):
		os.remove(self.master.ticket.name)
		with open(self.master.ticket.name, 'w') as ticket:
			ticket.write(self.file_entry.get("0.0", END))

	def quit(self):
		self.master.destroy()

	def add_description(self):
		self.hide_widget(self.desscription_button)
		self.add_description_button = ttk.Button(self.file_show_frame, text="Add Hypothesis", command=self.submit_description)
		self.description_entry = ttk.Entry(self.file_show_frame, width=70)
		self.description_entry.insert(0, "Hypothesis")
		self.add_description_button.grid(row=2, column=0)
		self.description_entry.grid(row=2, column=1, columnspan=3)
		self.des_pri = IntVar()
		self.des_pri_check = ttk.Checkbutton(self.file_show_frame, text="Priority", variable=self.des_pri, onvalue=1, offvalue=0)
		self.des_pri_check.grid(row=2, column=4)

	def submit_description(self):
		self.hide_widget(self.add_description_button)
		description_string = self.description_entry.get()
		self.hide_widget(self.description_entry)
		self.hide_widget(self.description_entry)
		self.hide_widget(self.des_pri_check)
		prior_check = self.des_pri.get()
		if self.description_line == 0:
			description_seq = """\
====================
     Hypothesis
====================
"""
			description_seq += description_string + "\n"
			self.last_save += description_seq
			self.file_entry.insert(self.convert_int_to_string(self.current_line_count), description_seq)
			self.current_line_count += 4
			if prior_check == 1:
				random_string = "priority" + str(self.priority_num)
				self.priority_num += 1
				self.file_entry.tag_add(random_string, self.convert_int_to_string(self.current_line_count-1), self.convert_int_to_string(self.current_line_count))
				self.file_entry.tag_config(random_string, background="red")
				self.priority_num += 1
			self.description_line += self.current_line_count
		else:
			description_seq = description_string + "\n"
			self.last_save += description_seq
			self.file_entry.insert(self.convert_int_to_string(self.description_line), description_seq)
			self.increase_current_line(1)
			print(prior_check)
			if prior_check == 1:
				random_string = str(random.random())
				self.file_entry.tag_add(random_string, self.convert_int_to_string(self.description_line), self.convert_int_to_string(self.description_line+1))
				self.file_entry.tag_config(random_string, background="red")
				self.priority_num += 1
			self.description_line += 1

		self.desscription_button.grid(row=2, column=0)

	def increase_current_line(self, amount):
		if self.description_line < self.port_line and self.description_line != 0:
			print("Increasing port_line")
			self.port_line += amount 
			self.current_line_count += amount 
		elif self.port_line < self.description_line and self.port_line != 0:
			print("Increading description line")
			self.description_line += amount
			self.current_line_count += amount
		else:
			self.current_line_count += amount

	def timer_go(self):
		self.timer_amount.grid_remove()
		self.timer_label = ttk.Label(self.file_show_frame, text="0")
		self.timer_label.grid(row=3, column=1)
		self.hide_widget(self.timer_button)
		self.stop_timer_button = ttk.Button(self.file_show_frame, text="Stop Timer", command=self.stop_timer)
		self.stop_timer_button.grid(row=3, column=0)
		self.timer_thread = threading.Thread(target=self.thread_timer)
		self.timer_thread_flag = True
		self.timer_thread.start()

	def stop_timer(self):
		self.timer_thread_flag = False
		self.hide_widget(self.stop_timer_button)
		self.timer_button.grid(row=3, column=0)
		self.hide_widget(self.timer_label)
		self.timer_amount.grid(row=3, column=1)
		self.hide_widget(self.timer_label)


	def thread_timer(self):
		amount = time.time()
		while time.time() - amount < int(self.timer_amount.get()) and self.timer_thread_flag != False:
			time.sleep(1)
			self.timer_label['text'] = str(round(time.time() - amount))

		if self.timer_thread_flag:

			winsound.PlaySound("C:\\Users\\natha\\Coding\\Projects\\Gigakoops.wav", winsound.SND_ASYNC)
			messagebox.showerror("Timer Done", "Your Timer is Finished")
			self.hide_widget(self.stop_timer_button)
			self.stop_music = ttk.Button(self.file_show_frame, text="Stop Alarm", command=self.stop_alarm)
			self.stop_music.grid(row=3, column=0)


	def stop_alarm(self):
		winsound.PlaySound(None, winsound.SND_PURGE)
		self.hide_widget(self.stop_music)
		self.hide_widget(self.timer_label)
		self.timer_button.grid(row=3, column=0)
		self.timer_amount.grid(row=3, column=1)


	def add_port(self):
		self.hide_widget(self.port_button)
		self.add_port_button = ttk.Button(self.file_show_frame, text="Submit Port", command=self.submit_port)
		self.port_number = ttk.Entry(self.file_show_frame)
		self.port_type = ttk.Entry(self.file_show_frame)
		self.port_description = ttk.Entry(self.file_show_frame, width=45)
		self.port_description.insert(0, "Apache James")
		self.port_type.insert(0, "TCP")
		self.port_number.insert(0, "80")
		self.add_port_button.grid(row=1, column=0)
		self.port_description.grid(row=1, column=1, columnspan=3)
		self.port_type.grid(row=1, column=4)
		self.port_number.grid(row=1, column=5)
		self.pri_check = IntVar()
		self.priority_check = ttk.Checkbutton(self.file_show_frame, text="Priority", variable=self.pri_check, onvalue=1, offvalue=0)
		self.priority_check.grid(row=1, column=6)

	def hide_widget(self, widget):
		widget.grid_remove()

	def submit_port(self):
		port_des = self.port_description.get()
		port_ty = self.port_type.get()
		port_num = self.port_number.get()
		prior_check = self.pri_check.get()
		if self.port_line == 0:
			grid_file_seq = """\
====================
        Ports
====================
"""
			grid_file_seq += port_num + "\t" + port_ty + "\t" + port_des + "\n"
			self.last_save += grid_file_seq
			print(grid_file_seq)
			self.file_entry.insert(self.convert_int_to_string(self.current_line_count), grid_file_seq)
			self.current_line_count += 4
			if prior_check == 1:
				random_string = "priority" + str(self.priority_num)
				self.priority_num += 1
				self.file_entry.tag_add(random_string, self.convert_int_to_string(self.current_line_count-1), self.convert_int_to_string(self.current_line_count))
				self.file_entry.tag_config(random_string, background="red")
				self.priority_num += 1
			self.port_line += self.current_line_count
		else:
			submit_port_seq = port_num + "\t" + port_ty + "\t" + port_des + "\n"
			self.last_save += submit_port_seq
			print(submit_port_seq)
			self.file_entry.insert(self.convert_int_to_string(self.port_line), submit_port_seq)
			self.increase_current_line(1)
			if prior_check == 1:
				random_string = "priority" + str(self.priority_num)
				self.priority_num += 1
				self.file_entry.tag_add(random_string, self.convert_int_to_string(self.port_line), self.convert_int_to_string(self.port_line+1))
				self.file_entry.tag_config(random_string, background="red")
				self.priority_num += 1
			self.port_line += 1

		self.hide_widget(self.port_number)
		self.hide_widget(self.port_type)
		self.hide_widget(self.port_description)
		self.hide_widget(self.add_port_button)
		self.hide_widget(self.priority_check)
		self.port_button.grid(row=1, column=0)

	def convert_int_to_string(self, number):
		int_string = str(number) + ".0"
		return int_string
