#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLEN 5000
#define MAXF 4000
float data[MAXLEN][MAXF];

int center_map[MAXLEN][MAXF] = {};
int min(int a, int b){
	if(a > b) return b;
	return a;
}
int max(int a, int b){
	if(a > b) return a;
	return b;
}
int main(int argc, char *argv[]){
	// inputfile down_t down_f
	if(argc != 4){
		printf("usage:./data2hash [input.data] [centerfilename] [hashfilename]\n");
		return 0;
	}
	char *filename = argv[1];
	FILE *file = fopen(filename, "r");
	char m_name[200];
	int size[2];
	int sr;
	int n_fft;
	fscanf(file, "%s", m_name);
	fscanf(file, "%d%d%d%d", &size[0], &size[1], &sr, &n_fft);
	float dt = (float)n_fft/4.0/sr;
	float df = (float)sr/n_fft;
	printf("read %s\n", filename);
	printf("data size = %d x %d\n", size[0], size[1]);
	int time_base = 0;
	int f_range_hz = 1700;
	int t_range_s = 4;
	int t_gap_s = 1;
	int f_sh = 1000;
	int t_f = (int)(f_range_hz/df);
	int t_time = (int)(t_range_s/dt); // target window

	int t_gap = (int)(t_gap_s/dt);
	// printf("%d %d %d\n", t_f, t_time, t_gap);
	char *centerfilename = argv[2];
	char *hashfilename = argv[3];
	FILE *centerfile = fopen(centerfilename, "w");
	printf("centerfile : %s\n", centerfilename);
	printf("hashfilename : %s\n", hashfilename);
	FILE *hashfile = fopen(hashfilename, "w");
	int count = 0;
	int w = 3;
	while(size[0] > 0){

		float e_sum[MAXLEN] = {};
		float e_total = 0;

		int len = min(size[0], MAXLEN);
		
		for(int i = 0; i < len; i++){
			for(int j = 0; j < size[1]; j++){
				fscanf(file, "%f", &data[i][j]);
				if(j*df < f_sh) continue; // if f < f_sh(Hz) ignore
				e_sum[i] += data[i][j];
				e_total += data[i][j];
			}
		}
		
		for(int i = 1; i < len-1; i++){
			// printf("%lf %lf\n", e_sum[i], e_sum[i]/size[1]);
			if(e_sum[i] < max(e_sum[i-1], e_sum[i+1])) continue;
			if(e_sum[i] < e_total/len) continue;
			for(int j = (int)(f_sh/df); j < size[1]-1; j++){
				// if(j*df < f_sh) continue; // if f < f_sh(Hz) ignore
				if(data[i][j] < e_sum[i]/(size[1]-(f_sh/df)) * 5) continue;
				int hit = 1;
				for(int m = 0; m < w && hit; m++){
					for(int n = 0; n < w && hit; n++){
						if(m == w/2 && n == w/2) continue;
						if(data[i-w/2+m][j-w/2+n] > data[i][j]){
							hit = 0;
						}
					}
				}
				if(hit){
					fprintf(centerfile, "%.2f %.2f %.2f\n", (i+time_base)*dt, j*df, data[i][j]);
					// printf("%.2f\n", data[i][j]);
					center_map[i][j] = 1;
				}
			}
		}
		for(int i = 0; i < len-t_gap; i++){
			for(int j = 0; j < size[1]; j++){
				if(center_map[i][j]){
					for(int m = 0; m < t_time; m++){
						for(int n = 0; n < t_f; n++){
							int px = i+t_gap+m;
							int py = j-t_f/2+n;
							if(px > len || py > MAXF || py < 0) continue;
							if(center_map[px][py]){
								fprintf(hashfile, "%.2f %.2f %.2f %.2f\n", j*df, py*df, (px-i)*dt, (time_base+i)*dt);
							}
						}
					}
				}
			}
		}
		memset(center_map, 0, sizeof(center_map));
		size[0] -= len;
		time_base += len;
	}
	return 0;
}