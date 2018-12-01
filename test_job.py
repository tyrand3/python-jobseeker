import sys
from kerjaan import user, employee, employer, catalog,ads

c=catalog()
name='yoel'
email='email6@gmail.com'
name2='william'
email2='email7@gmail.com'

title='Dicari SPG UNTUK EVENT'
category='others'
location='Jakarta'
employment_type='full_time'
exp_years=5
qualification='deegre'

c.item.append(employee(name, '11', 'address', email, 'phone_num', 'password'))
c.item.append(employer(name2, '11', 'address', email2, 'phone_num', 'password'))
c.item[7].ads_list.append(ads(title,category,location,employment_type,exp_years,qualification))

def test_add_employee_name():
    assert c.item[6].name==name


####ID <1000 == OBJECT EMPLOYEE, >1000 == OBJECT EMPLOYER
def test_employee_id():
    assert c.item[6].id<=1000


def test_employer_id():
    assert c.item[7].id>=1000


def test_add_employee_email():

   
    assert c.item[6].email==email

def test_add_ads_title():
    assert c.item[7].ads_list[0].title == title


#####CEK WHERE IS THE DATA SAVED IN THE ARRAY
def test_index_item():

    index=c.check_for_index(c.item[6].id)
    assert index == 6


######IF RETURN TRUE == EMPLOYEE OBJECT
def test_account_type_employee():
    flag=c.check_account_type(6)
    assert flag == True

def test_account_type_employer():
    flag=c.check_account_type(7)
    assert flag == False


### TES TAMBAH IKLAN
def test_apply_employee():
    account_type=c.check_account_type(6)
    if account_type==True:
        id_employer=1005
        index_pekerjaan=0
        index_employee=6
			
			

			### UBAH ID PERUSAHAAN JADI INDEX DI ARRAY ITEM
        index_employer=c.check_for_index(id_employer)

			##PARSE KE INT
			#index_employer=int(index_employer)
			#index_pekerjaan=int(index_pekerjaan)
			
			
        check_exists_employer=c.check_if_user_exists(int(index_employer))
        check_id=c.item[int(index_employer)].id
			
        if check_exists_employer==False and check_id>=1000:
				###tambahkan list of object employee ke object ads
				#self.item[index_employer]
				

				###ERROR HANDLING APABILA INDEX PEKERJAAN YANG DIPILIH TIDAK ADA
            
                #print(self.item[index_employer].ads_list[index_pekerjaan])
            c.item[int(index_employer)].ads_list[int(index_pekerjaan)].list_of_employee_applied.append(c.item[int(index_employee)])   
					
                
            c.item[int(index_employer)].ads_list[int(index_pekerjaan)].list_of_employee_applied_status.append(False)

            assert c.item[int(index_employer)].ads_list[int(index_pekerjaan)].list_of_employee_applied[0].name == name 
              
		
		
        else:
            print("company ID/index pekerjaan salah")


def test_employee_status():
    
    print(c.item[7].ads_list[0].list_of_employee_applied_status[0])
    assert c.item[7].ads_list[0].list_of_employee_applied_status[0] == False
    
### TES FUNGSI RECRUITMENT PROCESS KERJAAN.PY LINE KE-319
def test_recruitment_process():
    user_index=7
   	
    
    index_iklan=0
    index_applicant=0
    ###DARI KERJAAN.PY LINE 319
    c.item[user_index].ads_list[index_iklan].list_of_employee_applied_status[index_applicant]=True
    
    assert c.item[7].ads_list[0].list_of_employee_applied_status[0] == True 
		





