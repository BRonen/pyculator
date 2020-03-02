import PySimpleGUI as sg

sg.theme('DarkAmber')

WIN_W = 30
WIN_H = 50

menu_layout = [
               ['File', ['a', '---', 'Exit']],
               ['Tools', []],
               ['Help', ['About', 'Test']]
              ]

layout = [
          [sg.Menu(menu_layout)],
          [
          	sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='_BOX_'),
          	sg.Button('<-', font=('Consolas', 20), key='_BACKARROW_'),
          	sg.Button(' C', font=('Consolas', 20), key='_C_')
          ],
          [
          	sg.Button('7', font=('Consolas', 20), key='_SEVEN_'),
          	sg.Button('8', font=('Consolas', 20), key='_EIGHT_'),
          	sg.Button('9', font=('Consolas', 20), key='_NINE_'),
          	sg.Button('+', font=('Consolas', 20), key='_PLUS_'),
          	sg.Button('*', font=('Consolas', 20), key='_TIMES_')
          ],
          [
          	sg.Button('4', font=('Consolas', 20), key='_FOUR_'),
          	sg.Button('5', font=('Consolas', 20), key='_FIVE_'),
          	sg.Button('6', font=('Consolas', 20), key='_SIX_'),
          	sg.Button('-', font=('Consolas', 20), key='_MINUS_'),
          	sg.Button('/', font=('Consolas', 20), key='_DIVIDED_')
          ],
          [
          	sg.Button('1', font=('Consolas', 20), key='_ONE_'),
          	sg.Button('2', font=('Consolas', 20), key='_TWO_'),
          	sg.Button('3', font=('Consolas', 20), key='_THREE_'),
		sg.Button('0', font=('Consolas', 20), key='_ZERO_'),
          	sg.Button('=', font=('Consolas', 20), key='_RESULT_')
          ]
         ]

class App():
	def __init__(self):
		self.window = sg.Window('Pyculator', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
		self.result = 0
		self.oper = ''
		self.window.read(timeout=1)
		#self.window['_BOX_'].expand(expand_x=True)
		for i in range(1, 5):
			for button in layout[i]:
				button.expand(expand_x=True, expand_y=True)

	def about(self):
		sg.PopupQuick('"Just a notepad, use it!" - Me', auto_close=False)
    
	def test(self):
		sg.PopupQuick('"Hello world!" - A bored dev', auto_close=False)
		
	def resulter(self):
		print(self.result, self.values.get('_BOX_'))
		if self.oper == '+':
			return float(self.result) + float(self.values.get('_BOX_'))
		if self.oper == '-':
			return float(self.result) - float(self.values.get('_BOX_'))
		if self.oper == '*':
			return float(self.result) * float(self.values.get('_BOX_'))
		if self.oper == '/':
			return float(self.result) / float(self.values.get('_BOX_'))
		
	def Start(self):
		while True:
			event, self.values = self.window.read()
			print(event, self.result, self.oper)
			if event in (None, 'Exit', 'Escape:9'):
				break
			if event in ('About',):
				self.about()
			if event in ('Test',):
				self.test()

			if event in ('_ONE_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='1')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'1')
			if event in ('_TWO_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='2')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'2')
			if event in ('_THREE_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='3')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'3')
			if event in ('_FOUR_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='4')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'4')
			if event in ('_FIVE_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='5')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'5')
			if event in ('_SIX_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='6')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'6')
			if event in ('_SEVEN_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='7')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'7')
			if event in ('_EIGHT_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='8')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'8')
			if event in ('_NINE_',):
				if self.values.get('_BOX_') == '0':
					self.window['_BOX_'].update(value='9')
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'9')
			if event in ('_ZERO_',):
				if self.values.get('_BOX_') == '0':
					pass
				else:
					self.window['_BOX_'].update(value=self.values.get('_BOX_')+'0')
			if event in ('_C_',):
				self.result = 0
				self.window['_BOX_'].update(value=self.result)
			if event in ('_BACKARROW_',):
				self.window['_BOX_'].update(value=self.values.get('_BOX_')[:-1])
			if event in ('_PLUS_',):
				if self.oper != '':
					self.result = self.resulter()
				else:
					self.oper = '+'
					self.result = self.values.get('_BOX_')
				self.window['_BOX_'].update(value='')
			if event in ('_MINUS_',):
				if self.oper != '':
					self.result = self.resulter()
				else:
					self.oper = '-'
					self.result = self.values.get('_BOX_')
				self.window['_BOX_'].update(value='')
			if event in ('_TIMES_',):
				if self.oper != '':
					self.result = self.resulter()
				else:
					self.oper = '*'
					self.result = self.values.get('_BOX_')
				self.window['_BOX_'].update(value='')
			if event in ('_DIVIDED_',):
				if self.oper != '':
					self.result = self.resulter()
				else:
					self.oper = '/'
					self.result = self.values.get('_BOX_')
				self.window['_BOX_'].update(value='')
			if event in ('_RESULT_',):
				self.result = self.resulter()
				self.window['_BOX_'].update(value=self.result)
				self.result = 0
				self.oper = ''

App().Start()
