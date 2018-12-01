import sys
from kerjaan import user, employee, employer, catalog,ads

name=''
class Menu:
	

	def __init__(self):
		self.catalog = catalog()
		self.login_status=False

		####NAMA USER
		self.user_name=''


		####TYPE USER TRUE=EMPLOYEE, FALSE=EMPLOYER
		self.account_type=False


		####INDEX USER DI LIST ITEM
		self.user_index=0


		self.user_id=0


		
		self.choices = {
				"1": self.new_account,
				"2": self.login,
				"3":self.logout,
				"4": self.quit,
				"5":self.add_ads,
				"6":self.display_ads,
				"7":self.apply,
				"8":self.accept_applicant,
				"9":self.add_cv,
				"10":self.print_cv,
				"11":self.view_jobs_applied
				}

	def display_menu(self):
		##print('display_menu')
		
	##	print(self.login_status)
		if self.login_status==False:
			print("""
					Library Menu
					1. Make new account 
					2. LOGIN
					3. LOGOUT
					4. KELUAR
					
					""")
		elif self.login_status==True and self.account_type==True:
			print("Hi",self.user_name,"""
					Library Menu
					1. Buat Akun Baru
					3. LOGOUT
					4. QUIT
					7. LAMAR PEKERJAAN(EMPLOYEE)
					9. TAMBAH CV SAYA(EMPLOYEE)
					10. TAMPILKAN CV SAYA(EMPLOYEE)
					11. LIHAT SEMUA PEKERJAAN(EMPLOYEE)
					""")

		elif self.login_status==True and self.account_type==False:
			print("Hi",self.user_name,"""
					Library Menu
					1. Make new account 
					3. LOGOUT
					4. QUIT
					5. TAMBAH IKLAN(EMPLOYER)
					6. TAMPILKAN IKLAN SAYA(EMPLOYER)
					8. TERIMA APLICANT(EMPLOYER)
					
					""")
		

	def run(self):
		while True:
			self.display_menu()
			choice = input("Enter an option: ")
			action = self.choices.get(choice)
			if action:
				action()
		else:
				print("{0} is not a valid choice".format(choice))
	def new_account(self):
		#while True:
			#try:
		pilihan = input("1. Employee \n2. Employeer \n ")
		if pilihan == "1":
				
				self.catalog.new_employee2()
				
		elif pilihan == "2":
				self.catalog.new_employer2()
		
		#elif pilihan == "3":
				
				#self.catalog.print_all_jobs()
				#self.catalog.apply_jobs()

			#except:
				#print ("invalid input try again!")
	def identifikasi(self, users=None):              
		for user in users:           
			##print(user.id) 
			if user.id <=1000:
				print ("employee")
				#pilihan1 = ("")
			elif user.id >1000:
				print ("employer")
##		print(self.catalog.check_for_index(user.id))
		index_user=self.catalog.check_for_index(user.id)
		self.login_status=True
		self.user_name=self.catalog.item[index_user].name
		
		###SET INDEX WHERE IS THE OBJECT SAVED IN item[]
		self.user_index=(self.catalog.check_for_index(user.id))
		

		###SET ACCOUNT TYPE EMPLOYEE OR EMPLOYER
		self.account_type=(self.catalog.check_account_type(index_user))
		

		self.user_id=user.id

	def add_cv(self):
		self.catalog.add_cv_employee(self.user_index,self.account_type)

	
	def print_cv(self):
		self.catalog.print_cv(self.user_index,self.account_type)

	def view_jobs_applied(self):
		self.catalog.print_all_jobs(self.user_id)



		
				
	def login(self):
		
		filter = input("input email: ")
		filter2 =input ("input password: ")
		notes = self.catalog.search(filter,filter2)
		if notes:        
			self.identifikasi(notes)
		else:
			print("Wrong email or password")
		
	def apply(self):
		self.catalog.print_all_jobs(self.user_id)
		self.catalog.apply_jobs(self.user_index,self.account_type)

	def accept_applicant(self):
		self.catalog.recruitment_process(self.user_index)


	def add_ads(self):
		#### MENAMBAHKAN IKLAN SESUAI EMPLOYER YANG LOGIN
		##print(self.user_index)
		#print('account type job:',self.account_type, " ",self.user_index)
		self.catalog.add_ads(self.user_index,self.account_type)
	

	def display_ads(self):
		######MENAMPILKAN IKLAN YANG DIMILIKI OLEH EMPLOYER
		self.catalog.display_ads(self.user_index,self.account_type)
	

	def logout(self):
		############SESI LOGIN HAPUS
		self.login_status=False
		self.user_name=''


	def quit(self):
		sys.exit()


if __name__ == "__main__":
	Menu().run()

