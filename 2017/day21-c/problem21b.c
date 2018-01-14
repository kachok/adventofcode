//
//
//.#.
//..#
//###

char a[3][3]={
    {'.','#','.'},
    {'.','.','#'},
    {'#','#','#'}
};

char b[3][3]={
    {'#','.','.'},
    {'#','.','#'},
    {'#','#','.'}
};




char two[2][2]={
    {' ',' '},
    {' ',' '}
};

char two2[2][2]={
    {' ',' '},
    {' ',' '}
};
char three[3][3]={
    {' ',' ',' '},
    {' ',' ',' '},
    {' ',' ',' '}
};

char three2[3][3]={
    {' ',' ',' '},
    {' ',' ',' '},
    {' ',' ',' '}
};

char four2[4][4]={
    {' ',' ',' ',' '},
    {' ',' ',' ',' '},
    {' ',' ',' ',' '},
    {' ',' ',' ',' '}
};

/**
int a[3][4] = {  
   {0, 1, 2, 3} ,   
   {4, 5, 6, 7} ,   
   {8, 9, 10, 11}   
};
*/

char a2[2][2];
char b2[2][2];
char a3[3][3]={
    {' ',' ',' '},
    {' ',' ',' '},
    {' ',' ',' '}
};
char b3[3][3]={
    {' ',' ',' '},
    {' ',' ',' '},
    {' ',' ',' '}
};
char a4[4][4]={
    {' ',' ',' ',' '},
    {' ',' ',' ',' '},
    {' ',' ',' ',' '},
    {' ',' ',' ',' '}
};
char b4[4][4]={
    {' ',' ',' ',' '},
    {' ',' ',' ',' '},
    {' ',' ',' ',' '},
    {' ',' ',' ',' '}
};

char arr[3000][3000];
char arr2[3000][3000];

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void copy(int n, char array[n][n], char array2[n][n]) {
    int i=0;
    int j=0;

    for (i=0;i<n;i++) {
        for (j=0;j<n;j++){
            array2[i][j]=array[i][j];
        }
    }
    return;
}


void printarr(int n, char array[n][n]) {
    int i=0;
    int j=0;

    for (i=0;i<n;i++){
        for(j=0;j<n;j++){
            //printf("%d",n);
            printf("%c",array[i][j]);
            printf("");        
        }
        printf("\n");
    };    
    return;
}

int compare(int n, char array[n][n], char array2[n][n]) {
    /* do something */
    int eq=1;

    int i=0;
    int j=0;

    for (i=0;i<n;i++) {
        for (j=0;j<n;j++){
            if (array[i][j]!=array2[i][j]) {
                eq=0;
                break;
            }
        }
        if (eq==0) {
            break;
        }
    }
    return eq;
}


void rotate(int n, char array[n][n], char array2[n][n]) {
    int i=0;
    int j=0;

    for (i=0;i<n;i++) {
        for (j=0;j<n;j++){
          array2[n-1-j][i]=array[i][j]; 
        }
    }
    return;
}

void mirror(int n, char array[n][n], char array2[n][n]) {
    int i=0;
    int j=0;

    for (i=0;i<n;i++) {
        for (j=0;j<n;j++){
          array2[i][n-1-j]=array[i][j]; 
        }
    }
    return;
}


int match(int n, char array[n][n], char array2[n][n]) {
    int m=0;

    if (n==2){
        if (compare(n,array,array2)==1) {
            return 1;
        }

        rotate(n, array2, two);

        if (compare(n,array, two)==1) {
            return 1;
        }
            
        copy(n,two, two2);
        rotate(n, two2, two);
        if (compare(n,array, two)==1) {
            return 1;
        }

        copy(n,two, two2);
        rotate(n, two, two2);
        if (compare(n,array, two)==1) {
            return 1;
        }

        copy(n,two, two2);
        mirror(n, two2, two);
        if (compare(n,array, two)==1) {
            return 1;
        }

        copy(n,two, two2);
        rotate(n, two2, two);
        if (compare(n,array, two)==1) {
            return 1;
        }

        copy(n,two, two2);
        rotate(n, two2, two);
        if (compare(n,array, two)==1) {
            return 1;
        }
        
        copy(n,two, two2);
        rotate(n, two2, two);
        if (compare(n,array, two)==1) {
            return 1;
        }
    }
    else if (n==3){
        if (compare(n,array,array2)==1) {
            return 1;
        }

        rotate(n, array2, three);

        if (compare(n,array, three)==1) {
            return 1;
        }
            
        copy(n,three, three2);
        rotate(n, three2, three);
        if (compare(n,array, three)==1) {
            return 1;
        }

        copy(n,three, three2);
        rotate(n, three, three2);
        if (compare(n,array, three)==1) {
            return 1;
        }

        copy(n,three, three2);
        mirror(n, three2, three);
        if (compare(n,array, three)==1) {
            return 1;
        }

        copy(n,three, three2);
        rotate(n, three2, three);
        if (compare(n,array, three)==1) {
            return 1;
        }

        copy(n,three, three2);
        rotate(n, three2, three);
        if (compare(n,array, three)==1) {
            return 1;
        }
        
        copy(n,three, three2);
        rotate(n, three2, three);
        if (compare(n,array, three)==1) {
            return 1;
        }
    }


  
    return 0;
}

//copy matrix to/from another matrix at specific position
void copyto (int n, int n2, char array[n][n], char array2[n2][n2], int x2, int y2) {
    int i=0;
    int j=0;

    for (i=0;i<n;i++) {
        for (j=0;j<n;j++){
            array2[i+x2][j+y2]=array[i][j];
        }
    }
    return;
}

void copyfrom (int n, int n2, char array[n][n], int x1, int y1, char array2[n2][n2]) {
    int i=0;
    int j=0;

    for (i=0;i<n2;i++) {
        for (j=0;j<n2;j++){
            array2[i][j]=array[i+x1][j+y1];
        }
    }
    return;
}

//parse matching pattern from line for 2x2 -> 3x3
void parse2 (char line[200], char array1[2][2], char array2[3][3]){
    // ##/## => ##./#.#/###
    char array11[2][2]={
    {line[0],line[1]},
    {line[3],line[4]}
    };
    char array22[3][3]={
    {line[9],line[10],line[11]},
    {line[13],line[14],line[15]},
    {line[17],line[18],line[19]}    
    };
/*
    char array22[3][3]={
    {line[9],line[13],line[17]},
    {line[10],line[14],line[18]},
    {line[11],line[15],line[19]}    
    };
*/
    copy(2, array11, array1);
    copy(3, array22, array2);

    return;

}

//parse matching pattern from line for 3x3 -> 4x4
void parse3 (char line[200], char array1[3][3], char array2[4][4]){
    // .../.../... => ##../.#../#.#./....
    char array11[3][3]={
    {line[0],line[1],line[2]},
    {line[4],line[5],line[6]},
    {line[8],line[9],line[10]}    
    };

    char array22[4][4]={
    {line[15],line[16],line[17],line[18]},
    {line[20],line[21],line[22],line[23]},
    {line[25],line[26],line[27],line[28]},
    {line[30],line[31],line[32],line[33]}
    };
/*
    char array22[4][4]={
    {line[15],line[20],line[25],line[30]},
    {line[16],line[21],line[26],line[31]},
    {line[17],line[22],line[27],line[32]},
    {line[18],line[23],line[28],line[33]}
    };
*/
    copy(3, array11, array1);
    copy(4, array22, array2);

    /*
    printf("parse3 > \n");
    printf("array11:\n");
    printarr(3, array11);
    printf("array22:\n");
    printarr(4, array22);
    printf("array1:\n");
    printarr(3, array1);
    printf("array2:\n");
    printarr(4, array2);
    printf("----\n\n");
    */

    return;
}

void iterate(int size, char arr[3000][3000], char arr2[3000][3000], char lines[108][200]) {
        printf("size is %d \n", size);   

        if (size % 2 == 0) {
            //printf("2->3 transform \n");    
            
            int x;
            int y;

            for (x=0;x<size/2;x++){
                for(y=0;y<size/2;y++){
                    //printf("x, y = %d, %d\n", x,y);    
                    //grab a 2x2 square into "two"
                    copyfrom(3000, 2, arr, x*2, y*2, a2);
                    
                    //looking for match
                    int l;
                    for (l=0; l<108; l++)
                    {
                        if (lines[l][6]=='=') {
                            parse2(lines[l],b2, b3);                            
                            if (match(2, a2, b2)==1) {                                
                                //printf("match found \n");    

                                copyto(3,3000, b3, arr2,x*3,y*3);
                                break;
                            }
                        }
                    }                                                        
                }
            }
        }
        else if (size % 3 == 0) {
            //printf("3->4 transform \n");    
            int x;
            int y;

            for (x=0;x<size/3;x++){
                for(y=0;y<size/3;y++){
                    //printf("x, y = %d, %d\n", x,y);    
                    //grab a 3x3 square into "three"
                    copyfrom(3000, 3, arr, x*3, y*3, a3);

                    //printf("three:\n");
                    //printarr(3, a3);
                    
                    //looking for match
                    int l;
                    for (l=0; l<108; l++)
                    {
                        if (lines[l][6]!='=') {
                            parse3(lines[l],b3, b4);     

                            if (match(3, a3, b3)==1) {    
                                /*
                                printf("line > ");
                                printf(lines[l]);
                                printf("three2:\n");
                                printarr(3, b3);
                                printf("four2:\n");
                                printarr(4, b4);
                                printf("----\n\n");
                                */

                                //printf("match!\n");                         
                                copyto(4,3000, b4, arr2,x*4,y*4);
                                break;
                            }
                        }
                    }                                                        
                }
            }            
        }    
    return;
}

int main()

{
    char lines[108][200];
    FILE *fp;
    fp=fopen("problem21.input", "r");

    int l;
    for (l=0; l<108; l++)
    {
        fgets(lines[l], 200, fp);
    }
    fclose(fp);

    for (l=0; l<108; l++)
    {
        printf(lines[l]);
        if (lines[l][6]=='=') {
            printf(">short\n");            
        } else {
            printf(">long\n");            
        }
        printf(">\n");
    }
        printf(">\n");
  



    int i=0;
    int j=0;
    int size=3;

    for (i=0;i<size;i++){
        for(j=0;j<size;j++){
            arr[i][j]=a[i][j];        
        }
    };


    printarr(3, three);
    //exit(0);

    int iter;
/*
    for(iter=0; iter<18;iter++){
        if (size % 2 == 0) {
            size = (size/2)*3;
        }
        else if (size % 3 == 0) {
            size = (size/3)*4;
        }    
    }

    printf("%d",size);
    exit(0);
*/

    for(iter=0; iter<18;iter++){
        printf("iteration: %d\n",iter+1);    
        printf("current size : %d\n",size);

        iterate(size, arr, arr2, lines);
        copy(3000, arr2, arr);

        if (size % 2 == 0) {
            size = (size/2)*3;
        }
        else if (size % 3 == 0) {
            size = (size/3)*4;
        }
        printf("new size : %d\n",size);
        printf("\n");


        int answer=0;

        //size=3;
        for (i=0;i<size;i++){
            for(j=0;j<size;j++){
                if(arr[i][j]=='#') {
                    answer=answer+1;
                }
            }
        };

        printf("current answer: %d\n\n", answer);
        //printarr(3000,arr);


        //exit(0);
    };


    int answer=0;

    //size=3;
    for (i=0;i<size;i++){
        for(j=0;j<size;j++){
            if(arr[i][j]=='#') {
                answer=answer+1;
            }
        }
    };

    //printf("arr\n");
    //printarr(3000, arr);

    //printf("arr2\n");
    //printarr(3000, arr2);

    printf("answer: %d", answer);

    
    return 0;



}


