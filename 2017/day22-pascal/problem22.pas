{$mode Delphi}
program Problem22;

var i, j,k: integer;
var x,y:integer;
var dir:integer;
lines: array[1..25] of String;

dim: array[1..20000,1..20000] of Char;

answer: integer;

F: TextFile;

begin
  for i:=1 to 20000 do 
      for j:=1 to 20000 do 
            dim[i,j]:= '.';



  AssignFile(F, 'problem22.input');
  Reset(F);
  for i:=1 to 25 do 
  begin
    ReadLn(F, lines[i]);
  end;
  CloseFile(F);

  for i:=1 to 25 do 
      for j:=1 to 25 do 
            dim[10000+j,10000+i]:= lines[i][j];

  for i:=10001 to 10025 do 
  begin
      for j:=10001 to 10025 do 
            write(dim[i,j]);
            write(' ');
      writeln('');
  end;

  x:=10000+13;
  y:=10000+13;
  dir:=0; //0 up, 90 right, 180 down 270 left

  //writeln(dim[x,y]);

    answer:=0;


  for k:=1 to 10000 do 
  begin
    writeln(k);
    if dim[x,y]= '#' then 
    begin
        dir:=(dir+90) mod 360;  
        dim[x,y]:='.';
    end
    else
    begin
        dir:=(dir-90+360) mod 360;  
        dim[x,y]:='#';
        answer:=answer+1;
    end;

    if dir=0 then
        y:=y-1;
    if dir=90 then
        x:=x+1;
    if dir=180 then
        y:=y+1;
    if dir=270 then
        x:=x-1;
  end;


{

  for i:=1 to 20000 do 
  begin
      for j:=1 to 20000 do 
            write(dim[i,j]);
            write(' ');
      writeln('');
  end;

  for i:=1 to 20000 do 
      for j:=1 to 20000 do 
            if dim[i,j]= '#' then 
                answer:=answer+1;
}
  writeln('asnewr is:');
  writeln(answer);

end.

