-- http://lua-users.org/wiki/FileInputOutput

-- see if the file exists
function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end
  
  -- get all lines from a file, returns an empty 
  -- list/table if the file does not exist
  function lines_from(file)
    if not file_exists(file) then return {} end
    lines = {}
    for line in io.lines(file) do 
      lines[#lines + 1] = line
    end
    return lines
  end
  
  -- tests the functions above
  local file = 'problem04.txt'
  local lines = lines_from(file)
  
  count=0

  -- print all line numbers and their contents
  for k,v in pairs(lines) do
    --print('line[' .. k .. ']', v)

    norepeats=true

    words = {}
    for s in v:gmatch("[^\r ]+") do
        -- turn word into characters, sort them and put that word into "words"
        t={}
        s:gsub(".",function(c) table.insert(t,c) end)   
        
        table.sort(t)

        sortedword=''
        for _, ch in pairs(t) do 
            sortedword=sortedword..ch 
        end

        --print(s,"-",sortedword)

        if words[sortedword]==nil then
            words[sortedword]=true
        else
            norepeats=false
            break
        end
    end


    if norepeats then count=count+1 end
  end

  print('Answer: ',count)