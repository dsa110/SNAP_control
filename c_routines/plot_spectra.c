// -*- c++ -*-
#include <cpgplot.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


int main(int argc, char *argv[]) {

  
  // number of inputs
  int NSNAP = atoi(argv[1]);

  // allocate memory
  float plx[2048], ply[2048];
  float specs[NSNAP][2048];
  int i, snapId, sId;
  
  // read specs
  FILE *fin;
  fin=fopen("/mnt/nfs/runtime/spectra.txt","r");
  for (sId=0;sId<NSNAP;sId++) {
    for (i=0;i<2048;i++)
      fscanf(fin,"%f\n",&specs[sId][i]);
  }
  fclose(fin);

  // plot
  
  cpgbeg(0,"222/xs",1,1);
  cpgsfs(2);
  cpgslw(2.);
  cpgscf(2);
  cpgsch(1.4);

  cpgenv(1530.,1280.,-20.,50.,0,1);
  cpglab("Frequency (MHz)","Relative power (dB)","");

  for (i=0;i<2048;i++) plx[i] = 1530.-i*250./2048.;

  for (snapId=0;snapId<NSNAP;snapId++) {

    cpgsci(snapId+1);
    if (snapId==0) cpgptxt(1500.,40.,0.,0.,"1");
    if (snapId==1) cpgptxt(1480.,40.,0.,0.,"2");
    if (snapId==2) cpgptxt(1460.,40.,0.,0.,"3");
    if (snapId==3) cpgptxt(1440.,40.,0.,0.,"4");
    if (snapId==4) cpgptxt(1420.,40.,0.,0.,"5");
    for (i=0;i<2048;i++) {
      ply[i] = specs[snapId][i];
    }

    cpgline(2048,plx,ply);

  }

  cpgsci(1);
  for (i=0;i<2048;i++) ply[i] = 10.*log10(64.);
  cpgscr(1,1,1,1);
  cpgsls(2);
  cpgline(2048,plx,ply);

  

  
  cpgend();

}
