# 密碼測試
# 有三次機會
# 登入成功就顯示"登入成功"
# 登入失敗就顯示"密碼錯誤!還有_次機會"
# raise SystemExit 系統終止




password ='a123456'
input('請輸入你的名稱')
input_pwd = input('請輸入你的密碼')
x = 0
while x < 3:
	x = x + 1
	if password == input_pwd:
		print('登入成功')
		break
	else:
		print('密碼錯誤!還有', 3-x,'次機會')
		input_pwd = input('請再次輸入你的密碼')
		if 3-x == 0 and password != input_pwd:
			print('登入失敗!!!!')
			break