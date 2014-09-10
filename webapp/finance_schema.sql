drop table if exists expenses;
create table expenses (
	id integer primary key autoincrement,
	merchant text not null, 
	amount real not null,
	notes text not null,
	person text null
);