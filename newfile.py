from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

mybuild='''
MDScreenManager
	Screen1:
	Screen2:


<Screen1>:
	name:'home'
	MDBoxLayout:
		orientation:'vertical'
		MDRaisedButton:
			text:'Login'
			elevation:4
			pos_hint:{'center_x':0.5, 'center_y':0.5}
			on_press:root.manager.current='next'
			
			
			
<Screen2>:
	name:'next'
	MDNavigationLayout:
		MDTopAppBar:
			title:''
			id:nav_draw
			pos_hint:{'top':1}
			left_action_items:[['menu', lambda x:nav_draw.set_state('toggle')]]
		
		
	MDNavigationDrawer:
		id:nav_draw
		ScrollView:
			MDList:
				OneLineListItem:
					text:'@rahul-alt'
				TwoLineListItem:
					text:'follow me on github'
				FitImage:
					source:'image'
		
		
'''


	
	
class Screen1(MDScreen):
	pass


class Screen2(MDScreen):
	pass
	


class main(MDApp):
	def build(self):
		
		build=Builder.load_string(mybuild)
		
		return build
		
		
main().run()