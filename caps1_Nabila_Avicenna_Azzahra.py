
from tabulate import tabulate
import maskpass
import math

masterdata = {
    "id": [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 
           13001, 13002, 14001, 14002, 12001, 12002],
    "nama": ["Rani Kusuma Putri", "Jaya Perdana", "Lina Anggraini", "Dika Pratama", "Kiran Mahendra", "Niko Wibowo", 
            "Sari Ramadhani", "Indra Saputra", "Tia Maharani", "Kiki Anjani", "Ara Prameswari", "Bima Wiratama","Candra Aditya", "Dewa Arjuna", "Eka Nugraha", "Fajar Widodo"],
    "dept": ["Human Resource", "Human Resource", "Human Resource", "Human Resource", "Human Resource", 
             "Human Resource", "Human Resource", "Human Resource", "Human Resource", "Human Resource", 
             "Business Development", "Business Development", "Information Technology", "Information Technology", 
             "Sales & Marketing", "Sales & Marketing"],
    "lama_kerja": [10, 9, 9, 7, 6, 5, 5, 3, 3, 2, 1, 2, 5, 8, 3, 5],
    "level": ["Head", "Senior Manager", "Senior Manager", "Manager", "Manager", "Assistant Manager", "Assistant Manager", "Specialist", "Specialist", "Staff", "Staff", "Specialist", "Assistant Manager", "Senior Manager", "Specialist", "Manager"],
    "jenis_kelamin": ["P", "L", "P", "L", "P", "L", "P", "L", "P", "P", 
                      "P", "L", "L", "L", "P", "L"],  
    "marital_status": ["Menikah", "Menikah", "Menikah", "Cerai", "Belum menikah", "Menikah", "Belum menikah", "Belum menikah", "Cerai", "Belum menikah", 
                       "Belum menikah", "Belum menikah", "Menikah", "Menikah", "Belum menikah", "Belum menikah"],  
    "fte": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    "leadership": [75, 85, 70, 90, 60, 82, 74, 88, 65, 78, 92, 67, 83, 69, 81, 77],
    "review360": [80, 78, 75, 85, 65, 79, 76, 84, 70, 80, 89, 73, 85, 74, 83, 79],
    "kpi": [80, 4, 51, 6, 10, 148, 88, 156, 100, 107, 30, 167, 113, 104, 124, 23],
    "nilai_karyawan": [79.25, 42.05, 62.25, 46.25, 36.75, 113.95, 81.7, 120.6, 84.25, 93.2, 59.95, 119.1, 98.7, 88.25, 103.2, 50.7],
    "kelayakan": ["Tidak layak", "Tidak layak", "Tidak layak", "Tidak layak", "Tidak layak", "Layak", "Tidak layak", "Layak", "Tidak layak", "Layak", "Tidak layak", "Layak", "Layak", "Layak", "Layak", "Tidak layak"],
    "gaji_pokok": [0, 40000000, 40000000, 30000000, 27000000, 23000000, 23000000, 15000000, 15000000, 8000000, 5000000, 11500000, 23000000, 35500000, 15000000, 24000000],
    "bonus": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    "status": ["Aktif", "Aktif", "Aktif", "Aktif", "Aktif", "Aktif", "Aktif", "Aktif", 
               "Aktif", "Aktif", "Aktif", "Aktif", "Aktif", "Aktif", "Aktif", "Aktif"]
}

offboarding_table={
    "id":[],
    "nama":[],
    "dept":[],
    "aset":[],
    "hutang":[],
    "handover":[],
    "status":[]
}

perhitungan_dept={
    10: 10,
    13: 2,
    14: 2,
    12: 2
    }

list_status_perkawinan=["Belum menikah","Menikah","Cerai"]
list_jenis_kelamin=["P","L"]
list_fte=["Full time","Non-full time"]
list_dept=["Human Resource","Finance","Sales & Marketing","Information Technology","Operation","Legal","Procurement","Logistics","Engineering","Business development","Audit"]
list_code_dept=[10,11,12,13,14,15,16,17,18,19,20]
list_level=["Staff", "Specialist", "Assistant Manager", "Manager", "Senior Manager", "Head"]
sop_requirements = {
    "Staff": [1,2],              # Max 2 years for Staff
    "Specialist": [2,3],         # Max 3 years for Specialist
    "Assistant Manager": [3,5],  # Max 5 years for Assistant Manager
    "Manager": [5,7],            # Max 7 years for Manager
    "Senior Manager": [7,9],      # Max 9 years for Senior Manager
    "Head": [10,60]
}
permission_password={"id":[10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010],
                     "password":[10001123, 10002123, 10003123, 10004123, 10005123, 10006123, 10007123, 10008123, 10009123, 10010123]}
list_permission_onboarding=[10001, 10002, 10003, 10008, 10009, 10010]
list_permission_performance=[10001, 10002, 10003, 10004, 10005, 10006]
list_permission_payroll=[10001, 10002, 10003, 10004, 10005]
list_permission_offboarding=[10001, 10002, 10003, 10006, 10007, 10008]

data = []
option = []


###### print onboarding, performance, payroll ######

def print_table(nama_table):
    column_option=[]

    if nama_table == "onboarding_table":
        column_option = ["id", "nama", "dept", "lama_kerja", "level", "jenis_kelamin", "marital_status", "fte", "status"]
        header = ["ID", "Nama", "Departemen", "Lama Kerja", "level", "Jenis Kelamin", "Status Nikah", "FTE", "Status"]
    elif nama_table == "performance_table":
        column_option = ["id", "nama", "dept", "lama_kerja", "leadership", "review360", "kpi", "nilai_karyawan", "kelayakan", "status"]
        header = ["ID", "Nama", "Departemen", "Lama Kerja", "Leadership", "Review 360˚", "KPI", "Nilai Akhir", "Kelayakan", "Status"]
    elif nama_table == "payroll_table":
        column_option = ["id", "nama", "dept", "lama_kerja", "level", "fte", "nilai_karyawan", "gaji_pokok", "bonus"]
        header = ["ID", "Nama", "Departemen", "Lama Kerja", "level", "FTE", "Nilai Akhir", "Gaji Pokok", "Bonus"]
    

    data = []
    for i in range(len(masterdata["id"])):  # Asumsi jumlah data didasarkan pada panjang kolom "id"
        row = []
        for col in column_option:
            if (col == "gaji_pokok" or col == "bonus") and (type(masterdata[col][i]) == int):
                row.append(f"Rp {masterdata[col][i]:,}") # Mengakses nilai untuk setiap kolom yang ada di column_option   
            else:
                row.append(masterdata[col][i]) # Mengakses nilai untuk setiap kolom yang ada di column_option
        data.append(row)

    # Mencetak tabel
    print("\n")
    if nama_table == "onboarding_table":
        print(" \t\t\t\t\t\t    Onboarding Master Data Table    \t\t\t\t\t\t   ")
    elif nama_table == "performance_table":
        print(" \t\t\t\t\t\t\t   Performance Data Table\t\t\t\t\t\t\t ")
    elif nama_table == "payroll_table":
        print("\t\t\t\t\t\t\tPayroll Data Table\t\t\t\t\t\t      ")
    print(tabulate(data, headers=header, tablefmt="mixed_grid", colalign=("center", "left")))

###### ONBOARDING ######

# input new
def new_data_onboarding():
    while True:
        # add nama
        while True:
            new_data_nama=((input("\nMasukkan nama karyawan: ")).strip()).title()
            if new_data_nama == "":
                print(f'''
                    {"─"*27}
                           Invalid request
                      Nama tidak boleh kosong
                    {"─"*27}''')
            else:
                break

        masterdata["nama"].append(new_data_nama)

        # add dept sesuai list
        data = [[list_code_dept[i], list_dept[i]] for i in range(len(list_dept))]
        # Display the table
        print("\n")
        print(tabulate(data, headers=["Kode","Departemen"], tablefmt="simple_outline", colalign=("center", "left")))
        # input dept sesuai kode
        add_code_dept = validasi_input_list(list_code_dept, "\nMasukkan kode departemen karyawan: ", "\nInvalid request\nMasukkan sesuai tabel\n")
        
        # translate kode ke dept, add ke table onboarding
        idx_dept = list_code_dept.index(add_code_dept) # identify dept based on index
        add_onb_dept = list_dept[idx_dept] # add dept
        masterdata["dept"].append(add_onb_dept) # add to onb table
        
        # hitung jumlah orang per dept untuk 3 digit akhir on id
        if add_code_dept not in perhitungan_dept:
            perhitungan_dept[add_code_dept]=1
        else:
            perhitungan_dept[add_code_dept]+=1
        
        # add 2 digit awal id based on dept
        add_masterdata_id=(f"{add_code_dept}{perhitungan_dept[add_code_dept]:03d}")
        
        masterdata["id"].append(add_masterdata_id)
        
        # add lama kerja & level
        while True:
            try:
                add_masterdata_lamakerja=float(input("\nMasukkan lama kerja karyawan: "))
                add_masterdata_level=input("\nMasukkan level karyawan: ").title()

                if add_masterdata_level in sop_requirements:
                    max_years = sop_requirements[add_masterdata_level][1]
                    min_years = sop_requirements[add_masterdata_level][0]
                    add_masterdata_lamakerja = math.floor(add_masterdata_lamakerja)

                    if add_masterdata_lamakerja > max_years or add_masterdata_lamakerja < min_years:
                        print(f"\nLama kerja di luar batas yang diizinkan untuk level ini sesuai SOP.\nKaryawan dengan level {add_masterdata_level} harus memiliki lama kerja minimal {min_years} tahun dan maksimal {max_years} tahun.")
                        data = [[i+1, key, item[0], item[1]] for i, (key, item) in enumerate(sop_requirements.items())]
                        print("\n")
                        print(tabulate(data, headers=["No", "Level", "Minimum Lama Kerja (Tahun)", "Maksimum Lama Kerja (Tahun)"], tablefmt="simple_outline", colalign=("center", "left", "center", "center")))

                    else:
                        masterdata["lama_kerja"].append(math.floor(add_masterdata_lamakerja))
                        masterdata["level"].append(add_masterdata_level)
                        break
                else:
                    print(f'''
                        {"─"*45}
                                        Invalid request
                        Masukkan level sesuai dengan SOP PT SINAU
                        {"─"*45}''')
                    
                    data = [[i+1, key, item[0], item[1]] for i, (key, item) in enumerate(sop_requirements.items())]
                    print("\n")
                    print(tabulate(data, headers=["No", "Level", "Minimum Lama Kerja (Tahun)", "Maksimum Lama Kerja (Tahun)"], tablefmt="simple_outline", colalign=("center", "left", "center", "center")))
            
            except ValueError:
                print(f'''
                        {"─"*45}
                                        Invalid request
                        Masukkan level sesuai dengan SOP PT SINAU
                        {"─"*45}''')                

        # add gender
        new_jenis_kelamin = validasi_input_list(list_jenis_kelamin, "\nMasukkan jenis kelamin (p/l): ", "\nInvalid request\nMasukkan P atau L")
        masterdata["jenis_kelamin"].append(new_jenis_kelamin)

        # add marriage status
        new_marital_status = validasi_input_list(list_status_perkawinan,"\nMasukkan status kawin (Menikah, Belum Menikah, Cerai):", "\nInvalid request\nMasukkan sesuai opsi")
        masterdata["marital_status"].append(new_marital_status)

        # add FTE
        new_fte = validasi_input_list([1,0],"\nMasukkan status kepegawaian (Full time : 1, Non-full time : 0): ", "\nInvalid request\nMasukkan sesuai opsi")

        # new_fte = validasi_input_list(list_fte,"Masukkan status kepegawaian (Full time : 1, Non-full time : 0):", "\nInvalid request\nMasukkan sesuai opsi")
        
        # if new_fte=="Full time":
        #     new_fte=1
        # else:
        #     new_fte==0
        masterdata["fte"].append(new_fte)
        
        # add default value
        masterdata["nilai_karyawan"].append("0")
        masterdata["leadership"].append("0")
        masterdata["review360"].append("0")
        masterdata["kpi"].append("0")
        masterdata["kelayakan"].append("0")
        masterdata["gaji_pokok"].append("0")
        masterdata["bonus"].append("0")
        masterdata["status"].append("Aktif")

        # update validation
        while True:
            try:
                input_validasi=(input("\nApakah Anda ingin input data baru lagi? (y/n): ")).capitalize()
                
                if input_validasi == "N" or input_validasi == "Y":
                    break
                else:
                    print(f'''
                        {"─"*20}
                           Invalid request
                             Masukkan Y/N
                        {"─"*20}
                        ''')
                    
            except ValueError:
                print(f'''
                        {"─"*20}
                           Invalid request
                             Masukkan Y/N
                        {"─"*20}
                        ''')
    
        if input_validasi=="N":
            print(f'''
                        {"─"*20}
                           Data tersimpan
                        {"─"*20}
                        ''')
            break
       
# edit
def edit_onboarding():
    while True:

        id_to_edit = int(input("\nMasukkan ID karyawan yang datanya ingin Anda edit: "))

        if id_to_edit in masterdata["id"]:
            idx_masterdata = masterdata["id"].index(id_to_edit) # look for the index in masterdata

            # Display edit option table
            list_edit_onb=["Nama","Departemen","Lama Kerja","Jenis Kelamin","Marital Status","FTE"]
            data = [[i+1, list_edit_onb[i]] for i in range(len(list_edit_onb))]
            print("\n")
            print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

            pilih_edit_onb = int(input("Masukkan opsi data yang ingin diedit: "))

            # edit nama
            if pilih_edit_onb==1:
                new_nama = (input("\nMasukkan nama: "))
                # update masterdata
                masterdata["nama"][idx_masterdata]=new_nama   
            # edit dept
            elif pilih_edit_onb==2:
                # add dept sesuai list
                data = [[list_code_dept[i], list_dept[i]] for i in range(len(list_dept))]
                # Display the table
                print(tabulate(data, headers=["Kode","Departemen"], tablefmt="simple_outline", colalign=("center", "left")))
                new_dept= validasi_input_list(list_code_dept, '\nMasukkan kode departemen: ', "\nInvalid request\nMasukkan sesuai tabel")
                idx_dept=list_code_dept.index(new_dept)
                masterdata["dept"][idx_masterdata]=list_dept[idx_dept]
            # edit lama kerja dan level karyawan
            elif pilih_edit_onb==3:
                while True:
                    new_lama_kerja=float((input("\nMasukkan lama kerja karyawan: ")))
                    new_level=input("\nMasukkan level karyawan: ").title()

                    if new_level in sop_requirements:
                        max_years = sop_requirements[new_level][1]
                        min_years = sop_requirements[new_level][0]
                        new_lama_kerja = math.floor(new_lama_kerja)

                        if new_lama_kerja > max_years or new_lama_kerja < min_years:
                            print(f"\nLama kerja di luar batas yang diizinkan untuk level ini sesuai SOP.\nKaryawan dengan level {new_level} harus memiliki lama kerja minimal {min_years} tahun dan maksimal {max_years} tahun.")
                            data = [[i+1, key, item[0], item[1]] for i, (key, item) in enumerate(sop_requirements.items())]
                            print("\n")
                            print(tabulate(data, headers=["No", "Level", "Minimum Lama Kerja (Tahun)", "Maksimum Lama Kerja (Tahun)"], tablefmt="simple_outline", colalign=("center", "left", "center", "center")))

                        else:
                            masterdata["lama_kerja"][idx_masterdata]=new_lama_kerja
                            masterdata["level"][idx_masterdata]=new_level
                            break
                    else:
                        print(f'''
              {"─"*45}
                           Invalid request
                Masukkan level sesuai dengan SOP PT SINAU.
              {"─"*45}''')
                        data = [[i+1, key, item[0], item[1]] for i, (key, item) in enumerate(sop_requirements.items())]
                        print(tabulate(data, headers=["No", "Level", "Minimum Lama Kerja (Tahun)", "Maksimum Lama Kerja (Tahun)"], tablefmt="simple_outline", colalign=("center", "left", "center", "center")))
            # edit jenis kelamin
            elif pilih_edit_onb==4:
                new_jenis_kelamin = validasi_input_list(list_jenis_kelamin, "\nMasukkan jenis kelamin (p/l): ", "\nInvalid request\nMasukkan P atau L")
                masterdata["jenis_kelamin"][idx_masterdata]=new_jenis_kelamin    
            # edit marital status
            elif pilih_edit_onb==5:
                new_marital_status = validasi_input_list(list_status_perkawinan,"\nMasukkan status kawin (Menikah, Belum Menikah, Cerai):", "\nInvalid request\nMasukkan sesuai opsi")
                masterdata["marital_status"][idx_masterdata]=new_marital_status
            # edit status kepegawaian
            elif pilih_edit_onb==6:
                new_fte = validasi_input_list([1,0],"\nMasukkan status kepegawaian (Full time : 1, Non-full time : 0): ", "\nInvalid request\nMasukkan sesuai opsi")
                masterdata["fte"][idx_masterdata]=new_fte
                
            # validasi
            validasi_edit=(input("\nApakah Anda ingin mengubah data lain?  (y/n): ")).capitalize()
        
            if validasi_edit=="N":
                break
            elif validasi_edit=="Y":
                continue
            else:
                print(f'''
                        {"─"*20}
                           Invalid request
                             Masukkan Y/N
                        {"─"*20}''')
                break
                
        else: 
            print(f'''
                    {"─"*27}
                           Invalid request
                      ID tidak dapat ditemukan
                    {"─"*27}''')
            break
            
# delete
def delete_from_onboarding():
    column_option = ["id", "nama", "dept", "lama_kerja", "level", "jenis_kelamin", "marital_status", "fte", "status"]
    header = ["ID", "Nama", "Departemen", "Lama Kerja", "Level", "Jenis Kelamin", "Status Nikah", "FTE", "Status"]

    id_del = int(input("\nMasukkan ID yang datanya ingin anda hapus: "))

    if id_del in masterdata["id"]:
        idx_masterdata = masterdata["id"].index(id_del)
        data = [masterdata[key][idx_masterdata] for key in column_option]
        print(tabulate([data], headers=header, tablefmt="fancy_grid"))
        validasi_del = input("Apakah Anda yakin ingin menghapus data di atas? (y/n): ").capitalize()
        if validasi_del == "Y":
            for key in masterdata.keys():
                del masterdata[key][idx_masterdata]
        else:
            print("\nData batal dihapus")
        
    else:
                print(f'''
                    {"─"*27}
                           Invalid request
                      ID tidak dapat ditemukan
                    {"─"*27}''')

###### PERFORMANCE ######

# edit
def edit_performance():
    while True:

        id_to_edit = int(input("\nMasukkan ID karyawan yang datanya ingin Anda edit: "))
        
        if id_to_edit in masterdata["id"]:
            
            idx_perf = masterdata["id"].index(id_to_edit) # print index

            while True:
                # Display edit option table
                list_data_perf = ["Leadership", "Review 360˚", "KPI"]
                data = [[i+1, list_data_perf[i]] for i in range(len(list_data_perf))]

                print("\n")
                print(tabulate(data, headers=["No","Penilaian"], tablefmt="simple_outline", colalign=("center", "left")))
                
                # Edit masterdata
                pilih_edit_perf=int(input("Masukkan nomor opsi data yang ingin diedit: "))
                if pilih_edit_perf==1:
                    new_leadership = validasi_input_list(range(1,101),"Masukkan nilai Leadership baru (0-100): ", "\nInvalid request\nMasukkan 1-100")
                    masterdata["leadership"][idx_perf] = new_leadership

                elif pilih_edit_perf==2:
                    new_review360 = validasi_input_list(range(1,101),"Masukkan nilai Review 360˚ baru (0-100): ", "\nInvalid request\nMasukkan 1-100")
                    masterdata["review360"][idx_perf] = new_review360

                elif pilih_edit_perf==3:
                    new_kpi = validasi_input_list(range(1,201),"Masukkan nilai KPI baru (0-200): ", "\nInvalid request\nMasukkan 1-200")
                    masterdata["kpi"][idx_perf] = new_kpi

                else:
                                    print(f'''
                        {"─"*20}
                           Invalid request
                             Masukkan 1-3
                        {"─"*20}''')
        
                # Nilai Akhir formula
                leadership_value=float(masterdata["leadership"][idx_perf])
                review360_value=float(masterdata["review360"][idx_perf])
                kpi_value=float(masterdata["kpi"][idx_perf])

                masterdata["nilai_karyawan"][idx_perf] = (leadership_value*0.15 + review360_value*0.35 + kpi_value*0.5) # nilai akhir karyawan
                
                print(f"\nData performance karyawan dengan ID {id_to_edit} telah diperbarui.")
                
                # Kelayakan
                if masterdata["nilai_karyawan"][idx_perf]>=85:
                    masterdata["kelayakan"][idx_perf]="Layak"
                else:
                    masterdata["kelayakan"][idx_perf]="Tidak layak"

                validasi_edit=(input("\nApakah Anda ingin mengubah data lain?  (y/n): ")).capitalize()
                if validasi_edit=="N":
                    break
                elif validasi_edit=="Y":
                    continue
                else:
                    print(f'''
                        {"─"*20}
                           Invalid request
                             Masukkan Y/N
                        {"─"*20}''')
                    break

            if validasi_edit=="N":
                break

        else:
            print("ID tidak ditemukan di performance data.")

# filter layak promosi
def promotion_approval():
    data = transform_table("performance_sorted")
    
    filtered_data = list(filter(lambda transformed_table: transformed_table["Kelayakan"] == "Layak", data))            
                
    if len(filtered_data) != 0:
        print('''\n
        Kepada Yth. Head Departemen Human Resource Management,

        Bersama email ini, saya sampaikan daftar karyawan yang, berdasarkan hasil penilaian performa terbaru, layak dipertimbangkan untuk promosi. 
        Daftar ini mencakup karyawan yang telah menunjukkan kinerja dan komitmen yang sangat baik serta memenuhi kriteria kelayakan yang ditetapkan.

        Berikut adalah daftar karyawan yang direkomendasikan untuk promosi:
        ''')
        print(tabulate(filtered_data, headers="keys", tablefmt="simple_outline"))
        print('''
        Terima kasih.
              
        Best Regards,
        HR Performance and Development Team\n''')
        
        validasi_list = input("Kirim ke Head HR? (y/n): ").capitalize()
        if validasi_list == "Y":
            print("\nEmail terkirim\n")
        elif validasi_list =="N":
            print("\nEmail batal dikirim\n")
        else:
            print(f'''
                    {"─"*27}
                           Invalid request
                    {"─"*27}''')
    
    else:
                print(f'''
            {"─"*40}
                           Invalid request
                Belum ada karyawan yang layak dipromosi
            {"─"*40}''')    

###### PAYROLL ######

# approve gaji
def approve_gaji():
    while True:
        
        id_approve_gaji=int((input("\nMasukkan ID karyawan: ")))

        if  id_approve_gaji in masterdata["id"]:
            idx_pay=masterdata["id"].index(id_approve_gaji)

            if masterdata["gaji_pokok"][idx_pay] > 0:
                print(f'''\nGaji karyawan {masterdata["id"][idx_pay]} telah disetuji''')
                break
            
            elif masterdata["gaji_pokok"][idx_pay] == 0:
                # conditioning gaji based on level dan lama kerja
                masterdata["lama_kerja"][idx_pay] = int(masterdata["lama_kerja"][idx_pay])  # Convert to integer
                masterdata["nilai_karyawan"][idx_pay] = float(masterdata["nilai_karyawan"][idx_pay])  # Convert to float

                if masterdata["level"][idx_pay]=="Staff" and masterdata["lama_kerja"][idx_pay]==1:
                    gaji=5000000
                elif masterdata["level"][idx_pay]=="Staff" and masterdata["lama_kerja"][idx_pay]==2:
                    gaji=8000000
                elif masterdata["level"][idx_pay]=="Specialist" and masterdata["lama_kerja"][idx_pay]==2:
                    gaji=11500000
                elif masterdata["level"][idx_pay]=="Specialist" and masterdata["lama_kerja"][idx_pay]==3:
                    gaji=15000000
                elif masterdata["level"][idx_pay]=="Assistant Manager" and masterdata["lama_kerja"][idx_pay]==3:
                    gaji=16000000
                elif masterdata["level"][idx_pay]=="Assistant Manager" and masterdata["lama_kerja"][idx_pay]==4:
                    gaji=19500000
                elif masterdata["level"][idx_pay]=="Assistant Manager" and masterdata["lama_kerja"][idx_pay]==5:
                    gaji=23000000
                elif masterdata["level"][idx_pay]=="Manager" and masterdata["lama_kerja"][idx_pay]==5:
                    gaji=24000000
                elif masterdata["level"][idx_pay]=="Manager" and masterdata["lama_kerja"][idx_pay]==6:
                    gaji=27000000
                elif masterdata["level"][idx_pay]=="Manager" and masterdata["lama_kerja"][idx_pay]==7:
                    gaji=30000000
                elif masterdata["level"][idx_pay]=="Senior Manager" and masterdata["lama_kerja"][idx_pay]==7:
                    gaji=31000000
                elif masterdata["level"][idx_pay]=="Senior Manager" and masterdata["lama_kerja"][idx_pay]==8:
                    gaji=35500000
                elif masterdata["level"][idx_pay]=="Senior Manager" and masterdata["lama_kerja"][idx_pay]==9:
                    gaji=40000000
                elif masterdata["level"][idx_pay]=="Head":
                    gaji=45500000

                gaji_print = (f"Rp {gaji:,}")

                # print yang mau di-approve
                column_option = ["id", "nama", "dept", "lama_kerja", "level", "fte", "nilai_karyawan", "gaji_pokok", "bonus"]
                header = ["ID", "Nama", "Departemen", "Lama Kerja", "level", "FTE", "Nilai Akhir", "Gaji Pokok", "Bonus"]

                masterdata["gaji_pokok"][idx_pay] = gaji
                idx_masterdata = masterdata["id"].index(id_approve_gaji)

                data = []
                row = []

                for col in column_option:
                    value = masterdata[col][idx_masterdata]
                    if col in ["gaji_pokok", "bonus"]:
                        row.append(f"Rp {value:,}")  # Format nilai numerik sebagai mata uang
                    else:
                        row.append(value)  # Ambil nilai apa adanya untuk kolom lainnya

                data.append(row)
                print(tabulate(data, headers=header, tablefmt="fancy_grid"))
                approval=(input("Apakah Anda menyetui jumlah gaji tersebut? (y/n): ")).capitalize()

                if approval=="Y":
                    print("\nGaji karyawan telah disetujui\n")

                    break

                elif approval=="N":
                    print("\nGaji karyawan batal disetujui\n")
                    masterdata["gaji_pokok"][idx_masterdata] = 0
                    break
                
                else:
                    print(f'''
                    {"─"*27}
                           Invalid request
                            Masukkkan Y/N
                    {"─"*27}''')
                    
        else:
            print(f'''
                    {"─"*27}
                           Invalid request
                    {"─"*27}''')
            break

# approve bonus
def approve_bonus():
    print('''\n\t    Peraturan Perhitungan Bonus PT SINAU
                          
            1. Hanya karyawan dengan status Full-Time Employee yang berhak mendapatkan bonus.
            2. Karyawan dengan pengalaman kerja 1 tahun berhak mendapatkan bonus sebesar 1 kali gaji.
            3. Karyawan dengan pengalaman kerja lebih dari 1 tahun berhak mendapatkan bonus sebesar 2 kali gaji,
               apabila nilai performa karyawan lebih dari atau sama dengan 90.
                             ''')

    # validasi approval
    while True:

        validasi_hitung_bonus=input("Apakah anda yakin ingin menghitung bonus berdasarkan ketentuan di atas? (y/n): ").strip().upper()

        if validasi_hitung_bonus == "Y":
            
            for i in range(len(masterdata["id"])):
                if masterdata["fte"][i]==1:
                    # kalo baru satu tahun kerja, bonus 1x gaji
                    if masterdata["lama_kerja"][i]==1:
                        masterdata["bonus"][i]=(masterdata["gaji_pokok"][i]*1)
                    elif masterdata["lama_kerja"][i]>1 and masterdata["nilai_karyawan"][i]<90:
                        masterdata["bonus"][i]=(masterdata["gaji_pokok"][i]*1)
                    elif  masterdata["lama_kerja"][i]>1 and masterdata["nilai_karyawan"][i]>=90:
                        masterdata["bonus"][i]=(masterdata["gaji_pokok"][i]*2)
                        
                else:
                    masterdata["bonus"][i]="Tidak eligible mendapatkan bonus"
            
            print_table("payroll_table")

            validasi_approve_bonus=input("Apakah anda memberikan approval atas perhitungan bonus tersebut? (y/n): ").capitalize()

            if validasi_approve_bonus == "N":
                for i in range(len(masterdata["id"])):
                    masterdata["bonus"][i]=0
                print("\nBonus dibatalkan karena belum ada persetujuan. Harap ajukan persetujuan ulang. \n")
                break
            elif validasi_approve_bonus == "Y":
                print("\nData tersimpan\nBonus telah disetujui")
                break
            else:
                print(f'''
                        {"─"*20}
                            Invalid request
                              Masukkan Y/N
                        {"─"*20}''')
                
        elif validasi_hitung_bonus=="N":
            print("\nPerhitungan bonus dibatalkan\n")
            break
        
        else:
            print(f'''
                    {"─"*20}
                        Invalid request
                          Masukkan Y/N
                    {"─"*20}''')

###### OFFBOARDING ######

# print offboarding table
def print_offboarding():
    if len(offboarding_table["id"]) == 0:
        print('''
              ====================================================================
                            Belum ada data pada table offboarding
              Tidak ada karyawan yang sedang atau telah melalui prosess offboarding
              ====================================================================\n''')

    else:
        update_offboarding_from_masterdata()

        print(f"\nOffboarding Process Progess Table\n{"="*94}")

        header = ["ID", "Nama", "Departemen", "Aset", "Hutang", "Handover", "Status"]
        
        data = []
        for i in range(len(offboarding_table["id"])):  # Asumsi jumlah data didasarkan pada panjang kolom "id"
            row = [offboarding_table[col][i] for col in offboarding_table.keys()]  # Mengakses nilai untuk setiap kolom yang ada di column_option
            data.append(row)

        # Mencetak tabel
        print("\n")
        print(tabulate(data, headers=header, tablefmt="simple_outline", colalign=("center", "left")))

# input karyawan to be processed
def input_karyawan_offboarding():
    while True:
        id_resign = int(input("\nMasukkan ID karyawan: "))

        while True:
            if id_resign in masterdata["id"]:   
                if id_resign in offboarding_table["id"]:
                    print(f'''Karyawan dengan ID {id_resign} sedang atau telah melakukan proses offboarding.''')
                    break
                elif id_resign not in offboarding_table["id"]:
                    idx_masterdata = masterdata["id"].index(id_resign)   

                    offboarding_table["id"].append(masterdata["id"][idx_masterdata])
                    offboarding_table["nama"].append(masterdata["nama"][idx_masterdata])
                    offboarding_table["dept"].append(masterdata["dept"][idx_masterdata])
                    offboarding_table["status"].append(masterdata["status"][idx_masterdata])  
                    offboarding_table["aset"].append("0")
                    offboarding_table["hutang"].append("0")
                    offboarding_table["handover"].append("0")
                    break
            else:
                print(f'''
                    {"─"*27}
                           Invalid request
                      ID tidak dapat ditemukan
                    {"─"*27}''') 
                break 
                
        while True:
            validasi_ofb = input("\nApakah Anda ingin memasukkan data karyawan lain dalam tahap offboarding? (y/n): ").capitalize()
            if validasi_ofb=="N" or validasi_ofb=="Y":
                break
            else:
                print(f'''
                    {"─"*27}
                           Invalid request
                    {"─"*27}''')
        
        if validasi_ofb=="N":
            break

# edit proses offboarding karyawan
def edit_proses_offboarding():
    while True:
        id_resign=int(input("\nMasukkan ID karyawan: "))
        if id_resign in offboarding_table["id"]:
            
            while True:
                list_offboarding=["Penyerahan aset", "Penyelesaian hutang","Transfer knowledge/File handover"]
                data = [[i+1, list_offboarding[i]] for i in range(len(list_offboarding))]

                print("\n")
                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))
                
                pilih_list_offboarding=int(input("Masukkan pilihan nomor untuk mengubah checklist offboarding karyawan: "))
                idx_ofb = offboarding_table["id"].index(id_resign)

                if pilih_list_offboarding==1:
                    print(''' \nPastikan hal-hal dibawah ini telah dilakukan sebelum memberikan approval!

                        1. Karyawan sudah mengembalikan laptop
                        2. Karyawan sudah mengembalikan ponsel
                        3. Karyawan sudah mengembalikan kartu akses
                        ''')
                    
                    while True:
                        validasi=input("\nApakah Anda memberikan persetujuan bahwa karyawan telah menyelesaikan transfer knowledge/file handover? (y/n): ").capitalize()
                        if validasi=="Y":
                            offboarding_table["aset"][idx_ofb]=1
                            print("\nData tersimpan\n")
                            break
                        elif validasi=="N":
                            offboarding_table["aset"][idx_ofb]=0
                            print("\nKaryawan belum menyelesaikan tahap penyerahan aset")
                            break
                        else:
                            print(f'''
                    {"─"*27}
                           Invalid request
                            Masukkan Y/N
                    {"─"*27}''')

                
                elif pilih_list_offboarding==2:
                    print(''' \nPastikan hal-hal dibawah ini telah dilakukan sebelum memberikan approval!
                        
                        1. Seluruh pinjaman atau hutang, seperti pinjaman karyawan atau fasilitas kredit
                        2. Gaji akhir karyawan telah direkonsiliasi
                        3. Pastikan terdapat dokumen yang menunjukkan bahwa seluruh hutang telah lunas oleh bagian Finance
                        ''')
                    
                    while True:
                        validasi=input("Apakah Anda memberikan persetujuan bahwa karyawan telah menyelesaikan hutangnya? (y/n): ").capitalize()
                        if validasi=="Y":
                            offboarding_table["hutang"][idx_ofb]=1
                            print("\nData tersimpan\n")
                            break
                        elif validasi=="N":
                            offboarding_table["hutang"][idx_ofb]=0
                            print("\nKaryawan belum menyelesaikan tahap penyerahan aset")
                            break
                        else:
                            print(f'''
                    {"─"*27}
                           Invalid request
                            Masukkan Y/N
                    {"─"*27}''')

                elif pilih_list_offboarding==3:
                    print(''' \nPastikan hal-hal dibawah ini telah dilakukan sebelum memberikan approval!
                        
                        1. Pastikan terdapat dokumen konfirmasi manajer yang menunjukkan bahwa 
                            seluruh dokumen kerja telah disampaikan ke tim kerja atau pengganti
                        2. Pastikan akses karyawan telah dialihkan atau dinonaktifkan
                        ''')
                    
                    while True:
                        validasi=input("\nApakah Anda memberikan persetujuan bahwa karyawan telah melakukan transfer knowledge/file handover? (y/n): ").capitalize()
                        if validasi=="Y":
                            offboarding_table["handover"][idx_ofb]=1
                            print("\nData tersimpan\n")
                            break
                        elif validasi=="N":
                            offboarding_table["handover"][idx_ofb]=0
                            print("\nKaryawan belum menyelesaikan tahap penyerahan aset")
                            break
                        else:
                            print(f'''
                    {"─"*27}
                           Invalid request
                            Masukkan Y/N
                    {"─"*27}''')
                
                else:
                    print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-3
                        {"─"*20}
                        ''')

                # Status formula
                stat_aset = offboarding_table["aset"][idx_ofb]
                stat_hutang = offboarding_table["hutang"][idx_ofb]
                stat_handov = offboarding_table["handover"][idx_ofb]

                if stat_aset == 1 and stat_hutang == 1 and stat_handov ==1:
                    offboarding_table["status"][idx_ofb]="Inaktif"
                    idx_masterdata=masterdata["id"].index(id_resign)
                    masterdata["status"][idx_masterdata]="Inaktif"          
                    
                # validasi input score for THE SAME ID
                while True:
                    input_validasi=input(f"\nApakah Anda ingin memberikan approval pada opsi lain? (y/n): ").capitalize()
                    if input_validasi=="Y" or input_validasi=="N":
                        break
                    else:
                        print(f'''
                      {"─"*20}
                        Invalid request
                         Masukkan Y/N
                      {"─"*20}''')

                if input_validasi=="N":
                    break
                
        else:
            print(f'''
                    {"─"*27}
                           Invalid request
                      ID tidak dapat ditemukan
                    {"─"*27}''')
            break
                        
        # validasi input another score for DIFFERENT ID
        while True:
            validasi_edit=(input("\nApakah Anda ingin mengubah data karyawan lain?  (y/n): ")).capitalize()
            if validasi_edit=="N" or validasi_edit=="Y":
                break
            else:
                print(f'''
                        {"─"*20}
                           Invalid request
                             Masukkan Y/N
                        {"─"*20}
                        ''')
                break
        
        if validasi_edit=="N":
            break

# update FROM masterdata
def update_offboarding_from_masterdata():
    for idx_masterdata in range(len(masterdata["id"])):

        id_masterdata = masterdata["id"][idx_masterdata] # tarik id

        if id_masterdata in offboarding_table["id"]: 
            idx_masterdata = masterdata["id"].index(id_masterdata)
            idx_ofb = offboarding_table["id"].index(id_masterdata)

            offboarding_table["nama"][idx_ofb]=(masterdata["nama"][idx_masterdata])
            offboarding_table["dept"][idx_ofb]=(masterdata["dept"][idx_masterdata])
            offboarding_table["status"][idx_ofb]=(masterdata["status"][idx_masterdata])


###### FEATURE ######

# validasi
def validasi_input_list(list_input, text, errotext):
    new_value = input(text).capitalize()
    while True:
        if new_value.isdigit() and all(isinstance(item, int) for item in list_input): # kalo si new value = angka, dan seluruh instance item dalam list input = angka
            new_value = int(new_value)

        if new_value not in list_input :
            print(errotext)
            new_value = input(text).capitalize()
        else:
            break

    return new_value

        # while True:
    #     new_jenis_kelamin = (input("Masukkan jenis kelamin (p/l): ")).capitalize

    #     if new_jenis_kelamin != "P" and new_jenis_kelamin != "L":
    #         print("\nInvalid request\nMasukkan P atau L")
    #     else:
    #         break

# transform table
def transform_table(nama_table):  
    onboarding_sorted = []
    performance_sorted = []
    payroll_sorted = []
    offboarding_sorted = []

    if nama_table == "onboarding_sorted":

        for i in range(len(masterdata["id"])):
                onboarding_dict = {
                "ID": masterdata["id"][i],
                "Nama": masterdata["nama"][i],
                "Departemen": masterdata["dept"][i],
                "Lama Kerja": masterdata["lama_kerja"][i],
                "Level": masterdata["level"][i],
                "Jenis Kelamin": masterdata["jenis_kelamin"][i],
                "Status Nikah": masterdata["marital_status"][i],
                "FTE": masterdata["fte"][i],
                "Status": masterdata["status"][i]
                }
                onboarding_sorted.append(onboarding_dict)
        return onboarding_sorted

    elif nama_table == "performance_sorted":

        for i in range(len(masterdata["id"])):
                performance_dict = {
                "ID": masterdata["id"][i],
                "Nama": masterdata["nama"][i],
                "Departemen": masterdata["dept"][i],
                "Lama Kerja": masterdata["lama_kerja"][i],
                "Level": masterdata["level"][i],
                "Leadership": masterdata["leadership"][i],
                "Review 360": masterdata["review360"][i],
                "KPI": masterdata["kpi"][i],
                "Nilai Akhir": masterdata["nilai_karyawan"][i],
                "Kelayakan": masterdata["kelayakan"][i],
                "Status": masterdata["status"][i]
                }
                performance_sorted.append(performance_dict)
        return performance_sorted

    elif nama_table == "payroll_sorted":

        for i in range(len(masterdata["id"])):
                payroll_dict = {
                "ID": masterdata["id"][i],
                "Nama": masterdata["nama"][i],
                "Departemen": masterdata["dept"][i],
                "Lama Kerja": masterdata["lama_kerja"][i],
                "Level": masterdata["level"][i],
                "FTE": masterdata["fte"][i],
                "Nilai Akhir": masterdata["nilai_karyawan"][i],
                "Gaji Pokok": masterdata["gaji_pokok"][i],
                "Bonus": masterdata["bonus"][i]
                }
                payroll_sorted.append(payroll_dict)
        return payroll_sorted
        
    elif nama_table == "offboarding_sorted":

        for i in range(len(offboarding_table["id"])):
                offboarding_dict = {
                "ID": offboarding_table["id"][i],
                "Nama": offboarding_table["nama"][i],
                "Departemen": offboarding_table["dept"][i],
                "Aset": offboarding_table["aset"][i],
                "Hutang": offboarding_table["hutang"][i],
                "Handover": offboarding_table["handover"][i],
                "Status": offboarding_table["status"][i],
                }
                offboarding_sorted.append(offboarding_dict)
        return offboarding_sorted

# print data & option
def option_table(nama_table):
    if nama_table == "onboarding_sorted":
        option = ["ID", "Nama", "Departemen", "Lama Kerja", "Level", "Jenis Kelamin", "Status Nikah", "FTE", "Status"]
    elif nama_table == "performance_sorted":
        option = ["ID", "Nama", "Departemen", "Lama Kerja", "Leadership", "Review 360", "KPI", "Nilai Akhir", "Kelayakan", "Status"]
    elif nama_table == "payroll_sorted":
        option = ["ID", "Nama", "Departemen", "Lama Kerja", "Level", "FTE", "Nilai Akhir", "Gaji Pokok", "Bonus"]
    elif nama_table == "offboarding_sorted":
        option = ["ID", "Nama", "Departemen", "Aset", "Hutang", "Handover", "Status"]
    data = [[i+1, option[i]] for i in range(len(option))]
    return data, option

# sort table
def sort_table(nama_table): 
    data_table = transform_table(nama_table)
    data, option = option_table(nama_table)

    while True:
        ("\n")
        print(tabulate(data, headers=["No", "Opsi"], tablefmt="simple_outline"))
        pilih_sort = int(input("Pilih opsi mengurutkan data: "))

        if pilih_sort < 1 or pilih_sort > len(option):
            print(f"\nInvalid request\nMasukkan angka 1-{len(option)}\n") 
        else:
            list_menu_sort = ["Ascending (A -> Z)","Descending (Z -> A)"]
            data = [[i+1, list_menu_sort[i]] for i in range(len(list_menu_sort))]
            print("\n")
            print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))
            pilih_tipe_sort = int(input("Pilih tipe urutan: "))
            n = len(data_table)

            if pilih_tipe_sort == 1:

                for i in range(n): 
                    for j in range(0, n-i-1): 
                        if data_table[j][option[pilih_sort-1]] > data_table[j+1][option[pilih_sort-1]]: 
                            data_table[j], data_table[j+1] = data_table[j+1], data_table[j]
                print("\n")
                print(tabulate(data_table, headers="keys", tablefmt="simple_outline"))


            elif pilih_tipe_sort == 2:

                for i in range(n): 
                    for j in range(0, n-i-1): 
                            if data_table[j][option[pilih_sort-1]] < data_table[j+1][option[pilih_sort-1]]: 
                                data_table[j], data_table[j+1] = data_table[j+1], data_table[j]
                print("\n")                
                print(tabulate(data_table, headers="keys", tablefmt="simple_outline"))
            break
                            
# filter table
def filter_table(nama_table):  
    data_table = transform_table(nama_table)
    data, option = option_table(nama_table)

    while True:   
        # print pilihan filter
        print("\n")      
        print(tabulate(data, headers=["No", "Opsi"], tablefmt="simple_outline"))
        pilih_filter = int((input("\nPilih opsi filter data: ")).strip())

        if pilih_filter > len(option) or pilih_filter <= 0:
            print(f"Invalid request\nMasukkan angka 1-{len(option)}") 
        else:
            value_data = (input("\nMasukkan value: ").strip())

            if value_data.isdigit():
                filtered_data = list(filter(lambda transformed_table: transformed_table[option[pilih_filter - 1]] == int(value_data), data_table)) 
            else:  
                value_data = value_data.lower()
                filtered_data = list(filter(lambda transformed_table: transformed_table[option[pilih_filter - 1]].lower() == value_data, data_table))            
            
            if len(filtered_data) != 0:
                print("\n")
                print(tabulate(filtered_data, headers="keys", tablefmt="simple_outline"))
            else:
                print(f'''
                   {"─"*28}
                           Invalid request
                    Data tidak dapat ditemukan
                   {"─"*28}''')
            
            break
                 
# search table:
def search_table(nama_table):
    column_option=[]
    header=[]
       
    if nama_table == "onboarding_table":
        column_option = ["id", "nama", "dept", "lama_kerja", "level", "jenis_kelamin", "marital_status", "fte", "status"]
        header = ["ID", "Nama", "Departemen", "Lama Kerja", "Level", "Jenis Kelamin", "Status Nikah", "FTE", "Status"]
    elif nama_table == "performance_table":
        column_option = ["id", "nama", "dept", "lama_kerja", "leadership", "review360", "kpi", "nilai_karyawan", "kelayakan", "status"]
        header = ["ID", "Nama", "Departemen", "Lama Kerja", "Leadership", "Review 360", "KPI", "Nilai Akhir", "Kelayakan", "Status"]
    elif nama_table == "payroll_table":
        column_option = ["id", "nama", "dept", "lama_kerja", "level", "fte", "nilai_karyawan", "gaji_pokok", "bonus"]
        header = ["ID", "Nama", "Departemen", "Lama Kerja", "Level", "FTE", "Nilai Akhir", "Gaji Pokok", "Bonus"]
    elif nama_table == "offboarding_table":
        column_option = ["id", "nama", "dept", "aset ", "hutang", "handover", "status"]
        header = ["ID", "Nama", "Departemen", "Lama Kerja", "Level", "FTE", "Nilai Akhir", "Gaji Pokok", "Bonus"]

    while True:
        try:
            id_search = int(input("\nMasukkan ID karyawan yang ini ada cari: "))

            if id_search in masterdata["id"]:      
                idx_search = masterdata["id"].index(id_search)
                data = [[masterdata[column][idx_search] for column in column_option]]
                print("\n")
                print(tabulate(data, headers=header, tablefmt="fancy_grid"))   
                break

            else:
                print(f'''
                    {"─"*27}
                           Invalid request
                      ID tidak dapat ditemukan
                    {"─"*27}''')
                break


        except ValueError:
            print("masukkin id yang bener")

def search_table_ofb():
    column_option = ["id", "nama", "dept", "aset ", "hutang", "handover", "status"]
    header = ["ID", "Nama", "Departemen", "Aset", "Hutang", "Handover", "Status"]

    while True:
        id_search = int((input("\nMasukkan ID karyawan yang ini ada cari: ")).strip())

        if id_search in offboarding_table["id"]:  
                
            idx_search = offboarding_table["id"].index(id_search)
            data = [[offboarding_table[column][idx_search] for column in column_option]]
            print("\n")
            print(tabulate(data, headers=header, tablefmt="simple_outline"))   
            break     

        else:
                print(f'''
                    {"─"*27}
                           Invalid request
                      ID tidak dapat ditemukan
                    {"─"*27}''')
                break

# back
def back():
    while True:
        try:
            back_menu = input("\nMasukkan '0' untuk kembali ke menu sebelumnya: ")
            if back_menu == "0":
                break
            else:
                print("\nInput Yang Anda Masukan Salah, Mohon masukkan '0' lagi")
        except ValueError:
            print("\nInput tidak valid! Mohon masukkan '0'.")




###### WHOLE MENU ######

def menu():
    while True:
        # menu lvl 1
        print("\n")
        list_menu = ["Onboarding", "Performance and Development", "Payroll", "Offboarding", "Log Out"]
        data = [[i+1, list_menu[i]] for i in range(len(list_menu))]
        print(tabulate(data,headers=["No", "Main Menu"],tablefmt="simple_outline", colalign=("center", "left")))
        
        try:
            pilih_area=int((input("\nPilih area pengelolaan data: ")).strip())
            
            idx_login = masterdata["id"].index(login_id)

            # menu lvl 2
            if pilih_area==1 and (login_id in list_permission_onboarding) and (masterdata["status"][idx_login]=="Aktif"):
                while True:
                    list_menu = ["Lihat data karyawan", "Input data karyawan baru", "Edit data karyawan", "Hapus data karyawan","Kembali ke menu utama"]
                    data = [[i+1, list_menu[i]] for i in range(len(list_menu))]
                    print("\n")
                    print(tabulate(data,headers=["No", "Onboarding Menu"],tablefmt="simple_outline", colalign=("center", "left")))

                    try:
                        pilih_submenu=int((input("\nPilih opsi yang dibutuhkan: ")).strip())

                        if pilih_submenu==1:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Lihat semua data","Cari karyawan berdasarkan ID", "Urutkan tabel", "Filter tabel","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu==1:
                                        # update_onboarding_table_from_masterdata()
                                        print_table("onboarding_table")
                                        back()
                                    elif pilih_subsubmenu==2:
                                        search_table("onboarding_table")
                                        back()
                                    elif pilih_subsubmenu==3:
                                        sort_table("onboarding_sorted")
                                        back()
                                    elif pilih_subsubmenu==4:
                                        filter_table("onboarding_sorted")
                                        back()
                                    elif pilih_subsubmenu==5:
                                        break
                                    elif pilih_subsubmenu > len(subsubmenu_read) or pilih_submenu < 1:
                                        print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-5
                        {"─"*20}''')
                                except ValueError:
                                    print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')
                        elif pilih_submenu==2:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Input data karyawan baru","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu == 1:
                                        new_data_onboarding()
                                        back()
                                    elif pilih_subsubmenu == 2:
                                        break
                                    else:
                                        print("\nMasukkan 1-2 else")
                                except ValueError:
                                    print("\nMasukkan 1-2")
                        elif pilih_submenu==3:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Edit data karyawan","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu == 1:
                                        edit_onboarding()
                                        back()
                                    elif pilih_subsubmenu == 2:
                                        break
                                    else:
                                        print("\nMasukkan 1-2 else")
                                except ValueError:
                                    print("\nMasukkan 1-2")
                        elif pilih_submenu==4:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Hapus data karyawan","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu == 1:
                                        delete_from_onboarding()
                                        back()
                                    elif pilih_subsubmenu == 2:
                                        break
                                    else:
                                        print("\nMasukkan 1-2 else")
                                except ValueError:
                                    print("\nMasukkan 1-2")
                        elif pilih_submenu==5:
                            break
                        elif pilih_submenu > len(list_menu) or pilih_submenu < 1:
                            print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')

                    except ValueError:
                        print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')

            elif pilih_area==2 and (login_id in list_permission_performance) and (masterdata["status"][idx_login]=="Aktif"):

                while True:
                    list_menu = ["Lihat data performance & promotion", "Edit nilai karyawan", "Kirim email pengajuan promosi", "Kembali ke menu utama"]
                    data = [[i+1, list_menu[i]] for i in range(len(list_menu))]
                    
                    print("\n")
                    print(tabulate(data,headers=["No", "Performance Menu"],tablefmt="simple_outline", colalign=("center", "left")))
            
                    try:
                        pilih_submenu=int((input("\nSilahkan pilih opsi yang dibutuhkan: ")).strip())

                        if pilih_submenu==1:
                            while True:
                                # submenu lvl 3
                                subsubmenu_read=["Lihat semua data","Cari Karyawan Berdasarkan ID", "Urutkan Tabel", "Filter Tabel","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu==1:
                                        print_table("performance_table")
                                        back()
                                    elif pilih_subsubmenu==2:
                                        search_table("performance_table")
                                        back()
                                    elif pilih_subsubmenu==3:
                                        sort_table("performance_sorted")
                                        back()
                                    elif pilih_subsubmenu==4:
                                        filter_table("performance_sorted")
                                        back()
                                    elif pilih_subsubmenu==5:
                                        break
                                    elif pilih_subsubmenu > len(subsubmenu_read) or pilih_submenu < 1:
                                        print(f'''
                    {"─"*20}
                        Invalid request
                        Masukkan 1-4
                    {"─"*20}''')
                                except ValueError:
                                        print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')
                        elif pilih_submenu==2:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Edit data karyawan","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu == 1:
                                        edit_performance()
                                        back()
                                    elif pilih_subsubmenu == 2:
                                        break
                                    else:
                                        print("\nMasukkan 1-2 else")
                                except ValueError:
                                    print("\nMasukkan 1-2")
                        elif pilih_submenu==3:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Kirim email pengajuan promosi","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu == 1:
                                        promotion_approval()
                                        back()
                                    elif pilih_subsubmenu == 2:
                                        break
                                    else:
                                        print("\nMasukkan 1-2 else")
                                except ValueError:
                                    print("\nMasukkan 1-2")                        
                        elif pilih_submenu==4:
                            break
                        elif pilih_submenu > len(list_menu) or pilih_submenu < 1:
                            print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')
                            
                    except ValueError:
                        print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')

            elif pilih_area==3 and (login_id in list_permission_payroll) and (masterdata["status"][idx_login]=="Aktif"):
                while True:
                    list_menu = ["Lihat data payroll", "Approve gaji karyawan", "Approve bonus karyawan", "Kembali ke menu utama"]
                    data = [[i+1, list_menu[i]] for i in range(len(list_menu))]

                    print("\n")
                    print(tabulate(data,headers=["No", "Payroll Menu"],tablefmt="simple_outline", colalign=("center", "left")))

                    try:
                        pilih_submenu=int((input("\nSilahkan pilih opsi yang dibutuhkan: ")).strip())

                        if pilih_submenu==1:                             
                            while True:
                                # submenu lvl 3
                                subsubmenu_read=["Lihat Seluruh Data", "Cari Karyawan Berdasarkan ID", "Urutkan Tabel", "Filter Tabel","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu==1:
                                        print_table("payroll_table")
                                        back()     
                                    elif pilih_subsubmenu==2:
                                        search_table("payroll_table")
                                        back()
                                    elif pilih_subsubmenu==3:
                                        sort_table("payroll_sorted")
                                        back()
                                    elif pilih_subsubmenu==4:
                                        filter_table("payroll_sorted")
                                        back()
                                    elif pilih_subsubmenu==5:
                                        break
                                    elif pilih_subsubmenu > len(subsubmenu_read) or pilih_submenu < 1:
                                        print(f'''
                        {"─"*20}
                            Invalid request
                             Masukkan 1-4
                        {"─"*20}''')
                                
                                except ValueError:
                                    print(f'''
                    {"─"*27}
                            Invalid request
                    {"─"*27}''')
                        elif pilih_submenu==2:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Approve Gaji","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu == 1:
                                        approve_gaji()
                                        back()
                                    elif pilih_subsubmenu == 2:
                                        break
                                    else:
                                        print("\nMasukkan 1-2 else")
                                except ValueError:
                                    print("\nMasukkan 1-2")
                        elif pilih_submenu==3:
                            while True:
                                # menu lvl 3
                                subsubmenu_read=["Approve Bonus","Kembali ke Menu Area"]
                                data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                                print("\n")
                                print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                try:
                                    pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                    if pilih_subsubmenu == 1:
                                        approve_bonus()
                                        back()
                                    elif pilih_subsubmenu == 2:
                                        break
                                    else:
                                        print("\nMasukkan 1-2 else")
                                except ValueError:
                                    print("\nMasukkan 1-2")
                        elif pilih_submenu==4:
                            break
                        elif pilih_submenu > len(list_menu) or pilih_submenu < 1:
                            print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')
                            
                    except ValueError:
                        print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')
            
            elif pilih_area==4 and (login_id in list_permission_offboarding) and (masterdata["status"][idx_login]=="Aktif"):
                while True:
                
                    list_menu = ["Lihat data offboarding", "Input karyawan untuk proses offboarding", "Update proses offboarding karyawan", "Kembali ke menu utama"]
                    data = [[i+1, list_menu[i]] for i in range(len(list_menu))]
                    
                    print("\n")
                    print(tabulate(data,headers=["No", "Offboarding Menu"],tablefmt="simple_outline", colalign=("center", "left")))
                    
                    try:
                        pilih_submenu=int((input("\nSilahkan pilih opsi yang dibutuhkan: ")).strip())

                        if pilih_submenu==1:
                            if len(offboarding_table["id"]) == 0:
                                print_offboarding()
                            else:
                                while True:
                                    # submenu lvl 3
                                    subsubmenu_read=["Lihat Seluruh Data", "Cari Karyawan", "Urutkan Tabel", "Filter Tabel","Kembali ke Menu Area"]
                                    data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]

                                    print("\n")
                                    print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                                    try:

                                        pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                        if pilih_subsubmenu==1:
                                            print_offboarding() 
                                        elif pilih_subsubmenu==2:
                                            search_table_ofb()
                                        elif pilih_subsubmenu==3:
                                            transform_table("offboarding_sorted")
                                            sort_table("offboarding_sorted")
                                            break
                                        elif pilih_subsubmenu==4:
                                            transform_table("offboarding_sorted")
                                            filter_table("offboarding_sorted")
                                            break
                                        elif pilih_subsubmenu==5:
                                            break
                                        elif pilih_subsubmenu > len(subsubmenu_read) or pilih_submenu < 1:
                                            print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')
                                    
                                    except ValueError:
                                        print(f'''
                    {"─"*27}
                           Invalid request
                    {"─"*27}''')
                        elif pilih_submenu==2:
                            # menu lvl 3
                            subsubmenu_read=["Input karyawan untuk proses offboarding","Kembali ke Menu Area"]
                            data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                            print("\n")
                            print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                            try:
                                pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                if pilih_subsubmenu == 1:
                                    update_offboarding_from_masterdata()
                                    input_karyawan_offboarding()  
                                    back()
                                elif pilih_subsubmenu == 2:
                                    break
                                else:
                                    print("\nMasukkan 1-2 else")
                            except ValueError:
                                print("\nMasukkan 1-2")         
                        elif pilih_submenu==3:
                           # menu lvl 3
                            subsubmenu_read=["Update proses offboarding karyawan","Kembali ke Menu Area"]
                            data = [[i+1, subsubmenu_read[i]] for i in range(len(subsubmenu_read))]
                            print("\n")
                            print(tabulate(data, headers=["No","Opsi"], tablefmt="simple_outline", colalign=("center", "left")))

                            try:
                                pilih_subsubmenu=int((input(f"Pilih opsi sesuai yang dibutuhkan: ")).strip())
                                if pilih_subsubmenu == 1:
                                    edit_proses_offboarding()
                                    back()
                                elif pilih_subsubmenu == 2:
                                    break
                                else:
                                    print("\nMasukkan 1-2 else")
                            except ValueError:
                                print("\nMasukkan 1-2")         
                        elif pilih_submenu==4:
                            break
                        elif pilih_submenu > len(list_menu) or pilih_submenu < 1:
                            print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-4
                        {"─"*20}''')
                                                
                    except ValueError:
                        print(f'''
                    {"─"*27}
                           Invalid request ini try except payroll
                    {"─"*27}''')         
                           
            elif pilih_area==5:
                print(f'''
                    {"─"*27}
                        Logging Out........
                    {"─"*27}''')
                break       
                 
            elif pilih_area <= 0 or pilih_area > 5:
                print(f'''\n
                        {"─"*20}
                           Invalid request
                            Masukkan 1-5
                        {"─"*20}''')

            else:
                print(f'''\n
                {"="*41}
                            Permission denied
                  Anda tidak memiliki akses ke modul ini
                {"="*41}\n''')

        except ValueError:
            print(f'''
                        {"─"*20}
                           Invalid request
                            Masukkan 1-5
                        {"─"*20}''')



###### PROGRAM ######

while True:
    try:
        login_id = int((input(f'''
                {"─"*41}
                      Selamat datang di HRIS PT SINAU    
                {"─"*41}
            
                Masukkan ID: ''')).strip())
        
        password=maskpass.askpass("\t\tPassword: ")


        if login_id in permission_password["id"]:
            idx_login = permission_password["id"].index(login_id)
            validasi_pw = permission_password["password"][idx_login]

            if int(password) == validasi_pw:
                menu()
            else:
                print(f'''\n
                {"="*41}
                            Permission denied
                              Password salah
                {"="*41}\n''')
        
        else:
            print(f'''\n
                {"="*41}
                            Permission denied
                  Anda tidak memiliki akses ke modul ini
                {"="*41}\n''')
            
    except ValueError:
        print(f'''\n
                {"="*41}
                            Permission denied
                      Masukkan 5 digit angka ID Anda
                {"="*41}\n''')
    
