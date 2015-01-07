Title: Hash table
Date: 2010-11-28 15:39
Author: lmatt wang
Slug: Hash-table

**Hash
table定义**(摘自[wikidpedia](http://en.wikipedia.org/wiki/Hash_table))\
In computer science, a hash table or hash map is a data structure that
uses a hash function to map identifying values, known as keys (e.g., a
person's name), to their associated values (e.g., their telephone
number).\
hash
table简单来说就是一种数据结构，可以通过一个key来查询对应的value值（一般情况下效率是很高的）。

记得以前大学时，老师曾出过这样的一道题目：编写程序来统计文本中出现过的字母以及次数。一个很完美的方案（貌似是老师给出的）如下所示：

    int count[26];//不考虑文本中有大写字母的情况
    memset(count, 0, sizeof(count));
    读取文本中的一个字母c;
    int index = c - 'a';
    count[index]++;
    打印count数组中内容大于0的项；

这种方案就用到了hash
table，将字母c转为index可以被看作hash函数，变换的过程没有出现冲突（这在其他情况下是很难出现的）。

**hash table的实现**\
考虑下面一个问题，如何快速地查询某个人电话号码。\
![hash
table](http://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/500px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)\
一种方法是使用[trie](http://en.wikipedia.org/wiki/Trie);另外一种就是这里提到的hash
table。\
要实现hash table，首先需要一个hash函数。\
hash函数实现了key到下标的转换。下面是一个简单的hash函数，实现了人名到数组下标的转换。如果是其他类型的key，就需要选择其他的hash函数。好的hash函数能提高hash
table的性能。整数形的key可以采用直接取余数(k%TABLE\_SIZE)的方法，或者平方取中法（key平方后取数的中间几个bit）。

    HASHTABLE table[TABLE_SIZE];
    int hash_name(char *name)
     {
        unsigned int h = 0;
        unsigned int seed = 131;/* 31 131 1313 13131 131313 etc.. */
        for(int i = 0; name[i]; i++) 
        {
            h += h * seed + name[i];
        }
        return (int)(h % TABLE_SIZE);
    }

在使用key得到数组下标后，就可以通过这个下标把value（这里是电话号码）存入hash
table中。但需要注意的是，不同的key可能会得到相同下标，这种情况被称为Collision(冲突)。如何解决好Collision(冲突)问题，是hash
table的关键。\
通常处理Collision(冲突)的方法有两类：\
1.open hashing, closed addressing（链地址法）\
将所有下标相同的记录都存储到相同的链表中，而在table中存储链表的起始地址。\
![chain](http://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Hash_table_5_0_1_1_1_1_0_LL.svg/500px-Hash_table_5_0_1_1_1_1_0_LL.svg.png)\
2.closed hashing, open addressing（开放定址法）\
开放定址法则与链地址法不同，在出现冲突后会按照某个特定顺序去找table中下一个空的位置。

    fi = (f(key) + di) % TABLE_SIZE;//f(key)为hash函数，fi为找寻空位置时的序列，di为特定的序列

di一般取c1\*i + c2 \* ( i \* i )。i为1,2,3,...k (k \<= TABLE\_SIZE - 1)\
当c1=1, c2=0时，称为Linear probing(线性探测)。\
当c2!=0时，称为Quadratic probing(二次探测)。\
在二次探测时，需要注意一点，fi是否能取到所有下标。如果fi不能取到所有下标，就可能会出现无法插入元素的情况。\
如果TABLE\_SIZE为2的幂次，c1和c2可以取1/2。如果TABLE\_SIZE为大于2的素数，则c1=0,c2=1或c1=1,c2=1或c1=1/2,c2=1/2都是可以的。\
下面是线性探测的一个代码例子。

    bool insert_item(ITEM item)
    {
        int hi = hash_name(item.name);
        while(table[hi])//这里假设没有全为0的电话号码
        {
            if(table[hi].phone == item.phone) return false;//已存在，插入失败
            hi++;
            if(hi >= TABLE_SIZE) hi -= TABLE_SIZE;
        }
        table[hi].phone = item.phone;
        table[hi].name = item.name;
        return true;
    }

最后是hash table的查询，基本的过程与插入相同。下面是一个简单的代码例子。

    int search_hash(char *key)
    {
        int hi = hash_name(key);
        while(table[hi])//这里假设没有全为0的电话号码
        {
            if(table[hi].name == key)
            {
                 return table[hi].phone;
            }
            hi++;
            if(hi >= TABLE_SIZE) hi -= TABLE_SIZE;
        }
        return -1;//没有查到
    }

上面说明了如何构建hash table与如何查询的过程。在构建hash
table时，需要注意TABLE\_SIZE的大小。如果table的load太高，冲突产生的可能性越大，hash
table的性能就越低。一般建议table的load在0.75以下。
