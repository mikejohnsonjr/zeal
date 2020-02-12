with open('genesis.txt','r') as file:
	data = file.read();

new = data.replace('\n', '')
new = new.replace(':','')
with open('genesis.txt','w') as file:
	file.write(new)