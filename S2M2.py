import os
import sys
import argparse

def Parse():
    parser = argparse.ArgumentParser("S2M2")
    parser.add_argument("--input", help="path to .csv file created by SeCNV", type=str)
    parser.add_argument("--output", help="Output file in the form of path/name.tsv", type=str)
    args = parser.parse_args()

def CSVConvert(input, output, colnames="CELL\tchrom\tstart\tend\tCN\n"):
    tsv=list()
    locations=list()
    tsv.append(colnames)
    i=0
    with open(input,'r') as f:
        file=f.readlines()
        f.close()
    #print(len(file))
    for row in file:
        if i==0:
            names=row.split(',')
            j=0
            for chr in names:
                if j==0: pass
                else:
                    chrom="\tchr"+chr.split(':')[0][3:]+"\t"+chr.split(':')[1].split('-')[0]+"\t"+chr.split(':')[1].split('-')[1]
                    locations.append(chrom)
                j+=1
            #locations.append("\n")
            for k in range(len(file)-1):
                for l in range(len(locations)):
                    tsv.append(locations[l])
        else:
            names=row.split(',')
            name=names[0]
            j=0
            for cn in names:
                if j==0: pass
                elif j==1:
                    temp=tsv[((i-1)*(len(names)-1)+j)]
                    tsv[((i-1)*(len(names)-1)+j)]=name+temp+"\t"+cn
                else:
                    temp=tsv[((i-1)*(len(names)-1)+j)].replace("\n","")
                    tsv[((i-1)*(len(names)-1)+j)]="\n"+name+temp+"\t"+cn
                j+=1          
        i+=1
    with open(output, 'w') as f:
        for i in tsv:
            f.write(i)
        f.close()

if __name__=="__main__":
    args=Parse()
    CSVConvert(args.INPUT,args.OUTPUT)