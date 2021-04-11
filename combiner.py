import os
import glob
import pandas as pd
os.chdir("/Users/tejasvichabbra/Desktop/DRM_project/fo_DRM_data/fo_csv")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv[combined_csv['SYMBOL'].str.match('GMRINFRA')].to_csv( "/Users/tejasvichabbra/Desktop/DRM project/GMRINFRA_csv.csv", index=False, encoding='utf-8-sig')
# combined_csv.where(combined_csv['SYMBOL']=="GMRINFRA").to_csv( "GMRINFRA_csv.csv", index=False, encoding='utf-8-sig')