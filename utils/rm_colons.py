with open('pubkey.txt','r') as file:
	data = file.read();

new = data.replace('\n', '')
new = new.replace(':','')
with open('pubkey.txt','w') as file:
	file.write(new)