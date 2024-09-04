import os

bd = input("Enter the name of the database: ")
bd=bd.upper()

folder_path = "C:\\Users\\HP\\Desktop\\create_user_bd\\"+bd
os.makedirs(folder_path, exist_ok=True)




ch1="CREATE USER C##"+bd+" IDENTIFIED BY sys;\nconn SYSTEM/sys;\nALTER session set \"_ORACLE_SCRIPT\"=true;\nGRANT ALL PRIVILEGES TO C##"+bd+";\n conn C##"+bd+"/sys;"

print("\033[0mto create&&connect to the user:")
print('\033[1;32mstart \033[1;33m"C:\\Users\\HP\\Desktop\\create_user_bd\\'+bd+'\\setup_'+bd+'.sql"\033[0m')
script_filename = os.path.join(folder_path, "setup_"+bd+".sql")
with open(script_filename, 'w') as script_file:
    script_file.write(ch1 + "\n")
script_filename = os.path.join(folder_path, "main_"+bd+".sql")
with open(script_filename, 'a', encoding='utf-8') as script_file:
    script_file.write('/*\nوأحلى ناس مدنين 😊\n*/')
script_filename = os.path.join(folder_path, "exit_"+bd+".sql")
with open(script_filename, 'w', encoding='utf-8') as script_file:
    script_file.write('disconnect')
script_filename = os.path.join(folder_path, "drop_"+bd+".sql")
with open(script_filename, 'w', encoding='utf-8') as script_file:
    script_file.write(' conn SYSTEM/sys;\nDROP USER C##'+bd+';')
print("\033[0mto do your code:")
print('\033[1;32mstart \033[1;33m"C:\\Users\\HP\\Desktop\\create_user_bd\\'+bd+'\\main_'+bd+'.sql"\033[0m')
print("\033[0mto exit the user:")
print('\033[1;32mstart \033[1;33m"C:\\Users\\HP\\Desktop\\create_user_bd\\'+bd+'\\exit_'+bd+'.sql"\033[0m')
print("\033[0mto drop the user:")
print('\033[1;32mstart \033[1;33m"C:\\Users\\HP\\Desktop\\create_user_bd\\'+bd+'\\drop_'+bd+'.sql"\033[0m')

