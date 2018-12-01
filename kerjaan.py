import datetime
import re


###EMPLOYEE ID
employee_id = 0

##EMPLOYER ID
employer_id = 1000
class user:

	def __init__(self, name, age, address, email, phonenum, password):

		
		self.name = name
		self.age = age
		self.address = address
		self.email = email
		self.phonenum = phonenum
		self.password = password
		###SIMPAN OBJEK CV
		
	

	####UNTUK MENCARI EMAIL DAN PASSWORD LOGIN####
	def match(self, filter, filter2):
		return filter == self.email and filter2 == self.password
	
class cv:

	def __init__(self):

		###DUMMY DATA
		self.list_of_job_experience=[]
		self.list_of_education=[]

	def add_list_of_job_experience(self):
		job_experience=input('masukan job experience anda(ex : 2007-2009 BEKERJA DI MICROSOFT	)')
		self.list_of_job_experience.append(job_experience)
	
	def add_list_of_education(self):
		education=input('masukan edukasi anda(ex : 2007-2009 UPH TEKNIK INFORMATIKA	)')
		self.list_of_education.append(education)

	def print_my_cv(self):
		print('	Pengalaman kerja : ')
		print('	',self.list_of_job_experience)
		print('	Edukasi : ')
		print('	',self.list_of_education)


	

	




class employee(user):

	def __init__(self, name, age, address, email, phonenum, password):
		super().__init__( name, age, address, email, phonenum, password)
		global employee_id
		employee_id += 1
		self.id = employee_id
		self.c=cv()

	def print_employee_cv(self):
		print()
		
		print('	',self.name,"'s Curicculum Vitae")
		print('	Nama : ',self.name)
		print('	Umur : ',self.age)
		print('	Alamat : ',self.address)
		print('	Nomor telepon : ',self.phonenum)
		print('	Email : ',self.email)
		print(self.c.print_my_cv())
		

	

	
class employer(user):
	
	
	def __init__(self,  name, age, address, email, phone_num, password):
		super().__init__( name, age, address, email, phone_num, password)
		#####LIST DARI IKLAN YANG DIMILIKI EMPLOYER
		self.ads_list = []
		global employer_id
		employer_id +=1
		self.id = employer_id

		
	

	####TAMBAH IKLAN KE LIST
	def add_ads(self):
		title=input('judul iklan\n')
		category=input('category iklan\n')
		location=input('lokasi pekerjaan')
		employment_type=input('tipe employment\n')
		exp_years=input('minimum years of experience\n')
		qualification=input('kualifikasi\n')
		self.ads_list.append(ads(title,category,location,employment_type,exp_years,qualification))
	

	
	def print_ads_list_employee(self,employee_id):
		#####PRINT SEMUA IKLAN YANG DIPUNYA OLEH EMPLOYER
		###INDEX UNTUK LIST PEKERJAAN
		index=0
		for i in self.ads_list:
			print('\t',index,'. ',i.title,)
			print ('\t','Category : ',i.category)
			print ('\t','Location : ',i.location)
			print ('\t','Employment type : ',i.employment_type)
			print ('\t','Years of experience : ',i.exp_years)
			print ('\t','Qualification : ',i.qualification)
			print('\t','Posted on : ',i.posted)
			index=index+1

			

			for p in range(len(i.list_of_employee_applied)):
				
				if employee_id == i.list_of_employee_applied[p].id:
					if i.list_of_employee_applied_status[p]==True:
						print("	Anda diterima di iklan ini !")
					else:
						print("	Anda tidak/belum diterima di iklan ini !")


			
				
		
	


class ads:

	def __init__(self,title,category,location,employment_type,exp_years,qualification):
		

		##LIST DARI EMPLOYEE YANG APPLY
		self.list_of_employee_applied=[]
		##LIST DARI EMPLOYEE YANG APPLY employee[0]==employee_applied_status[0]
		self.list_of_employee_applied_status=[]
		
		self.title=title
		self.category=category
		self.location=location
		self.employment_type=employment_type
		self.exp_years=exp_years
		self.qualification=qualification
		self.posted=datetime.datetime.today().strftime('%Y-%m-%d')

	def add_employee(self,name, age, address, email, phonenum, password):
		self.list_of_employee_applied.append(employee(name, age, address, email, phonenum, password))

		##AWAL APPLY SET STATUS EMPLOYEE=FALSE
		self.list_of_employee_applied_status.append(False)
	

		

	
	
class catalog:

	def __init__(self):
		self.item=[]
		#self.item_employee = []

		##DUMMY DATA
		self.item.append(employer('PT.ANGKASA PURA', '11', 'address', 'email1', '22222222222', 'password'))
		self.item.append(employer('PT. NANI KORE', '11', 'address', 'email2', '3333333333', 'password'))
		self.item.append(employer('PT. SUBARASHI', '11', 'address', 'email3', '444444444', 'password'))
		self.item.append(employer('PT. HAZUKASHI', '11', 'address', 'email4', '555555555555', 'password'))
		self.item.append(employee('William', '11', 'address', 'email5', '66666666666', 'password'))
		self.item.append(employee('yoel', '11', 'address', 'email6', '77777777777', 'password'))
	

	
	
				
	def check_for_index(self,user_id):
		####-1 agar sesuai dengan list item[]
		index=(-1)
		
		for p in self.item:
			index=index+1
			if p.id==user_id:
				p.id=int(p.id)
				break

		return index

	### cek apakah employee==true or employer==False
	def check_account_type(self,user_index):
		user_index=int(user_index)
		check=type(self.item[user_index]) is employee
		return check

		

	###TAMBAH IKLAN(EMPLOYER)
	def add_ads(self,index_employer,account_type):
		
		if account_type==False:
			print(self.item[index_employer].name)
			self.item[index_employer].add_ads()

	###TAMPILKAN IKLAN(EMPLOYER)
	def display_ads(self,index_employer,account_type):
		
		if account_type==False:
			####INDEX UNTUK PELAMAR KERJA DI MENU
			index_iklan=0
			
			for i in self.item[index_employer].ads_list:
				index_employee=0
				print()
				print('	======iklan ke-',index_iklan,'======')
				print('	',i.title)
				print("	Category : ",i.category)
				print("	Location : ",i.location)
				print("	Employment type : ",i.employment_type)
				print("	Minimum years experience : ",i.exp_years)
				print("	Qualification : ",i.qualification)
				print()
				print("	List of Applicant : ")
				index_iklan=index_iklan+1


				for p in i.list_of_employee_applied:
					print('	',index_employee,'. ',p.name)
					print(p.print_employee_cv())
					print()
					
				index_employee=index_employee+1
	
				print()
				print()
##				print('\t',i.list_of_employee_applied[0].name)

	##TAMPILKAN IKLAN UNTUK EMPLOYEE
	def print_all_jobs(self,employee_id):
			print()
		####PRINT UNTUK LIST ITEM
			###INDEX NAMA PERUSAHAAN
			index=0
			for i in self.item:
			## PANGGIL FUNGSI PRINT		
				if i.id>=1000:
				##	print("check : ",checks)
				
					print ('ID : ',i.id,i.name)
				
					print() 
					i.print_ads_list_employee(int(employee_id))
					index=index+1

			print()


	###apply jobs untuk employee
	#def apply_jobs(self):
	#	index_perusahaan=input("input ID dari perusahaan")
	#	index_pekerjaan=input("input index dari pekerjaan")


########mengubah status accept/deny lamaran employee user_id=id dari employer
	def recruitment_process(self,user_index):
		checks=self.check_account_type(user_index)
		
		if checks==False:
			index_iklan=input('pilih index iklan')
			index_applicant=input('pilih index applicant')
		#	index_iklan=int(index_iklan)
		#	index_applicant=int(index_applicant)

			try:
				
				print('nama iklan : ',self.item[int(user_index)].ads_list[int(index_iklan)].title)  
					
				try:
   					print('nama aplicant : ',self.item[int(user_index)].ads_list[int(index_iklan)].list_of_employee_applied[int(index_applicant)].name)
					
					
				except IndexError:
					print('Tidak ada pelamar index ke-',index_applicant,'di index iklan ke-',index_iklan)
					return
				except ValueError:
					print("Index hanya terdiri dari angka")
					return
				
					
			except IndexError:
				print('Tidak ada index pekerjaan ke-',index_iklan)
				return
			except ValueError:
				print("Index hanya terdiri dari angka")
				return
			
				

			choice= input('do you want accept this applicant ? (y/n)')
			if(choice=='y' or choice=='Y'):
				print("The employee will be notified.")
				#############UBAH STATUS INDEX APPLICANT MENJADI TRUE(DITERIMA)
				self.item[int(user_index)].ads_list[int(index_iklan)].list_of_employee_applied_status[int(index_applicant)]=True
				print('anda menerima',self.item[int(user_index)].ads_list[int(index_iklan)].list_of_employee_applied[int(index_applicant)].name ,
				' ',self.item[int(user_index)].ads_list[int(index_iklan)].list_of_employee_applied_status[int(index_applicant)])
			else:
				return





		###check apakah employee atau employer
	#	if checks==False:





	###################ADD CV UNTUK EMPLOYEE
	def add_cv_employee(self,index_employee,account_type):
		if(account_type==True):
			self.item[index_employee].c.add_list_of_job_experience()
			
			self.item[index_employee].c.add_list_of_education()
			self.item[index_employee].print_employee_cv()

	############ PRINT CV UNTUK EMPLOYEE
	def print_cv(self,index_employee,account_type):
		if(account_type==True):
			self.item[index_employee].print_employee_cv()


	def apply_jobs(self,index_employee,account_type):

		if account_type==True:
			id_employer=input("Input id perusahaan di list yang diinginkan\n")
			index_pekerjaan=input("Input nomor pekerjaan di list yang diinginkan\n")

			

			### UBAH ID PERUSAHAAN JADI INDEX DI ARRAY ITEM
			try:
				index_employer=self.check_for_index(int(id_employer))
			except ValueError:
				print("index hanya angka")
				return
			##PARSE KE INT
			#index_employer_int=int(index_employer)
			#index_pekerjaan=int(index_pekerjaan)
			
			
			
			check_exists_employer=self.check_if_user_exists(int(index_employer))
	
			check_id=self.item[int(index_employer)].id


			if check_exists_employer==False and check_id>=1000:
				###tambahkan list of object employee ke object ads
				#self.item[index_employer]
				

				###ERROR HANDLING APABILA INDEX PEKERJAAN YANG DIPILIH TIDAK ADA
				try:
   					#print(self.item[index_employer].ads_list[index_pekerjaan])
					self.item[int(index_employer)].ads_list[int(index_pekerjaan)].list_of_employee_applied.append(self.item[int(index_employee)])   
					
					try:
   						self.item[int(index_employer)].ads_list[int(index_pekerjaan)].list_of_employee_applied_status.append(False)
					
					except IndexError:
						print('Tidak ada index pekerjaan :', int(index_pekerjaan), 'pada ', self.item[int(index_employer)].name)
					except ValueError:
						print("Index hanya terdiri dari angka")
					
				except IndexError:
					print('Tidak ada index pekerjaan :', int(index_pekerjaan), 'pada ', self.item[int(index_pekerjaan)].name)
				except ValueError:
					print("Index hanya terdiri dari angka")
					
		
			else:
				print("company ID/index pekerjaan salah")

	###cek apakah userid ada di list item[]
	def check_if_user_exists(self,id_employer):
		for i in self.item:
			if(i.id)==id_employer:
				return True
			else:
				return False
		

		
	def check_email_contains(self, email_address, characters, min_length=6):
		while True:
			for character in characters:
				if character not in email_address:
					email_address = input("Your email address must have '{}' in it\nPlease write your email address again: ".format(character))
					continue
			if len(email_address) <= min_length:
				email_address = input("Your email address is too short\nPlease write your email address again: ")
				continue
			return email_address

	def new_employee2(self):
		
		while True:
			name = input("Enter name: ")
			if not re.match("^[a-z]*$", name):
				print("Error! Only letters a-z allowed!")
			else:
				break
		while True:
			try:
				age = int(input("Please enter your age: "))
				break
			except ValueError:
  				print("invalid input!")
		while True:
			address = input("Enter a address: ")
			if len(address) < 20:
				print("Address is too short! try again")

			else:
				break
		apa = 0
		while apa==0:
			email = input("email address: ")
			characters = "@"
			for character in characters:
				if character in email:
					apa +=1
				else:
					print("invalid email!")
		
						

		while True:
			try:	
				phone_num = int(input("Enter Phone number: "))
				break
			except ValueError:
  				print("invalid input!")

		while True:
			password = input("Enter a password: ")
			if len(password) < 8:
				print("Make sure your password is at lest 8 letters")

			else:
				break
            

		self.item.append(employee(name, age, address, email, phone_num, password))
		print("Employee register success")

	def new_employer2(self):
			
		while True:
			name = input("Enter name: ")
			if not re.match("^[a-z]*$", name):
				print("Error! Only letters a-z allowed!")
			else:
				break
		while True:
			try:
				age = int(input("Please enter your age: "))
				break
			except ValueError:
  				print("invalid input!")
		while True:
			address = input("Enter a address: ")
			if len(address) < 20:
				print("Address is too short! try again")

			else:
				break
		apa = 0
		while apa==0:
			email = input("email address: ")
			characters = "@"
			for character in characters:
				if character in email:
					apa +=1
				else:
					print("invalid email!")
		
						

		while True:
			try:	
				phone_num = int(input("Enter Phone number: "))
				break
			except ValueError:
  				print("invalid input!")

		while True:
			password = input("Enter a password: ")
			if len(password) < 8:
				print("Make sure your password is at lest 8 letters")

			else:
				break
            

		
		
		self.item.append(employer(name, age, address, email, phone_num, password))
		print("Employer register success")
		
	




	def search(self, filter, filter2):        
        
		return [user for user in self.item if
                    user.match(filter, filter2)] 

	

	
	
