# something

#in lb
> consul agent -server -bootstrap-expect 1 -data-dir /tmp/
> consul members -detailed #eventually conistent
> curl localhost:8500/v1/catalog/nodes #consistent now
> dig @127.0.0.1 -p 8600 vagrant-ubuntu-trusty-64.node.consul #dns query

> echo '{"service": {"name": "web", "tags": ["django"], "address":"20.0.0.3", "port": 3000}}' >/etc/consul.d/web.json
> consul agent -server -bootstrap-expect 1 -data-dir /tmp/ -config-dir /etc/consul.d
> dig @127.0.0.1 -p 8600 web.service.consul SRV

	; <<>> DiG 9.9.5-3ubuntu0.5-Ubuntu <<>> @127.0.0.1 -p 8600 web.service.consul SRV
	; (1 server found)
	;; global options: +cmd
	;; Got answer:
	;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10552
	;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
	;; WARNING: recursion requested but not available

	;; QUESTION SECTION:
	;web.service.consul.		IN	SRV

	;; ANSWER SECTION:
	web.service.consul.	0	IN	SRV	1 1 3000 vagrant-ubuntu-trusty-64.node.dc1.consul.

	;; ADDITIONAL SECTION:
	vagrant-ubuntu-trusty-64.node.dc1.consul. 0 IN A 20.0.0.3

	;; Query time: 3 msec
	;; SERVER: 127.0.0.1#8600(127.0.0.1)
	;; WHEN: Wed Dec 02 13:53:00 UTC 2015
	;; MSG SIZE  rcvd: 170

> http://localhost:8500/v1/catalog/service/web
 [{"Node":"vagrant-ubuntu-trusty-64",
    "Address":"10.0.2.15",
    "ServiceID":"web",
    "ServiceName":"web",
    "ServiceTags":["django"],
    "ServiceAddress":"20.0.0.3",
    "ServicePort":3000}
  ]

#u can update service configs and just end SIGHUP to agent


#create server-agent
> vagrant ssh lb
> consul agent -server -bootstrap-expect 1 -data-dir /tmp/ -node=agent-one -bind=20.0.0.2 #-bind is the private ip 
              #note; the server variable

#create client-agent
> vagrant ssh appOne
> consul agent -data-dir /tmp/ -node=agent-two -bind=20.0.0.3
            #note; no server variable
> consul members #not yet linked

#joining cluster
> vagrant ssh lb
> consul join 20.0.0.3 #20.0.0.3 is ip of second server(client)
#To join a cluster, a Consul agent only needs to learn about one existing member.

> consul members
	Node       Address        Status  Type    Build  Protocol  DC
	agent-two  20.0.0.3:8301  alive   client  0.5.2  2         dc1
	agent-one  20.0.0.2:8301  alive   server  0.5.2  2         dc1


