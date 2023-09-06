import pandas as pd
import numpy as np
import datetime

class get_event:
	def __init__(self,alea_un,epis_un,portfolio_value):
		self.alea_un = alea_un
		self.epis_un = epis_un
		self.portfolio_value = portfolio_value
	def event_unit(self,x,txt):
		#if a huge draw down(3%) in 7 days, output it
		event_list = []
		last_day = x.shift(-1)
		tmp = x.values
		tmp = ((tmp/last_day)[-7:]-1) * 100
		tmp = tmp[tmp>=3]
		for i in range(tmp.shape[0]):
			text = 'Date: {0}, {2}({1})'.format(tmp.index[i].strftime("%Y-%m-%d"), round(tmp.values[i],3),txt)
			event_list.append(text)
		return event_list
	def loss_event(self):
		txt = 'Event: Huge loss over 3%'
		return self.event_unit(self.portfolio_value,txt)
	def alea_event(self):
		txt = 'Event: Huge change(%) in Aleatoric Un'
		return self.event_unit(self.alea_un,txt)
	def epis_event(self):
		txt = 'Event: Huge change(%) in Epistemic Un'
		return self.event_unit(self.epis_un,txt)
	def get_all_events(self):
		t1 = self.loss_event()
		t2 = self.alea_event()
		t3 = self.epis_event()
		return t1+t2+t3