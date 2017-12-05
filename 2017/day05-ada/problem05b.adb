with Ada.Directories,
     Ada.Direct_IO,
     Ada.Text_IO;
 
with Ada.Strings; use Ada.Strings;

with Ada.Strings.UnBounded;

procedure Problem05b is
 


   File_Name : String  := "problem05.txt";
   File_Size : Natural := Natural (Ada.Directories.Size (File_Name));
 
   s : Ada.Strings.Unbounded.UnBounded_String;

   subtype File_String    is String (1 .. File_Size);
   package File_String_IO is new Ada.Direct_IO (File_String);
 
   File     : File_String_IO.File_Type;
   Contents : File_String;


   type Block_Collection is array (Positive range <>) of Integer;
   Jumps : Block_Collection (1 .. 1043);
   Offsets : Block_Collection (1 .. 1043);

   Index : Integer;
   Curr:Integer;
   Temp:Integer;
   Count:Integer;

begin
   File_String_IO.Open  (File, Mode => File_String_IO.In_File,
                               Name => File_Name);
   File_String_IO.Read  (File, Item => Contents);
   File_String_IO.Close (File);
 
   -- Ada.Text_IO.Put (Contents);

    Index:=0;
   for J in 1 .. Contents'Length loop
      
      if Contents(J) = Character'Val (10) then
        Index:=Index+1;

         --Ada.Text_IO.Put ("break is in Contents");
         --Ada.Text_IO.New_Line(1);
         --Ada.Text_IO.Put (Integer'Image(Index));
         --Ada.Text_IO.Put (Ada.Strings.Unbounded.To_String(s));
         --Ada.Strings.Unbounded.Overwrite(s, 0,Ada.Strings.Unbounded.To_Unbounded_String(""));

        Jumps(Index):=Integer'Value(Ada.Strings.Unbounded.To_String(s));
        Offsets(Index):=0;

         s:=Ada.Strings.Unbounded.To_Unbounded_String("");
         --Ada.Text_IO.New_Line(1);
      else
         --Ada.Text_IO.Put ("appending "&Contents(J));
         --Ada.Text_IO.New_Line(1);
         Ada.Strings.Unbounded.Append(s, Contents(J));

      end if;
   end loop;

Curr:=1;
Count:=0;
Until_Loop :
   loop
--Ada.Text_IO.Put ("count ");
--Ada.Text_IO.Put (Integer'Image(Count));
--Ada.Text_IO.Put (" curr ");
--Ada.Text_IO.Put (Integer'Image(Curr));
--Ada.Text_IO.Put (" jump ");
--Ada.Text_IO.Put (Integer'Image(Jumps(Curr)));
--Ada.Text_IO.Put (" off ");
--Ada.Text_IO.Put (Integer'Image(Offsets(Curr)));
--Ada.Text_IO.New_Line(1);

        Temp:=Curr;
        Curr:=Curr+Jumps(Curr);

        if Jumps(Temp) < 3 then
            Jumps(Temp):=Jumps(Temp)+1;
        else
            Jumps(Temp):=Jumps(Temp)-1;
        end if;
      
      Count:=Count+1;
      exit Until_Loop when Curr < 1 or Curr>1043;
   end loop Until_Loop;

Ada.Text_IO.Put ("answer is ");
Ada.Text_IO.Put (Integer'Image(Count));
Ada.Text_IO.New_Line(1);

end Problem05b;