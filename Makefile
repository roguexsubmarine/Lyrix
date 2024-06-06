lyrix:

clean:
	rm -rf /usr/bin/lyrix_dist
	rm /usr/bin/lyrix

install:
	cp -r lyrix_dist /usr/bin/
	cp lyrix /usr/bin/	
	chmod +x /usr/bin/lyrix
