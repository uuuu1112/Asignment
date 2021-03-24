insert into user (name,username,password) values("Jesse","ply","ply");
insert into user (name,username,password,time) values
("Jesse1","a","aa","1983-11-12 11:22:33"),
("Jesse2","b","bb","1983-11-13 11:22:33"),
("Jesse3","c","cc","1983-11-14 11:22:33"),
("Jesse4","d","dd","1983-11-15 11:22:33");

select * from user;

![image](https://user-images.githubusercontent.com/54828912/112367620-1f117700-8d15-11eb-9c74-6c1675364249.png)

select count(*) from user;

![image](https://user-images.githubusercontent.com/54828912/112368904-8b40aa80-8d16-11eb-99ab-c1810ec1abdc.png)

select * from user order by time desc;

![image](https://user-images.githubusercontent.com/54828912/112369682-6c8ee380-8d17-11eb-91ea-da09f88e0d6c.png)

select * from user order by time desc limit 3 offset 1;

![image](https://user-images.githubusercontent.com/54828912/112370910-f0959b00-8d18-11eb-879b-7133805fe445.png)

select * from user where username="ply";

![image](https://user-images.githubusercontent.com/54828912/112371220-541fc880-8d19-11eb-954f-eb45c7fc7c39.png)

select * from user where username="ply" and password="ply";

![image](https://user-images.githubusercontent.com/54828912/112371819-035c9f80-8d1a-11eb-8bf3-5015065c173d.png)


