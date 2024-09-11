import os
import argparse
def ParseArgs():
    parser = argparse.ArgumentParser(prog='VCF2TSV', description="Program that transforms a vcf file into a binary/ternary tsv file")
    parser.add_argument("-i", "--INPUT", metavar='Input', required=True,help="Path to the vcf file", type=str)
    parser.add_argument("-o", "--OUTPUT", metavar='Output', required=True,help="file path of output file in the form of /path/to/output.tsv", type=str)
    parser.add_argument("-t","--TYPE", metavar="type",required=True, choices=['binary','ternary'], help="Type of matrix you want, either 'binary' or 'ternary'", type=str)
    parser.add_argument("-s","--SPACING", metavar="spacing",required=True, choices=['tab','space'], help="Type of spacing separating the matrix, either 'tab' or 'space'", type=str)
    parser.add_argument("-l","--LIST", metavar="Sample list",required=False, default=None, help="Optional path to a text file for sample names if they are needed in a separate file.", type=str)
    return parser.parse_args()
def ValidateInputs(args):
    check=True
    if os.path.exists(args.INPUT) is False:
        print('Input file does not exist')
        check=False
    if args.OUTPUT.endswith('tsv') is False:
        print('Output file in incorrect format')
        check=False
        if args.SAMPLE is not None:
            if args.SAMPLE.endswith('txt') is False:
                print('Incorrect sample file format')
                check=False
    return check
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
    args=ParseArgs()
    check=ValidateInputs(args)
    if check==False:
        print("Validation of inputs failed.")
        exit(-1)
    if args.TYPE =='binary' and args.SPACING == 'tab':
        BinaryTab(args.INPUT,args.OUTPUT,args.LIST)
    elif args.TYPE == 'binary' and args.SPACING == 'space':
        BinarySpace(args.INPUT,args.OUTPUT,args.LIST)
    elif args.TYPE == 'ternary' and args.SPACING == 'tab':
        TernaryTab(args.INPUT,args.OUTPUT,args.LIST)
    else:
        TernarySpace(args.INPUT,args.OUTPUT,args.LIST)

if __name__=="__main__":
    Main()
#Usage: python VCFtoTSV.py -i (input) -o (output) -t(binary/ternary) -s(tab/space) -l(list)(optional)
