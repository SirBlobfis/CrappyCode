#include "/Users/joseph.hoffman/Documents/GitHub/CrappyCode/BrainFuck/BrainFuck.bf"
#include "/Users/joseph.hoffman/Documents/GitHub/CrappyCode/BrainFuck/BrainFuck.c"
#define CC "/usr/bin/gcc"

void usage(char **argv);
void generate(char *c_output_name);

FILE *outfile;
FILE *infile;


int main(int argc, char **argv){

char c;
char *output_name; /* name of the executable that will be made */
char *c_output_name; /* name of the C source file that is generated */
char compile_opts[256] = CC; /* this array will contain the compiler options */
int keep_file = 0; /* Keep the generated C source file? */
int verbose = 0; /* Use verbose output? */
int no_compile = 0; /* Don't compile, just generate C source file */

if(argc < 2){
usage(argv);
exit(1);
}

/* chk(argv); */

while(1){
c = getopt(argc, argv, "o:c:knvh");
if(c < 0) break;

switch(c){
case 'o':
output_name = optarg;
break;
case 'v':
verbose = 1;
break;
case 'h':
usage(argv);
break;
case 'k':
keep_file = 1;
break;
case 'c':
c_output_name = optarg;
break;
case 'n':
no_compile = 1;
keep_file = 1;
break;
}
}


if((optind >= argc) || (strcmp(argv[optind], "-") == 0)){
fprintf(stderr, "%s: no input file specified\n", argv[0]);
usage(argv);
exit(-1);
}

if(verbose)printf("[+] Opening %s...", argv[optind]);
if((infile = fopen(argv[optind], "r")) == 0){
if(verbose)printf("failed\n");
fprintf(stderr,"%s: could not open %s\n", argv[0], argv[optind]);
exit(-1);
}
if(verbose)printf("Ok\n");

if(!c_output_name)
c_output_name = "bf.out.c";

if(!output_name)
output_name = "bf.out";

if(verbose)printf("[+] Opening the output file...");
if((outfile = fopen(c_output_name, "w")) == 0){
if(verbose)printf("failed\n");
fprintf(stderr, "%s: error opening output file %s\n", argv[0],
c_output_name);
exit(-1);
}
if(verbose)printf("Ok\n");

if(verbose)printf("[+] Generating C source...");
generate(c_output_name);
if(verbose)printf("Ok\n");
fclose(outfile);
/*strcat(compile_opts, "/usr/bin/gcc");*/
strcat(compile_opts, " -o ");
strcat(compile_opts, output_name);
strcat(compile_opts, " ");
strcat(compile_opts, c_output_name);

if(!no_compile){
if(verbose){
printf("[+] Compiling...\n");
printf("Compiler: " CC "\n");
printf("Compile Options: %s\n", compile_opts);
}
system(compile_opts);
if(verbose)printf("Compiling Complete\n");
}

if(!keep_file){
if(verbose)printf("[+] Deleting intermediate file %s...", c_output_name);
unlink(c_output_name);
if(verbose)printf("Ok\n");
}
else
if(verbose)printf("[+] Keeping intermediate file %s...Ok\n",
c_output_name);

fclose(infile);
return(0);
}

void generate(char *c_output_name){
char c;

fprintf(outfile, "/*\n * This source was automatically generated with");
fprintf(outfile, "\n * obfc - The \"brainfuck compiler\".");
fprintf(outfile, "\n * katie ");
fprintf(outfile, "\n * \n */\n");
fprintf(outfile, "#include \n");
fprintf(outfile, "main() {\nchar a[30000],*ptr=a;\n");

while((c=fgetc(infile)) != EOF){
switch(c){
case '>': fprintf(outfile, "ptr++;\n"); break;
case '<': fprintf(outfile, "ptr--;\n"); break;
case '+': fprintf(outfile, "++*ptr;\n"); break;
case '-': fprintf(outfile, "--*ptr;\n"); break;
case '[': fprintf(outfile, "while(*ptr){\n"); break;
case ']': fprintf(outfile, "}\n"); break;
case '.': fprintf(outfile, "putchar(*ptr);\n"); break;
case ',': fprintf(outfile, "*ptr=getchar();\n"); break;
}
}
fprintf(outfile,"exit(0);\n}\n");
}



void usage (char *argv[]){

printf("obfc - the \"brainfuck compiler\"\n");
printf("by katie <katie@roachhd.com\n");
printf("\n");
printf("Usage: %s [OPTIONS] [FILE]\n",argv[0]);
printf("Available Options:\n");
printf("\t-o outfile\tspecify output file name\n");
printf("\t-k\t\tkeep the generated C source (normally bf.out.c)\n");
printf("\t-c c_outfile\tspecify C source file name. Only used option-\n");
printf("\t\t\tally in conjunction with -k option\n");
printf("\t-n\t\tDon't compile the C source, just output a copy of it\n");
printf("\t-v\t\tverbose output\n");
printf("\t-h\t\tdisplay help\n");
}