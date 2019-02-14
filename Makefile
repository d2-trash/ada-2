certs = app/src/fullchain.pem app/src/privkey.pem

.PHONY: install
install: requirements.txt certs
	apt-get install python3-pip
	pip3 install -r requirements.txt && \
		pre-commit install


.PHONY: all
all: install

.PHONY: run
run:
	docker-compose up

.PHONY: test
test: clean
	docker-compose up --build --force-recreate

$(certs):
	apt-get update
	apt-get install -y software-properties-common
	add-apt-repository universe -y
	add-apt-repository ppa:certbot/certbot -y
	apt-get update
	apt-get install -y certbot
	certbot certonly --standalone -n --agree-tos --email samcaccavale@gmail.com -d ada-2.cc -d www.ada-2.cc
	cp /etc/letsencrypt/live/ada-2.cc/*.pem app/src

.PHONY: certs
certs: $(certs)

.PHONY: clean
clean:
	-docker stop $$(docker ps -aq)
	-docker rm $$(docker ps -aq)
