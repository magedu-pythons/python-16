#!usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     :2018/10/9 14:36
# @Author   : Sai Zhou
# @File     : make_control_group_1000K.py
# @Function :get_new_ref

import sys
import os
import re
import numpy
import csv
from operator import itemgetter
import string

if len(sys.argv) < 6:
    print('python' + sys.argv[0] + '  sample_gender_file  GC_correction_dir run_dir bin_size(1000K|100K) cv_input out_file_tsv \n')
    exit()

sample_gender_file = sys.argv[1]
GC_correction_dir =  sys.argv[2]
run_dir = sys.argv[3]
bin_size = sys.argv[4]
CV_input = sys.argv[5]
MMSC_last = sys.argv[6]

###### global arguments ######
if bin_size == "1000K":
    flag = "_" + bin_size + "_0.001_GC_corrected.tsv"
    hg_mask_file = "/data/software/ChromGo/pipeline/PGS/data/hg19.1000K.GC.mask.tsv"
if bin_size == "100K":
    flag = "_" + bin_size + "_0.001_GC_corrected.tsv"
    hg_mask_file = "/data/software/ChromGo/pipeline/PGS/data/hg19.100K.GC.mask.tsv"
temp_dir = run_dir + "/" + "ref_procedure_file/"
if os.path.exists(temp_dir):
    pass
else:
    os.mkdir(temp_dir)

###### read gender_file  ######
sample_gender_all = {}
sample_gender_female = {}
sample_gender_male = {}

with open(sample_gender_file) as SEX:
    sex_head = SEX.readline()
    for line in SEX.readlines():
        line = line.strip()
        temp_gender = line.split('\t')
        sample_gender_name = temp_gender[0]
        sample_gender_info = temp_gender[1]
        sample_gender_all[sample_gender_name] = sample_gender_info
        if sample_gender_info == "female":
            sample_gender_female[sample_gender_name] = sample_gender_info
        if sample_gender_info == "male":
            sample_gender_male[sample_gender_name] = sample_gender_info

###### read GC_correction_flie and get ration not include chrX and chrY ######
sample_name_from_GC = {}
all_sample_ration_file = temp_dir + "01_" + bin_size + "_all_sample_ration.txt"  ### 第1个临时文件:放的是所有样本的ration

path_dir = os.listdir(GC_correction_dir)
for alldir in path_dir:
    #if '_1000K_0.001_GC_corrected.tsv' in alldir:
    if flag in alldir:
        sample_name_GC = alldir.replace(flag,'')
        if sample_name_GC in sample_gender_all.keys():
            sample_name_from_GC[sample_name_GC] = "NA"


sample_bin_ration = {}
bin_chr_start_end = {}
for sample_name in sample_name_from_GC.keys():
    GC_correction_file = GC_correction_dir + "/" + sample_name + flag
    with open(GC_correction_file, 'rb') as GC:
        GC_all_info = csv.reader(GC, delimiter="\t")
        header = GC_all_info.next()
        for line_GC in GC_all_info:
            GC_bin = int(line_GC[1])
            GC_chr_bin = line_GC[2] + "_" + str(GC_bin)
            GC_chr_bin_stat_end = line_GC[1] + "\t" + line_GC[2] + "\t" + line_GC[3] + "\t" + line_GC[4]
            GC_ration = line_GC[18]
            bin_chr_start_end[GC_bin] = GC_chr_bin_stat_end
            if not sample_name in sample_bin_ration:
                sample_bin_ration[sample_name] = {}
            if not GC_bin in sample_bin_ration[sample_name]:
                sample_bin_ration[sample_name][GC_bin] = {}
            if not GC_chr_bin in sample_bin_ration[sample_name][GC_bin]:
                sample_bin_ration[sample_name][GC_bin][GC_chr_bin] = GC_ration

all_sample_ration_info = open(all_sample_ration_file, 'w')
for sample in sample_bin_ration.keys():
    #print(sample)
    all_sample_ration_info.writelines("\n" + sample)
    for bin_ID in sorted(sample_bin_ration[sample].keys()):
        #print(len(sample_bin_ration[sample]))
        #print(bin_ID)
        for chr_bin in sample_bin_ration[sample][bin_ID].keys():
            if (not re.search('chrX',chr_bin) and not re.search('chrY',chr_bin)):
                    #print(bin_ID)
                    all_sample_ration_info.writelines("\t" + str(sample_bin_ration[sample][bin_ID].get(chr_bin)))
                    #print(sample + "\t" + chr_bin + "\t" + str(bin_ID) + "\t" + str(sample_bin_ration[sample][chr_bin].get(bin_ID)))
all_sample_ration_info.close()

###### calculate mean sd  median cv for ration not include chrX and chrY ######
sample_list = []
row_number_list = []

data = open(all_sample_ration_file).read()
allinfo = re.split('\n',data.strip())
lines = len(allinfo)
temp_list = allinfo[1].split('\t')
col = len(temp_list)
row_number_list = numpy.zeros([lines,col -1])
n = 0
RA = open(all_sample_ration_file,'r')
skip = RA.readline()
for line_cal in RA.readlines():
    line_cal = line_cal.strip()
    cal_temp = line_cal.split('\t')

    for j in range(1,col):
        row_number_list[n][j-1] = cal_temp[j]
    n += 1

row_number_list_n = []
for i in range(0,col -1):
    list1 = [x[i] for x in row_number_list]
    row_number_list_n.append(list1)
###### above code has got a two dimension list,next according to this list to calculate the mean,median,sd,cv ######
MMSC_01_file = temp_dir + "02_" + bin_size + "_sample_MMSC_01.tsv"  ### 第2个临时文件:放的是 除chrX 和chrY 外的 4个值
MMSC1 = open(MMSC_01_file,'w')
for k in range(0,col - 1):
    list2 = row_number_list_n[k]
    list2_aver = numpy.average(list2)  # 这个不用
    list2_mean = numpy.mean(list2)  # 就取这个
    list2_median = numpy.median(list2)  # 没有问题
    list2_std = numpy.std(list2)  # 就是这个，但是和R的std有差异，比R偏小
    list2_var = numpy.var(list2)
    list2_cv = list2_std / list2_mean
    MMSC1.writelines(str(list2_mean) + "\t" + str(list2_std) + "\t" + str(list2_median) + "\t" + str(list2_cv) + "\n")

###### read  female sample GC_correction_flie and get ration only include chrX ######
female_sample_name_from_GC = {}
female_sample_ration_file = temp_dir + "03_" + bin_size + "_female_sample_ration.txt" ### 第3个临时文件:放的是 chrX 的 4个值

path_dir = os.listdir(GC_correction_dir)
for alldir in path_dir:
    #if '_1000K_0.001_GC_corrected.tsv' in alldir:
    if flag in alldir:
        #female_sample_name_GC = alldir.replace('_1000K_0.001_GC_corrected.tsv','')
        female_sample_name_GC = alldir.replace(flag, '')
        if female_sample_name_GC in sample_gender_female.keys():
            female_sample_name_from_GC[female_sample_name_GC] = "NA"


female_sample_bin_ration = {}
female_bin_chr_start_end = {}
for female_sample_name in female_sample_name_from_GC.keys():
    #print(female_sample_name)
    #female_GC_correction_file = GC_correction_dir + "/" + female_sample_name + "_1000K_0.001_GC_corrected.tsv"
    female_GC_correction_file = GC_correction_dir + "/" + female_sample_name + flag
    with open(female_GC_correction_file, 'rb') as GC_FE:
        FE_GC_all_info = csv.reader(GC_FE, delimiter="\t")
        header = FE_GC_all_info.next()
        for line_FE_GC in FE_GC_all_info:
            female_GC_bin = int(line_FE_GC[1])
            #print(GC_bin)
            female_GC_chr_bin = line_FE_GC[2] + "_" + str(female_GC_bin)
            #GC_chr_bin_stat_end = line_GC[1] + "\t" + line_GC[2] + "\t" + line_GC[3] + "\t" + line_GC[4]
            female_GC_ration = line_FE_GC[18]
            #female_bin_chr_start_end[female_GC_bin] = GC_chr_bin_stat_end
            #print(GC_ration)
            if not female_sample_name in female_sample_bin_ration:
                female_sample_bin_ration[female_sample_name] = {}
            if not female_GC_bin in female_sample_bin_ration[female_sample_name]:
                female_sample_bin_ration[female_sample_name][female_GC_bin] = {}
            if not female_GC_chr_bin in female_sample_bin_ration[female_sample_name][female_GC_bin]:
                female_sample_bin_ration[female_sample_name][female_GC_bin][female_GC_chr_bin] = female_GC_ration

female_sample_ration_info = open(female_sample_ration_file, 'w')
for fe_sample in female_sample_bin_ration.keys():
    #print(female_sample)
    female_sample_ration_info.writelines("\n" + fe_sample)
    for bin_ID_fe in sorted(female_sample_bin_ration[fe_sample].keys()):
        #print(len(sample_bin_ration[sample]))
        #print(bin_ID)
        for chr_bin_fe in female_sample_bin_ration[fe_sample][bin_ID_fe].keys():
            if (re.search('chrX',chr_bin_fe)):
                    #print(bin_ID)
                    female_sample_ration_info.writelines("\t" + str(female_sample_bin_ration[fe_sample][bin_ID_fe].get(chr_bin_fe)))
                    #print(sample + "\t" + chr_bin + "\t" + str(bin_ID) + "\t" + str(sample_bin_ration[sample][chr_bin].get(bin_ID)))
female_sample_ration_info.close()

###### calculate mean sd  median cv for ration only include chrX from female sample ######
sample_list_female = []
row_number_list_female = []

data_female = open(female_sample_ration_file).read()
allinfo_female = re.split('\n',data_female.strip())
lines_female = len(allinfo_female)
temp_list_female = allinfo_female[1].split('\t')
col_female = len(temp_list_female)
row_number_list_female = numpy.zeros([lines_female,col_female -1])
n_female = 0
FEM = open(female_sample_ration_file,'r')
skip = FEM.readline()
for line_cal_female in FEM.readlines():
    line_cal_female = line_cal_female.strip()
    cal_temp_female = line_cal_female.split('\t')

    for j_female in range(1,col_female):
        row_number_list_female[n_female][j_female-1] = cal_temp_female[j_female]
    n_female += 1

row_number_list_n_female = []
for i_female in range(0,col_female -1):
    list1_female = [x[i_female] for x in row_number_list_female]
    row_number_list_n_female.append(list1_female)

###### above code has got a two dimension list,next according to this list to calculate the mean,median,sd,cv ######
for k_female in range(0,col_female - 1):
    list2_female = row_number_list_n_female[k_female]
    list2_female_aver = numpy.average(list2_female)
    list2_female_mean = numpy.mean(list2_female)
    list2_female_median = numpy.median(list2_female)
    list2_female_std = numpy.std(list2_female)
    list2_female_var = numpy.var(list2_female)
    list2_female_cv = list2_female_std / list2_female_mean
    MMSC1.writelines(str(list2_female_mean) + "\t" + str(list2_female_std) + "\t" + str(list2_female_median) + "\t" + str(list2_female_cv) + "\n")

###### read  male sample GC_correction_flie and get ration only include chrY ######
male_sample_name_from_GC = {}
male_sample_ration_file = temp_dir + "04_" + bin_size + "_male_sample_ration.txt"  ### 第4个临时文件:放的是 chrY 的 4个值

path_dir = os.listdir(GC_correction_dir)
for alldir in path_dir:
    #if '_1000K_0.001_GC_corrected.tsv' in alldir:
    if flag in alldir:
        #male_sample_name_GC = alldir.replace('_1000K_0.001_GC_corrected.tsv', '')
        male_sample_name_GC = alldir.replace(flag,'')
        if male_sample_name_GC in sample_gender_male.keys():
            male_sample_name_from_GC[male_sample_name_GC] = "NA"


male_sample_bin_ration = {}
for male_sample_name in male_sample_name_from_GC.keys():
    #print(male_sample_name)
    #male_GC_correction_file = GC_correction_dir + "/" + male_sample_name + "_1000K_0.001_GC_corrected.tsv"
    male_GC_correction_file = GC_correction_dir + "/" + male_sample_name + flag
    with open(male_GC_correction_file, 'rb') as GC_MAL:
        MAL_GC_all_info = csv.reader(GC_MAL, delimiter="\t")
        header = MAL_GC_all_info.next()
        for line_MAL_GC in MAL_GC_all_info:
            male_GC_bin = int(line_MAL_GC[1])
            #print(GC_bin)
            male_GC_chr_bin = line_MAL_GC[2] + "_" + str(male_GC_bin)
            male_GC_ration = line_MAL_GC[18]
            if not male_sample_name in male_sample_bin_ration:
                male_sample_bin_ration[male_sample_name] = {}
            if not male_GC_bin in male_sample_bin_ration[male_sample_name]:
                male_sample_bin_ration[male_sample_name][male_GC_bin] = {}
            if not male_GC_chr_bin in male_sample_bin_ration[male_sample_name][male_GC_bin]:
                male_sample_bin_ration[male_sample_name][male_GC_bin][male_GC_chr_bin] = male_GC_ration

male_sample_ration_info = open(male_sample_ration_file, 'w')
for ma_sample in male_sample_bin_ration.keys():
    #print(female_sample)
    male_sample_ration_info.writelines("\n" + ma_sample)
    for bin_ID_ma in sorted(male_sample_bin_ration[ma_sample].keys()):
        #print(len(sample_bin_ration[sample]))
        #print(bin_ID)
        for chr_bin_ma in male_sample_bin_ration[ma_sample][bin_ID_ma].keys():
            if (re.search('chrY',chr_bin_ma)):
                    #print(bin_ID)
                    male_sample_ration_info.writelines("\t" + str(male_sample_bin_ration[ma_sample][bin_ID_ma].get(chr_bin_ma)))
                    #print(sample + "\t" + chr_bin + "\t" + str(bin_ID) + "\t" + str(sample_bin_ration[sample][chr_bin].get(bin_ID)))
male_sample_ration_info.close()

###### calculate mean sd  median cv for ration only include chrY from male sample ######
sample_list_male = []
row_number_list_male = []

data_male = open(male_sample_ration_file).read()
allinfo_male = re.split('\n',data_male.strip())
lines_male = len(allinfo_male)
temp_list_male = allinfo_male[1].split('\t')
col_male = len(temp_list_male)
row_number_list_male = numpy.zeros([lines_male,col_male -1])
n_male = 0
MA = open(male_sample_ration_file,'r')
skip = MA.readline()
for line_cal_male in MA.readlines():
    line_cal_male = line_cal_male.strip()
    cal_temp_male = line_cal_male.split('\t')

    for j_male in range(1,col_male):
        row_number_list_male[n_male][j_male-1] = cal_temp_male[j_male]
    n_male += 1

row_number_list_n_male = []
for i_male in range(0,col_male -1):
    list1_male = [x[i_male] for x in row_number_list_male]
    row_number_list_n_male.append(list1_male)
###### above code has got a two dimension list,next according to this list to calculate the mean,median,sd,cv ######
for k_male in range(0,col_male - 1):
    list2_male = row_number_list_n_male[k_male]
    list2_male_aver = numpy.average(list2_male)
    list2_male_mean = numpy.mean(list2_male)
    list2_male_median = (numpy.median(list2_male))*2
    list2_male_std = numpy.std(list2_male)
    list2_male_var = numpy.var(list2_male)
    list2_male_cv = list2_male_std / list2_male_mean
    MMSC1.writelines(str(list2_male_mean) + "\t" + str(list2_male_std) + "\t" + str(list2_male_median) + "\t" + str(list2_male_cv) + "\n")
MMSC1.close()  ## MMSC1 只有4个值

###### accoording to human masked bin file and a chosen CV value to deal with MMSC1 file ######
MMSC_01_mask_file = temp_dir + "05_" + bin_size + "_sample_MMSC_01_mask.tsv"
MMSC_01_mask_new_file = temp_dir + "06_" + bin_size  + "_sample_MMSC_01_new_mask.tsv"
MMSC_01_mask_new_chr_file = temp_dir + "07_" + bin_size + "_sample_MMSC_01_new_chr_mask.tsv"

bin_MMSC = {}

MMSC_02 = open(MMSC_01_file).read()
MMSC_02_info = re.split('\n',MMSC_02.strip())
lines_MMSC_02 = len(MMSC_02_info)
for bin_key in range(1,lines_MMSC_02 + 1):
    bin_MMSC[bin_key] = MMSC_02_info[bin_key -1] + "\t" + str(0)


MMSC_01_mask_file_info = open(MMSC_01_mask_file,'w')
for key in bin_MMSC.keys():
    #print(str(key) + "\t" + bin_MMSC.get(key) + "\t")
    MMSC_01_mask_file_info.writelines(str(key) + "\t" + bin_MMSC.get(key) + "\t" + str(0) + "\n")
MMSC_01_mask_file_info.close()

sample_MASK = {}
MMSC_01_mask_file_info_01 = open(MMSC_01_mask_file,'r')
MMSC_01_mask_new_file_info_01 = open(MMSC_01_mask_new_file,'w')
for line_01 in MMSC_01_mask_file_info_01.readlines():
    line_01 = line_01.strip()
    line_mask = line_01.split('\t')
    bin_mask = line_mask[0]
    bin_mean_mask = line_mask[1]
    bin_sd_mask = line_mask[2]
    bin_median_mask = line_mask[3]
    bin_CV_mask = line_mask[4]
    mask_value = line_mask[5]
    sample_MASK_all = str(bin_mask) + "\t" + str(bin_mean_mask) + "\t" + str(bin_sd_mask) + "\t" + str(bin_median_mask) + "\t" + str(bin_CV_mask)
    sample_MASK[sample_MASK_all] = mask_value
    if ( bin_CV_mask > CV_input):
        mask_value = 1
    if (bin_CV_mask == "nan"):
        mask_value = 1
    if (bin_median_mask == 0):
        mask_value = 1
    #print(sample_MASK_all + "\t" + str(mask_value))
    MMSC_01_mask_new_file_info_01.writelines(sample_MASK_all + "\t" + str(mask_value) + "\n")
MMSC_01_mask_file_info_01.close()
MMSC_01_mask_new_file_info_01.close()

hg_MASK = {}
hg_chr_start_end = {}
hg_mask_info = open(hg_mask_file,'r')
head_info = hg_mask_info.readline()
for hg_line in hg_mask_info.readlines():
    hg_line = hg_line.strip()
    hg_temp_list = hg_line.split('\t')
    bin_hg = hg_temp_list[0]
    chr_hg = hg_temp_list[1]
    chr_hg_start = hg_temp_list[2]
    chr_hg_end = hg_temp_list[3]
    hg_mask_value = hg_temp_list[12]
    hg_MASK[bin_hg] = hg_mask_value
    hg_chr_start_end[bin_hg] = bin_hg + "\t" + chr_hg + "\t" + str(chr_hg_start) + "\t" + str(chr_hg_end)


MMSC_01_mask_new_file_info_02 = open(MMSC_01_mask_new_file,'r')
MMSC_01_mask_new_chr_file_info = open(MMSC_01_mask_new_chr_file,'w')
MMSC_01_mask_new_chr_file_info.writelines("bin_ID" + "\t" + "chr" + "\t" + "start" + "\t" + "end" + "\t" + "bin_mean" + "\t" + "bin_sd" + "\t" + "bin_median" + "\t" + "bin_CV" + "\t" + "mask_sample" + "\t" + "mask_gh" + "\n")
for line_02 in MMSC_01_mask_new_file_info_02.readlines():
    line_02 = line_02.strip()
    line_02_list = line_02.split('\t')
    bin_new = line_02_list[0]
    except_bin_new = line_02_list[1] + "\t" + str(line_02_list[2]) + "\t" + str(line_02_list[3]) + "\t" + str(line_02_list[4]) + "\t" + str(line_02_list[5] + "\t" + str(hg_MASK[bin_new]))
    #print(except_bin_new)
    MMSC_01_mask_new_chr_file_info.writelines(hg_chr_start_end[bin_new] + "\t" + except_bin_new + "\n")
MMSC_01_mask_new_file_info_02.close()
MMSC_01_mask_new_chr_file_info.close()

#MMSC_last = "/data/Project/Project_PGD_reasearch_for_01B_ref/ref/analysis_for_ref/" + "last_sample_MMSC_01_new_chr_mask.tsv"
LAST = open(MMSC_last,'w')
MMSC_total = open(MMSC_01_mask_new_chr_file,'r')
HEAD = MMSC_total.readline()
LAST.writelines("bin_ID" + "\t" + "chr" + "\t" + "start" + "\t" + "end" + "\t" + "bin_mean" + "\t" + "bin_sd" + "\t" + "bin_median" + "\t" + "bin_CV" + "\t" + "mask" + "\t" + "weight" + "\n")
for line_total in MMSC_total.readlines():
    line_total = line_total.strip()
    #print(line_total)
    line_total_list = line_total.split('\t')
    median_total = line_total_list[6]
    #print(median_taotal)
    CV_total = line_total_list[7]
    mask_total_sample = line_total_list[8]
    mask_total_hg = line_total_list[9]
    if ( mask_total_hg == "1" ):
        mask_total_sample = "1"
    if (CV_total == "nan"):
        CV_total = "NA"
    if (median_total == "0"):
        mask_total_sample = "1"
    if mask_total_sample == "1":
        weight = 0
    else:
        weight = 1 /(string.atof(median_total))

    except_mask_total = (str(line_total_list[0]) + "\t" + str(line_total_list[1]) + "\t" + str(line_total_list[2]) + "\t" + str(line_total_list[3]) + "\t"+ str(line_total_list[4]) + "\t" + str(line_total_list[5]) + "\t" + str(median_total) + "\t" + str(CV_total) + "\t" + str(mask_total_sample) + "\t" + str(weight))
    #print(except_mask_total)
    LAST.writelines(except_mask_total + "\n")


