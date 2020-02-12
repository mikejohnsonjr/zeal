with open('testnetalert.txt','r') as file:
	data = file.read();

new = data.replace('\n', '')
new = new.replace(':','')
with open('testnetalert.txt','w') as file:
	file.write(new)