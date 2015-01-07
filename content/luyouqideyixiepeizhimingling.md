Title: 路由器的一些配置命令
Date: 2010-06-30 16:55
Author: lmatt wang
Slug: luyouqideyixiepeizhimingling

**//enter admin**

enable

**//begine configure**

configure terminal

**//interface  fast.. configure**

-Interface F.. 0/0(0/1)

--ip address a.b.c.d ma.mb.mc.md

**//tunnel configure**

-Interface T.. number(数字）

--tunnel source ip

--tunnel dest.. ip

--ip address a.b.c.d ma.mb.mc.md

--ip ospf network point-to-point

**//ospf configure**

-router ospf number(数字)

--network a.b.c.d ma.mb.mc.md area number(数字）

--passive..

--redis.. bgp id(数字) subnets

--router-id(maybe)

**//bgp configure**

-router bgp id(数字)

--neighbor ip remote-as as\_id

--redis.. ospf number(数字)

--router-id(maybe)

**//exit**

end

exit

**//save configure**

wr
