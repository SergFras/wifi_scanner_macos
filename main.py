from modules.networks import getNets, hello


def main():
	nets = getNets()

	print('\nResult:')
	for net in nets:
		print(f'\nWifi name: {net[0]}\nWifi mac addres: {net[1]}\n')


if __name__ == "__main__":
	hello()
	main()