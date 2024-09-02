import os
def TernarySpace(input,output,SampleFile=None,Names=True):
    SampleNames=''
    Locations=''
    check=True#One time check for formatting purposes if the tsv file doesn't want names. very annoying
    f=open(output, 'w+')
    x=os.popen('bcftools query -f \'[%SAMPLE:%POS:%GT:%CHROM ]\' '+input).read().split('\n')
    for i in x:
        for j in i.strip().split(' '):
            if ":" not in j: 
                pass
            else:
                if j.split(':')[0] not in SampleNames: 
                    SampleNames+=j.split(':')[0]+" "
                if Locations=='':
                    if Names: f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if j.split(':')[3]+j.split(':')[1] not in Locations:
                    check=True                    
                    f.write('\n')
                    if Names:f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if (j.split(":")[2].split('/')[0]=="."):
                    if not Names and not check or Names:
                        f.write(" 3")
                    else:
                        f.write("3")
                        check=False
                elif(j.split(":")[2].split('/')[0]=="0" and j.split(":")[2].split('/')[1]=="0"):
                    if not Names and not check or Names:                    
                        f.write(" 0")
                    else:
                        f.write("0")
                        check=False
                elif(j.split(":")[2].split('/')[0]!=j.split(":")[2].split('/')[1]):
                    if not Names and not check or Names:                    
                        f.write(" 1")
                    else:
                        f.write("1")
                        check=False
                else:
                    if not Names and not check or Names:                   
                        f.write(" 2")
                    else:
                        f.write('2')
                        check=False
    f.close()
    if SampleFile is not None:
        with open(SampleFile, 'w+') as f:
            f.write(SampleNames)
            f.close()

def TernaryTab(input,output, SampleFile=None, Names=True):
    SampleNames=''
    Locations=''
    check=True
    f=open(output, 'w+')
    x=os.popen('bcftools query -f \'[%SAMPLE:%POS:%GT:%CHROM ]\' '+input).read().split('\n')
    for i in x:
        for j in i.strip().split(' '):
            if ":" not in j: 
                pass
            else:
                if j.split(':')[0] not in SampleNames: 
                    SampleNames+=j.split(':')[0]+" "
                if Locations=='':
                    if Names: f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if j.split(':')[3]+j.split(':')[1] not in Locations:
                    check=True                    
                    f.write('\n')
                    if Names:f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if (j.split(":")[2].split('/')[0]=="."):
                    if not Names and not check or Names:
                        f.write("\t3")
                    else:
                        f.write("3")
                        check=False
                elif(j.split(":")[2].split('/')[0]=="0" and j.split(":")[2].split('/')[1]=="0"):
                    if not Names and not check or Names:                    
                        f.write("\t0")
                    else:
                        f.write("0")
                        check=False
                elif(j.split(":")[2].split('/')[0]!=j.split(":")[2].split('/')[1]):
                    if not Names and not check or Names:                    
                        f.write("\t1")
                    else:
                        f.write("1")
                        check=False
                else:
                    if not Names and not check or Names:                   
                        f.write("\t2")
                    else:
                        f.write('2')
                        check=False
    f.close()
    if SampleFile is not None:
        with open(SampleFile, 'w+') as f:
            f.write(SampleNames)
            f.close()

def BinarySpace(input,output,SampleFile=None,Names=True):
    SampleNames=''
    Locations=''
    check=True
    f=open(output, 'w+')
    x=os.popen('bcftools query -f \'[%SAMPLE:%POS:%GT:%CHROM ]\' '+input).read().split('\n')
    for i in x:
        for j in i.strip().split(' '):
            if ":" not in j: 
                pass
            else:
                if j.split(':')[0] not in SampleNames: 
                    SampleNames+=j.split(':')[0]+" "
                if Locations=='':
                    if Names: f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if j.split(':')[3]+j.split(':')[1] not in Locations:
                    check=True                    
                    f.write('\n')
                    if Names:f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if (j.split(":")[2].split('/')[0]=="."):
                    if not Names and not check or Names:
                        f.write(" 3")
                    else:
                        f.write("3")
                        check=False
                elif(j.split(":")[2].split('/')[0]=="0" and j.split(":")[2].split('/')[1]=="0"):
                    if not Names and not check or Names:                    
                        f.write(" 0")
                    else:
                        f.write("0")
                        check=False
                else:
                    if not Names and not check or Names:                    
                        f.write(" 1")
                    else:
                        f.write("1")
                        check=False
    f.close()
    if SampleFile is not None:
        with open(SampleFile, 'w+') as f:
            f.write(SampleNames)
            f.close()

def BinaryTab(input,output, SampleFile=None,Names=True):
    SampleNames=''
    Locations=''
    check=True
    f=open(output, 'w+')
    x=os.popen('bcftools query -f \'[%SAMPLE:%POS:%GT:%CHROM ]\' '+input).read().split('\n')
    for i in x:
        for j in i.strip().split(' '):
            if ":" not in j: 
                pass
            else:
                if j.split(':')[0] not in SampleNames: 
                    SampleNames+=j.split(':')[0]+" "
                if Locations=='':
                    if Names: f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if j.split(':')[3]+j.split(':')[1] not in Locations:
                    check=True
                    f.write('\n')
                    if Names:f.write(j.split(':')[1])
                    Locations+=j.split(':')[3]+j.split(':')[1]
                if (j.split(":")[2].split('/')[0]=="."):
                    if not Names and not check or Names:
                        f.write("\t3")
                    else:
                        f.write("3")
                        check=False
                elif(j.split(":")[2].split('/')[0]=="0" and j.split(":")[2].split('/')[1]=="0"):
                    if not Names and not check or Names:                    
                        f.write("\t0")
                    else:
                        f.write("0")
                        check=False
                else:
                    if not Names and not check or Names:                    
                        f.write("\t1")
                    else:
                        f.write("1")
                        check=False
    f.close()
    if SampleFile is not None:
        with open(SampleFile, 'w+') as f:
            f.write(SampleNames)
            f.close()

def Main():
    input="CRC24.ToySet.vcf"
    TS="ToyTS.tsv"
    TT="ToyTT.tsv"
    BS="ToyBS.tsv"
    BT="ToyBT.tsv"
    TernarySpace(input,TS,"ToySetSamn.txt")
    TernaryTab(input,TT)
    BinarySpace(input,BS)
    BinaryTab(input,BT)

if __name__=="__main__":
    Main()
