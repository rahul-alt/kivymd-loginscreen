from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
import webbrowser

from jnius import autoclass
from android import activity


mybuild='''
MDScreenManager
	Screen1:
	Screen2:


<Screen1>:
	name:'home'
	MDBoxLayout:
		orientation:'vertical'
		MDLabel:
			text:'English uk&'
			halign:'center'
		MDIconButton:
			icon:'github'
			cols:1
			icon_size:'30sp'
			pos_hint:{'center_x':0.5}
		MDTextField:
            id: username
            hint_text: "Username"
            icon_right: "account"
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            icon_right: "lock"
        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": 0.5 ,"center_y":0.8}
            on_release:app.check_login(username.text, password.text)
        MDLabel:
            text:'forget or signup'
            halign:'center'
        MDTopAppBar:
        	title:'create account'
			
			
<Screen2>:
	name:'next'
	MDNavigationLayout:
		orientation:'vertical'
		MDTopAppBar:
			title:''
			id:nav_draw
			pos_hint:{'top':1}
			md_bg_color:'black'
			left_action_items:[['menu', lambda x:nav_draw.set_state('toggle')]]
		MDScreenManager:
			MDScreen:
				MDBoxLayout:
					MDIconButton:
						icon:'facebook'
						pos_hint:{'center_y':0.5}
					MDTextField:
						text:'enter target'
						pos_hint:{'center_y':0.5}
					MDRaisedButton:
						text:'start attack'
						md_bg_color:'green'
						pos_hint:{'center_y':0.5}
						on_press:app.open_url('https://www.google.com')
				
		
		
		
	MDNavigationDrawer:
		id:nav_draw
		ScrollView:
			MDList:
				OneLineListItem:
					text:'follow me on'
				TwoLineListItem:
					text:'profile'
				ThreeLineListItem:
					text:'logout'
					bold:True
				OneLineListItem:
					text:'home'
					
		MDGridLayout:
			cols:1
			spacing:30
			MDIconButton:
				icon:'github'
				icon_size:'35sp'
			MDIconButton:
				icon:'account'
				icon_size:'35sp'
			MDIconButton:
				icon:'logout'
				icon_size:'35sp'
				on_press:root.manager.current='home'
			MDIconButton:
				icon:'home'
				icon_size:'35sp'
				on_press:nav_draw.set_state('close')
			ScrollView:
				MDList:
					OneLineListItem:
						text:'more tool avilable on github'
					TwoLineListItem:
						text:'https://github.com/rahul-alt/'
		
		
'''


	
	
class Screen1(MDScreen):
	pass


class Screen2(MDScreen):
	pass
	


class main(MDApp):
	def build(self):
		self.theme_cls.theme_style='Dark'
		build=Builder.load_string(mybuild)
		self.Intent = autoclass('android.content.Intent')
		self.Uri = autoclass('android.net.Uri')
		return build
		
		
	def check_login(self, username, password):
	           if username == "rahul" and password == "rahul":
	           	self.root.current = "next"
	           	
	           	
	def open_url(self, url):
	    intent = self.Intent(self.Intent.ACTION_VIEW, self.Uri.parse(url))
	    activity.mActivity.startActivity(intent)
		
		
main().run()