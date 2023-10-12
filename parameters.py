# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:18:01 2023

@author: aggar
"""

import tkinter as tk
from tkinter import ttk

def lower_rate_limit(self):
    #lower rate limit label
    lower_rate = tk.Label(self,text = 'Lower Rate Limit', font = ('Montserrat',12),anchor = 'center')
    lower_rate.grid(row = 1, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #lower rate limit field input
    lower_rate_read = ttk.Combobox(self, width = 10) 
    lower_rate_read.grid(column = 2, row = 1,sticky ='W')
    lower_rate_read['values'] = (30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                 80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
    lower_rate_read.current(0)
    return lower_rate_read.get()

def upper_rate_limit(self):
    #Upper rate limit label
    upper_rate = tk.Label(self,text = 'Upper Rate Limit', font = ('Montserrat',12),anchor = 'center')
    upper_rate.grid(row = 2, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #Upper rate limit field input
    upper_rate_read = ttk.Combobox(self, width = 10) 
    upper_rate_read.grid(row = 2,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    upper_rate_read['values'] = (50,55,60,65,70,75,80,85,90,95,100,105,110,115,
                                 120,125,130,135,140,145,150,155,160,165,170,175) 
    upper_rate_read.current(0)
    
    return upper_rate_read 

def atrial_amplitude(self):
    #Atrial amplitude label
    global  atrial_amp
    atrial_amp = tk.Label(self,text = 'Atrial Amplitude', font = ('Montserrat',12),anchor = 'center')
    atrial_amp.grid(row = 3, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    atrial_amp_read = ttk.Combobox(self, width = 10) 
    atrial_amp_read.grid(row = 3,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    atrial_amp_read['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                 2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
    atrial_amp_read.current(0)
    
    return atrial_amp_read.get()

def ventrical_amplitude(self):
    global ventrical_amp 
    #Atrial amplitude label
    ventrical_amp = tk.Label(self,text = 'Ventrical Amplitude', font = ('Montserrat',12),anchor = 'center')
    ventrical_amp.grid(row = 4, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    ventrical_amp_read = ttk.Combobox(self, width = 10) 
    ventrical_amp_read.grid(row = 4,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    ventrical_amp_read['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                 2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
    ventrical_amp_read.current(0)
    
    return ventrical_amp_read.get()


def atrial_pulse(self):
    global atrial_puls 
    #Atrial pulse width label
    atrial_puls = tk.Label(self,text = 'Ventrical Pulse Width', font = ('Montserrat',12),anchor = 'center')
    atrial_puls.grid(row = 5, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    atrial_pulse_read = ttk.Combobox(self, width = 10) 
    atrial_pulse_read.grid(row = 5,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    atrial_pulse_read['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
    atrial_pulse_read.current(0)
    
    return atrial_pulse_read.get()

def ventrical_pulse(self):
    global ventrical_puls 
    #Atrial pulse width label
    ventrical_puls = tk.Label(self,text = 'Ventrical Pulse Width', font = ('Montserrat',12),anchor = 'center')
    ventrical_puls.grid(row = 6, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    ventrical_pulse_read = ttk.Combobox(self, width = 10) 
    ventrical_pulse_read.grid(row = 6,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    ventrical_pulse_read['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
    ventrical_pulse_read.current(0)
    
    return ventrical_pulse_read.get()

def atrial_sensitivity(self):
    #Atrial pulse width label
    atrial_sense = tk.Label(self,text = 'Atrial Sensitivity', font = ('Montserrat',12),anchor = 'center')
    atrial_sense.grid(row = 7, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    atrial_sense_read = ttk.Combobox(self, width = 10) 
    atrial_sense_read.grid(row = 7,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    atrial_sense_read['values'] = (0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0) 
    atrial_sense_read.current(0)
    
    return atrial_sense_read.get()

def ventrical_sensitivity(self):
    #Atrial pulse width label
    ventrical_sense = tk.Label(self,text = 'Ventrical Sensitivity', font = ('Montserrat',12),anchor = 'center')
    ventrical_sense.grid(row = 8, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    ventrical_sense_read = ttk.Combobox(self, width = 10) 
    ventrical_sense_read.grid(row = 8,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    ventrical_sense_read['values'] = (0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0) 
    ventrical_sense_read.current(0)
    
    return ventrical_sense_read.get()

def vrp(self):
    #Atrial pulse width label
    ventrical_period = tk.Label(self,text = 'Ventrical Refractory Period', font = ('Montserrat',12),anchor = 'center')
    ventrical_period.grid(row = 9, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    ventrical_period_read = ttk.Combobox(self, width = 10) 
    ventrical_period_read.grid(row = 9,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    ventrical_period_read['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
    ventrical_period_read.current(0)
    
    return ventrical_period_read.get()

def arp(self):
    #Atrial pulse width label
    atrial_period = tk.Label(self,text = 'Atrial Refractory Period', font = ('Montserrat',12),anchor = 'center')
    atrial_period.grid(row = 10, column = 1,sticky = 'we', pady =10,padx =50 )
    
    #atrial_amp field input
    atrial_period_read = ttk.Combobox(self, width = 10) 
    atrial_period_read.grid(row = 10,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    atrial_period_read['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
    atrial_period_read.current(0)
    
    return atrial_period_read.get()

def pvarp(self):
    #Atrial pulse width label
    pvar_period = tk.Label(self,text = 'PVARP', font = ('Montserrat',12),anchor = 'center')
    pvar_period.grid(row = 11, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    pvar_period_read = ttk.Combobox(self, width = 10) 
    pvar_period_read.grid(row = 11,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    pvar_period_read['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
    pvar_period_read.current(0)
    
    return pvar_period_read.get()

def hysteresis(self):
    #Atrial pulse width label
    hys_limit = tk.Label(self,text = 'Hysteresis', font = ('Montserrat',12),anchor = 'center')
    hys_limit.grid(row = 12, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    hys_limit_read = ttk.Combobox(self, width = 10) 
    hys_limit_read.grid(row = 12,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    hys_limit_read['values'] =(0,30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                 80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
    hys_limit_read.current(0)
    
    return hys_limit_read.get()

def rate_smoothing(self):
    #Atrial pulse width label
    global rate_smooth
    rate_smoothing = tk.Label(self,text = 'Rate Smoothing (%)', font = ('Montserrat',12),anchor = 'center')
    rate_smoothing.grid(row = 12, column = 1,sticky = 'we', pady = 10,padx =50 )
    
    #atrial_amp field input
    rate_smoothing_read = ttk.Combobox(self, width = 10) 
    rate_smoothing_read.grid(row = 12,column = 2,sticky ='W') 
    # Adding combobox drop down list 
    rate_smoothing_read['values'] =(0,3,6,9,12,15,18,21,25) 
    rate_smoothing_read.current(0)
    
    return rate_smoothing_read.get()




