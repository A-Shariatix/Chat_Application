def check_user_existence(username, password, cursor):
user_exist = cursor.execute(f'select username, password '
f'from information where username = "{username}"'
f' and password = "{password}"')
if user_exist == 2:
return True
else:
return False
