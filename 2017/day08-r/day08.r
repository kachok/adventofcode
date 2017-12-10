library(hash)

df <- read.delim("day08.input", sep=" ")

m<-as.matrix(df)

h <- hash() 


#register op value iff register2 comp value2
con = file("day08.input", "r")
while ( TRUE ) {
    line = readLines(con, n = 1)
    if ( length(line) == 0 ) {
        break
    }
    el<-strsplit(line, " ")[[1]]
    #print(cat(el[0])
    #cat(el[2],el[1])
    #print("")


    if (!(el[1]  %in% keys(h))) {
        h[el[1]]=0
    }

    if (!(el[5]  %in% keys(h))) {
        h[el[5]]=0
    }    
    
    cond<-FALSE

    reg<-el[5]
    com<-el[6]
    val<-el[7]
    val<-as.numeric(as.character(val))

    #sprintf("reg: %s, val: %s, com: %s", reg, val, com)
    #print("reg val cm")
    #print(reg)
    #print(val)
    #print(com)

    if (com==">" && (h[[reg]]>as.integer(val))) {
        cond<-TRUE
    }
    if (com=="<" &&(h[[reg]]<val)) {
        cond<-TRUE
    }
    if (com=="==" &&(h[[reg]]==val)) {
        cond<-TRUE
    }
    if (com==">="&& (h[[reg]]>=val)) {
        cond<-TRUE
    }
    if (com=="<=" &&(h[[reg]]<=val)) {
        cond<-TRUE
    }
    if (com=="!="&&(h[[reg]]!=val)) {
        cond<-TRUE
    }
    reg<-el[1]
    ops<-el[2]
    val<-el[3]
    val<-as.numeric(as.character(val))


    if (cond==TRUE) {
        if (ops =="dec"){
            #print(class(val))
            #print(val)
            #print(">>>>")
            h[reg]<-h[[reg]]-val
        }
        else
        {
            h[reg]<-h[[reg]]+val
        }
    }



}
close(con)


print(values(h)[[which.max(values(h))]])
