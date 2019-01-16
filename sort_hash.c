#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXL 5000000
float data[MAXL][4];
int compare(void *a, void *b){
	float *t1 = a, *t2 = b;
	for(int i = 0; i < 4; i++){
		if(t1[i] > t2[i]) return 1;
		if(t1[i] < t2[i]) return -1;
	}
	return 0;

}
int main(int argc, char *argv[]){
	if(argc != 3){
		printf("usage: ./sort_hash [input.hash] [sort_filename]\n");
		return 0;
	}
	FILE *f = fopen(argv[1], "r");
	float l1, l2, dt, offset;
	int count = 0;
	while(fscanf(f, "%f%f%f%f", &data[count][0] ,&data[count][1], &data[count][2], &data[count][3]) != EOF){
		count ++;
		if(count >= MAXL){
			printf("data out of bound\n");
			return 0;
		}
	}
	fclose(f);
	qsort(data, count, sizeof(data[0]), compare);
	char *outname = argv[2];
	f = fopen(outname, "w");

	for(int i = 0; i < count; i++){
		fprintf(f, "%.2f %.2f %.2f %.2f\n", data[i][0], data[i][1], data[i][2], data[i][3]);
	}
	fclose(f);
	return 0;
}