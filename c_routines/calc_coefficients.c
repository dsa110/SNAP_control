// -*- c++ -*-
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>

int main(int argc, char *argv[]) {

  char ip[100], port[100], server[100];

    if (argc!=7) {
      printf("Need IP, port, server as -ip, -port, -server\n");
      return 0;
    }
    
    for (int i=1;i<argc;i++) {
      if (strcmp(argv[i],"-ip")==0) {
	strcpy(ip,argv[i+1]);
      }
      if (strcmp(argv[i],"-port")==0) {
	strcpy(port,argv[i+1]);
      }
      if (strcmp(argv[i],"-server")==0) {
	strcpy(server,argv[i+1]);
      }

    }
    
    // set up socket
    struct addrinfo hints;
    struct addrinfo* res=0;
    memset(&hints,0,sizeof(hints));
    struct sockaddr_storage src_addr;
    socklen_t src_addr_len=sizeof(src_addr);
    hints.ai_family=AF_INET;
    hints.ai_socktype=SOCK_DGRAM;
    //hints.ai_protocol=0;
    getaddrinfo(ip,port,&hints,&res);
    int fd; 


    // read from socket

    // allocate memory
    float *stddev = (float *)malloc(sizeof(float)*8192);    
    char *rawdata = (char *)malloc(sizeof(char)*8200);
    ssize_t ct;
    int nreads = 9000, i, j;
    signed char a, b;

    for (i=0;i<8192;i++) stddev[i] = 0.;

    for (i=0;i<nreads;i++) {

    	fd = socket(res->ai_family,res->ai_socktype,res->ai_protocol);
    	bind(fd,res->ai_addr,res->ai_addrlen);

	if (i==0) printf("Waiting for packet\n");
	
    	// read packet	   
    	ct = recvfrom(fd,rawdata,8200,0,(struct sockaddr*)&src_addr,&src_addr_len);

    	
    	// add to rms	
    
	for (j=8;j<8200;j++) {

    	    a = ((unsigned char)(rawdata[j]) & 15) << 4;
	    b = (unsigned char)(rawdata[j]) & (15 << 4);

	    stddev[j-8] += ((float)(a*a+b*b))/(512.*nreads);
	}

	close(fd);



    }

    FILE *fout;
    char filenam[200];
    sprintf(filenam,"/mnt/nfs/runtime/%s_coeffs.dat",server);
    fout=fopen(filenam,"w");
    for (i=0;i<2048;i++) 
    	fprintf(fout,"%f %f %f %f\n",sqrt(stddev[i*4+3]),sqrt(stddev[i*4+2]),sqrt(stddev[i*4+1]),sqrt(stddev[i*4]));
    fclose(fout);
	

    // free
    freeaddrinfo(res);
    free(stddev);
    free(rawdata);

}
