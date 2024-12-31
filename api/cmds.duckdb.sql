
attach 'db.sqlite3' (TYPE SQLITE);

create table temp_tbl as select *  from read_csv('./ToTK-Recipe.csv') where "Cooking Req" = 'In Pot';

alter table temp_tbl add column created_at timestamp default current_localtimestamp();
alter table temp_tbl add column created_at timestamp default current_localtimestamp();


insert into db.api_recipe (id, name, ingredient_1, ingredient_2, ingredient_3, ingredient_4, ingredient_5, created_at, updated_at)  
    select "Recipe Number", "Name", "Recipe", "column4", "column5", "column6", "column7", created_at, updated_at from temp_tbl; 

