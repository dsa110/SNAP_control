calc_coefficients: calc_coefficients.c 
	gcc -o $@ $^ -I/usr/local/include -L/usr/local/lib -lm -O3

check_spectra: check_spectra_onesnap.c 
	gcc -o $@ $^ -I/usr/local/include -L/usr/local/lib -lm -O3

plot_spectra: plot_spectra.c 
	g++ -o $@ $^ -I/usr/local/include -L/usr/local/lib -lm -O3 -lcpgplot -lpgplot -lgfortran -lX11

