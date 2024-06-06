lyrix:
	chmod +x lyrix
	chmod +x lyrix_dist/lyrix

clean:
	rm -r lyrix_dist
	rm lyrix

install:
	cp -r lyrix_dist /usr/bin/
	cp lyrix /usr/bin
