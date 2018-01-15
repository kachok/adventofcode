{$mode Delphi}
program Problem22b;

var i, j,k: integer;
var x,y:integer;
var dir:integer;
lines: array[1..25] of String;

var maxx,maxy,minx,miny: integer;

dim: array[1..300*2,1..300*2] of Char;

answer,answer1,answer2,answer3: longint;

F: TextFile;

var size: integer;

begin
    size:=300;
    maxx:=size;
    maxy:=size;
    minx:=size;
    miny:=size;

  for i:=1 to 2*size do 
      for j:=1 to 2*size do 
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
            dim[size+j,size+i]:= lines[i][j];

  for i:=size-10 to size+35 do 
  begin
      for j:=size-10 to size+35 do 
            write(dim[j,i]);
            write(' ');
      writeln('');
  end;

  x:=size+13;
  y:=size+13;
  dir:=0; //0 up, 90 right, 180 down 270 left

  writeln(dim[x,y]);

    answer:=0;
    answer1:=0;
    answer2:=0;
    answer3:=0;


  for k:=1 to 10000000 do 
  begin
    //writeln('----');
    //writeln(k,' ',x,' ',y, ' ',dir, ' ',dim[x,y]);
    if dim[x,y]= '#' then 
    begin
        dir:=(dir+90) mod 360;  
        dim[x,y]:='F';
        answer3:=answer3+1;
    end
    else if dim[x,y]= 'F' then 
    begin
        dir:=(dir+180) mod 360;  
        dim[x,y]:='.';
        answer2:=answer2+1;
    end
    else if dim[x,y]= '.' then 
    begin
        dir:=(dir-90+360) mod 360;  
        dim[x,y]:='W';
        answer:=answer+1;
    end
    else if dim[x,y]= 'W' then 
    begin
        dim[x,y]:='#';
        answer1:=answer1+1;
    end;

    if dir=0 then
    begin
        y:=y-1;
        //writeln('up');
    end
    else if dir=90 then
    begin
        x:=x+1;
        //writeln('right');
    end
    else if dir=180 then
    begin
        y:=y+1;
        //writeln('down');
    end 
    else if dir=270 then
    begin
        x:=x-1;
        //writeln('left');
    end;

    //writeln(k,' ',x,' ',y, ' ',dir, ' ',dim[x,y]);

    if x>maxx then maxx:=x;
    if y>maxy then maxy:=y;
    if x<minx then minx:=x;
    if x<miny then miny:=y;

    {
    for i:=size-10 to size+35 do 
    begin
        for j:=size-10 to size+35 do 
                write(dim[j,i]);
                write(' ');
        writeln('');
    end;    
    }
  end;



  writeln('asnewr is:');
  writeln(answer1);


{
  writeln('minx maxx miny maxy');
  writeln(minx,' ',maxx,' ',miny,' ',maxy);

  for i:=size-10 to size+35 do 
  begin
      for j:=size-10 to size+35 do 
            write(dim[i,j]);
            write(' ');
      writeln('');
  end;
}

end.

