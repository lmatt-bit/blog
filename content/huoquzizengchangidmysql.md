Title: 获取自增长id（mysql）
Date: 2010-10-20 10:40
Author: lmatt wang
Slug: huoquzizengchangidmysql

**java**

    PreparedStatement ps =conn.prepareStatement("insert into table (col) values (?)", Statement.RETURN_GENERATED_KEYS);
    ps.getGeneratedKeys();

**sql**

最后插入的id

    select last_insert_id();

下一个id

    SHOW TABLE STATUS LIKE "table_name";//auto_increment列
