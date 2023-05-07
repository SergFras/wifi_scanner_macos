import os


def getNets():
	print('\n\nScanning network...\n\n')
	os.system('airport -s > modules/wifi.log')
	wifi, nets = None, []


	with open('modules/wifi.log', 'r') as f:
		wifi = f.readlines()

	for i in range(1, len(wifi)):
		wifi[i] = wifi[i].lstrip(' ')
		wifi[i] = wifi[i].replace(' ', '&')
		wifi[i] = wifi[i].split(',')
		wifi[i] = wifi[i][0]
		wifi[i] = wifi[i].split('&')

		nets.append(list((wifi[i][0], wifi[i][1])))

	return nets


def hello():
	print('\n░██████╗███████╗██████╗░░██████╗░███████╗██████╗░░█████╗░░██████╗\n██╔════╝██╔════╝██╔══██╗██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔════╝\n╚█████╗░█████╗░░██████╔╝██║░░██╗░█████╗░░██████╔╝███████║╚█████╗░\n░╚═══██╗██╔══╝░░██╔══██╗██║░░╚██╗██╔══╝░░██╔══██╗██╔══██║░╚═══██╗\n██████╔╝███████╗██║░░██║╚██████╔╝██║░░░░░██║░░██║██║░░██║██████╔╝\n╚═════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░')