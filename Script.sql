--drop function fn_get;

create or replace function fn_get (inp_username varchar(24), inp_password varchar(64)) 
	returns bool
as $$
	begin
		(select exists(select 1 from users where username = inp_username and "password" = inp_password));
		
	end;
$$
	LANGUAGE plpgsql;
	
create or replace function fn_add (inp_username varchar(24), inp_password varchar(64)) 
	returns bool
as $$
	begin
		--begin
			insert into users(username, "password") values (inp_username, inp_password); 
		return true;
		exception 
			when others 
		then 
		return false;
		
		--end;
		
	end;
$$
	LANGUAGE plpgsql;