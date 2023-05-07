from modules.networks import getNets, hello
from modules.brute import bruteNets


def main():
	nets = getNets()

	print('\nResult:')
	for net in nets:
		print(f'\nWiFi SSID: {net[0]}\nWiFi MAC address: {net[1]}\n')
	print('\n')


if __name__ == "__main__":
	__slots__ = ('storage',)
	
	hello()
	main()
	bruteNets()