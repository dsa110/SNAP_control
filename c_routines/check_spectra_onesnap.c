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

  
  // number of inputs
  int SNAP = atoi(argv[1]);

  // set up socket
  struct addrinfo hints;
  struct addrinfo* res=0;
  memset(&hints,0,sizeof(hints));
  struct sockaddr_storage src_addr;
  socklen_t src_addr_len=sizeof(src_addr);
  hints.ai_family=AF_INET;
  hints.ai_socktype=SOCK_DGRAM;
  if (SNAP==1)
    getaddrinfo("10.10.3.1","4011",&hints,&res);
  if (SNAP==2)
    getaddrinfo("10.10.3.1","4012",&hints,&res);
  if (SNAP==3)
    getaddrinfo("10.10.3.1","4013",&hints,&res);
  if (SNAP==4)
    getaddrinfo("10.10.3.1","4014",&hints,&res);
  if (SNAP==5)
    getaddrinfo("10.10.3.1","4015",&hints,&res);
  int fd; 


  // read from socket

  // allocate memory
  float plx[2048], ply[2048];
  float specs[2048];

  char *rawdata = (char *)malloc(sizeof(char)*4104);
  ssize_t ct;
  int nreads = 10, i, j, n;
  
  for (j=0;j<2048;j++) specs[j] = 0.;

  int snapId, sId;
  unsigned short tmp;
  
  n=0;
  while (n<nreads) {
    
    fd = socket(res->ai_family,res->ai_socktype,res->ai_protocol);
    bind(fd,res->ai_addr,res->ai_addrlen);
    
    // read packet	   
    ct = recvfrom(fd,rawdata,4104,0,(struct sockaddr*)&src_addr,&src_addr_len);

    snapId = (int)rawdata[7];
    n++;
      
    for (i=0;i<512;i++) {
      for (j=0;j<4;j++) {
	tmp = 0;
	tmp |= (unsigned short)(rawdata[i*8+j*2+8]) << 8;
	tmp |= (unsigned short)(rawdata[i*8+j*2+1+8]);
	specs[i*4+3-j] += (float)(tmp);
      }
    }
   
    close(fd);
  }
  
  

  for (i=0;i<2048;i++) 
    specs[i] = 10.*log10(specs[i]/(1.*nreads));


  FILE *fout;
  fout = fopen("/mnt/nfs/runtime/spectra.txt","w");

  for (i=0;i<2048;i++) 
    fprintf(fout,"%g\n",specs[i]);
  

  fclose(fout);

  // free
  freeaddrinfo(res);
  free(rawdata);

}
